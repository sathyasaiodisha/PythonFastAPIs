from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import Samithi
from pydantic import BaseModel

class SamithiToUpdate(BaseModel):
    samithiCode: str
    samithiName: str
    updatedBy: str

class SamithiToCreate(BaseModel):
    samithiName: str
    samithiRegNo: str
    districtId: int
    createdBy: str

router = APIRouter()

@router.get("/samithis")
def get_samithis():
    with SessionLocal() as session:
        samithisModel = Samithi
        samithis = session.query(samithisModel).all()
        return samithis
    
@router.get("/district/{districtId}/samithis")
def get_samithis_by_district(districtId: int):
    with SessionLocal() as session:
        samithisModel = Samithi
        samithis = session.query(samithisModel).filter(samithisModel.DistrictID==districtId).all()
        return samithis
    
@router.post("/samithis/add")
def create_samithi(samithiPayload: SamithiToCreate):
    with SessionLocal() as session:
        samithisModel = Samithi
        maxSamithiId = session.query(func.max(samithisModel.ID)).scalar()
        maxValOfSamithiCode = session.query(samithisModel.SamithiCode).filter(samithisModel.DistrictID==samithiPayload.districtId).order_by(desc(samithisModel.SamithiCode)).limit(1).scalar()
        splitMaxValOfSamithiCode = (str(maxValOfSamithiCode)).split("-")
        intValOfLastIndex = splitMaxValOfSamithiCode[len(splitMaxValOfSamithiCode)-1]
        intValOfLastIndexOfItemToCreate = int(intValOfLastIndex) + 1
        strValOfLastIndexOfItemToCreate = str(intValOfLastIndexOfItemToCreate)
        strValOfLastIndexOfItemToCreateWithZFill = strValOfLastIndexOfItemToCreate.zfill(3)
        strValOfSamithiCodeToCreate = (str(maxValOfSamithiCode))[:-len(intValOfLastIndex)] + strValOfLastIndexOfItemToCreateWithZFill
        new_samithi = samithisModel(ID = (maxSamithiId + 1), DistrictID = samithiPayload.districtId, SamithiCode = strValOfSamithiCodeToCreate, SamithiRegNo = samithiPayload.samithiRegNo, SamithiName = samithiPayload.samithiName, CreatedBy = samithiPayload.createdBy)
        session.add(new_samithi)
        session.commit()
        session.refresh(new_samithi)
        return {"message":"Samithi created", "samithi_id":strValOfSamithiCodeToCreate}
    
@router.put("/samithis/update/{id}")
def update_samithi(id: int, samithiPayload: SamithiToUpdate):
    with SessionLocal() as session:
        samithisModel = Samithi
        samithiToUpdate = session.query(samithisModel).filter(samithisModel.ID == id).first()
        if samithiToUpdate:
            samithiToUpdate.SamithiName = samithiPayload.samithiName
            samithiToUpdate.CreatedBy = "Portal"
            session.commit()
            return {"message":f"Samithi with ID {id} updated"}
        return {"error": f"Samithi with ID {id} not found"}
    
@router.delete("/samithis/delete/{id}")
def delete_samithi(id: int):
    with SessionLocal() as session:
        samithisModel = Samithi
        samithiToDelete = session.query(samithisModel).filter(samithisModel.ID == id).first()
        if samithiToDelete:
            session.delete(samithiToDelete)
            session.commit()
            return {"message":f"Samithi with ID {id} deleted"}
        return {"error": f"Samithi with ID {id} not found"}