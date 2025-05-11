from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import District
from pydantic import BaseModel

class DistrictToUpdate(BaseModel):
    distCode: str
    distName: str
    updatedBy: str

class DistrictToCreate(BaseModel):
    distCode: str
    distName: str
    createdBy: str

router = APIRouter()

@router.get("/saidistricts")
def get_saidistricts():
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistricts = session.query(saidistrictsModel).all()
        return saidistricts
    
@router.post("/saidistricts/add")
def create_saidistrict(saidistrict: DistrictToCreate):
    with SessionLocal() as session:
        try:
            saidistrictsModel = District
            maxIdLessThan50 = session.query(saidistrictsModel.ID).filter(saidistrictsModel.ID < 50).order_by(desc(saidistrictsModel.ID)).limit(1).scalar()            
            new_saidistrict = saidistrictsModel(ID=(maxIdLessThan50 + 1), DistrictName=saidistrict.distName, DistrictCode=saidistrict.distCode, CreatedBy=saidistrict.createdBy, UpdatedBy="PortalUser")
            
            session.add(new_saidistrict)
            session.commit()
            session.refresh(new_saidistrict)
            return {"message":"Sai district created", "saidistrict_id":new_saidistrict.ID}
        except Exception as ex:
            session.rollback()
            import traceback
            traceback.print_exc()
            return {"Error":ex}
    
@router.put("/saidistricts/update/{id}")
def update_saidistrict(id: int, saidistrict: DistrictToUpdate):
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistrictToUpdate = session.query(saidistrictsModel).filter(saidistrictsModel.ID == id).first()
        if saidistrictToUpdate:
            saidistrictToUpdate.DistrictCode = saidistrict.distCode
            saidistrictToUpdate.DistrictName = saidistrict.distName
            saidistrictToUpdate.UpdatedBy = saidistrict.updatedBy
            session.commit()
            return {"message":f"Sai district with ID {id} updated"}
        return {"error": f"Sai district with ID {id} not found"}
    
@router.delete("/saidistricts/delete/{id}")
def delete_saidistrict(id: int):
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistrictToDelete = session.query(saidistrictsModel).filter(saidistrictsModel.ID == id).first()
        if saidistrictToDelete:
            session.delete(saidistrictToDelete)
            session.commit()
            return {"message":f"Sai district with ID {id} deleted"}
        return {"error": f"Sai district with ID {id} not found"}