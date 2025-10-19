from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from sqlalchemy import select, insert
from models import AdminUser, AdminJurisdiction, t_AdminUserJurisdiction, District
from pydantic import BaseModel
from passlib.context import CryptContext
from utils.authutil import hashPassword

class DataAdminToUpdate(BaseModel):
    userJurisdiction: int
    userDistrict: int
    userName: str
    userEmail: str
    userPwd: str
    updatedBy: str

class DataAdminToCreate(BaseModel):
    userJurisdiction: int
    userDistrict: int
    userName: str
    userEmail: str
    userPwd: str
    createdBy: str

router = APIRouter()

@router.get("/dataadmins/all")
def get_alldataadmins():
    with SessionLocal() as session:
        dataAdminsModel = AdminUser
        dataAdminJurisdictionModel = AdminJurisdiction
        districtModel = District
        
        # selectRoleStmt = select(t_UserRoles).where(t_UserRoles.c.RoleID)

        statement = (select (
            dataAdminsModel.ID,
            dataAdminsModel.UserName,
            dataAdminsModel.UserEmail,
            districtModel.ID,
            districtModel.DistrictName,
            dataAdminJurisdictionModel.ID,
            dataAdminJurisdictionModel.Jurisdiction
        ).select_from(dataAdminsModel)
        .join(target=t_AdminUserJurisdiction, onclause=dataAdminsModel.ID==t_AdminUserJurisdiction.c.AdminUserID)
        .join(target=dataAdminJurisdictionModel, onclause=t_AdminUserJurisdiction.c.JurisdictionID==dataAdminJurisdictionModel.ID)
        .join(target=districtModel, onclause=dataAdminsModel.DistrictID==districtModel.ID))
        
        dataAdmins = session.execute(statement).mappings().all()

        return dataAdmins
    
@router.get("/dataadminjurisdictions")
def get_dataadminjurisdictions():
    with SessionLocal() as session:
        jurisdictionModel = AdminJurisdiction
        adminJurisdictions = session.query(jurisdictionModel).all();
        return adminJurisdictions
    
@router.post("/dataadmins/add")
def create_dataadmin(dataadminToCreate : DataAdminToCreate):
    with SessionLocal() as session:
        dataAdminModel = AdminUser
        recordCount = session.query(func.count(dataAdminModel.ID)).scalar()
        if recordCount == 0:
            maxDataAdminId = 0;    
        else:
            maxDataAdminId = session.query(func.max(dataAdminModel.ID)).scalar()

        
        
        new_dataAdmin = dataAdminModel(ID = (maxDataAdminId + 1), 
                                        DistrictID = dataadminToCreate.userDistrict if dataadminToCreate.userDistrict != -1 else None,
                                        UserName = dataadminToCreate.userName,
                                        UserEmail = dataadminToCreate.userEmail,
                                        Password = hashPassword(dataadminToCreate.userPwd),
                                        CreatedBy = "Portal")
        session.add(new_dataAdmin)
        session.commit()

        adminUser = session.get(AdminUser, maxDataAdminId+1)
        adminRole = session.get(AdminJurisdiction, dataadminToCreate.userJurisdiction)
        
        adminJurisdictionModel = t_AdminUserJurisdiction
        insertUserRole = insert(adminJurisdictionModel).values(AdminUserID=maxDataAdminId+1, JurisdictionID=dataadminToCreate.userJurisdiction, CreatedBy="Portal")
        session.execute(insertUserRole)
        session.commit()
        
        session.refresh(new_dataAdmin)
        return {"message":"Data Admin created", "Data Admin Id":str(maxDataAdminId + 1)}
    
@router.put("/dataadmins/update/{id}")
def update_dataadmin(id: int, dataadminToUpdate: DataAdminToUpdate):
    with SessionLocal() as session:
        dataadminModel = AdminUser
        dataaminUserToUpdate = session.query(dataadminModel).filter(dataadminModel.ID == id).first()
        if dataaminUserToUpdate:
            dataaminUserToUpdate.UserName = dataadminToUpdate.userName
            dataaminUserToUpdate.UserEmail = dataadminToUpdate.userEmail
            dataaminUserToUpdate.Password = hashPassword(dataadminToUpdate.userPwd)
            
            dataaminUserToUpdate.UpdatedBy = "Portal"
            session.commit()
            return {"message":f"Data Admin with ID {id} updated"}
        return {"error": f"Data Admin with ID {id} not found"}
    
@router.delete("/dataadmins/delete/{id}")
def delete_districtofficebearer(id: int):
    with SessionLocal() as session:
        dataadminModel = AdminUser
        dataAdminUserToDelete = session.query(dataadminModel).filter(dataadminModel.ID == id).first()
        if dataAdminUserToDelete:
            session.delete(dataAdminUserToDelete)
            session.commit()
            return {"message":f"Data Admin with ID {id} deleted"}
        return {"error": f"Data Admin with ID {id} not found"}