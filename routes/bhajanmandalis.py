from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import BhajanMandali, Samithi
from pydantic import BaseModel

class BMToUpdate(BaseModel):
    bmRegNo: str
    bmName: str
    updatedBy: str

class BMToCreate(BaseModel):
    bmName: str
    bmRegNo: str
    samithiId: int
    createdBy: str

router = APIRouter()

@router.get("/bhajanmandalis")
def get_bhajanmandalis():
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandalis = session.query(bhajanmandaliModel).all()
        return bhajanmandalis
    
@router.get("/district/{districtId}/bhajanmandalis")
def get_bhajanmandalisbydistrict(districtId: int):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        samithiModel = Samithi
        bhajanmandalis = session.query(bhajanmandaliModel).filter((bhajanmandaliModel.SamithiID == samithiModel.ID) & (samithiModel.DistrictID == districtId)).all()
        return bhajanmandalis
    
@router.get("/samithi/{samithiId}/bhajanmandalis")
def get_bhajanmandalisbysamithi(samithiId: int):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandalis = session.query(bhajanmandaliModel).filter(bhajanmandaliModel.SamithiID == samithiId).all()
        return bhajanmandalis
    
@router.post("/bhajanmandalis/add")
def create_bhajanmandali(bmPayload: BMToCreate):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        maxBhajanMandaliId = session.query(func.max(bhajanmandaliModel.ID)).scalar()
        maxValOfBMCode = session.query(bhajanmandaliModel.BhajanMandaliCode).filter(bhajanmandaliModel.SamithiID==bmPayload.samithiId).order_by(desc(bhajanmandaliModel.BhajanMandaliCode)).limit(1).scalar()
        splitMaxValOfBMCode = (str(maxValOfBMCode)).split("-")
        intValOfLastIndex = splitMaxValOfBMCode[len(splitMaxValOfBMCode)-1]
        intValOfLastIndexOfItemToCreate = int(intValOfLastIndex) + 1
        strValOfLastIndexOfItemToCreate = str(intValOfLastIndexOfItemToCreate)
        strValOfLastIndexOfItemToCreateWithZFill = strValOfLastIndexOfItemToCreate.zfill(3)
        strValOfBMCodeToCreate = (str(maxValOfBMCode))[:-len(intValOfLastIndex)] + strValOfLastIndexOfItemToCreateWithZFill
        new_bhajanmandali = bhajanmandaliModel(ID = (maxBhajanMandaliId + 1), SamithiID = bmPayload.samithiId, BhajanMandaliCode = strValOfBMCodeToCreate, BhajanMandaliRegNo = bmPayload.bmRegNo, BhajanMandaliName = bmPayload.bmName, CreatedBy = "Portal")
        session.add(new_bhajanmandali)
        session.commit()
        session.refresh(new_bhajanmandali)
        return {"message":"Bhajan Mandali created", "bhajanmandali_id":strValOfBMCodeToCreate}
    
@router.put("/bhajanmandalis/update/{id}")
def update_bhajanmandali(id: int, bmPayload: BMToUpdate):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandaliToUpdate = session.query(bhajanmandaliModel).filter(bhajanmandaliModel.ID == id).first()
        if bhajanmandaliToUpdate:
            bhajanmandaliToUpdate.BhajanMandaliRegNo = bmPayload.bmRegNo
            bhajanmandaliToUpdate.BhajanMandaliName = bmPayload.bmName
            bhajanmandaliToUpdate.UpdatedBy = bmPayload.updatedBy
            session.commit()
            return {"message":f"Bhajan Mandali with ID {id} updated"}
        return {"error": f"Bhajan Mandali with ID {id} not found"}
    
@router.delete("/bhajanmandalis/delete/{id}")
def delete_bhajanmandali(id: int):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandaliToDelete = session.query(bhajanmandaliModel).filter(bhajanmandaliModel.ID == id).first()
        if bhajanmandaliToDelete:
            session.delete(bhajanmandaliToDelete)
            session.commit()
            return {"message":f"Bhajan Mandali with ID {id} deleted"}
        return {"error": f"Bhajan Mandali with ID {id} not found"}