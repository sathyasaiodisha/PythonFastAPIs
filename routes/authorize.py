from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import SessionLocal
from jose import JWTError, jwt
from utils.authutil import hashPassword, verifyPassword
from models import AdminUser, AdminJurisdiction, t_AdminUserJurisdiction, District
from datetime import datetime, timedelta
from typing import Optional

# Secret & settings
SECRET_KEY = "SUPER_SECRET_KEY"  # change in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def verify_password(plain_password, hashed_password):
    return verifyPassword(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    with SessionLocal() as session:
        dataadmins = AdminUser
        dataAdminToValidate = session.query(dataadmins).filter(dataadmins.UserName == username).first()
        
        if not dataAdminToValidate or not verify_password(password, dataAdminToValidate.Password):
            return None
        return dataAdminToValidate

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        juris: str = payload.get("juris")
        if username is None or juris is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    with SessionLocal() as session:
        dataadmins = AdminUser
        user = session.query(dataadmins).filter(dataadmins.UserName == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return {"username": username, "juris": juris}

def require_role(required_role: str):
    async def role_checker(user=Depends(get_current_user)):
        if user["juris"] != required_role:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return user
    return role_checker


router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    with SessionLocal() as session:
        adminUserJurisdictions = t_AdminUserJurisdiction
        userJurisdictionMapping = session.query(adminUserJurisdictions).filter(adminUserJurisdictions.c.AdminUserID == user.ID).first()

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.UserName, "juris": userJurisdictionMapping.JurisdictionID},
            expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/admin-only")
async def admin_route(user=Depends(require_role("admin"))):
    return {"msg": f"Hello {user['username']}, you are an Admin!"}

@router.get("/user-only")
async def user_route(user=Depends(require_role("user"))):
    return {"msg": f"Hello {user['username']}, you are a User!"}