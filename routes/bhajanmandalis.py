from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import BhajanMandali

router = APIRouter()

@router.get("/bhajanmandalis")
def get_bhajanmandalis():
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandalis = session.query(bhajanmandaliModel).all()
        return bhajanmandalis
    
@router.post("/bhajanmandalis/add")
def create_bhajanmandali(samithiid:int, bhajanmandaliregno: str, bhajanmandaliname: str):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        maxBhajanMandaliId = session.query(func.max(bhajanmandaliModel.ID)).scalar()
        maxValOfBMCode = session.query(bhajanmandaliModel.BhajanMandaliCode).filter(bhajanmandaliModel.SamithiID==samithiid).order_by(desc(bhajanmandaliModel.BhajanMandaliCode)).limit(1).scalar()
        splitMaxValOfBMCode = (str(maxValOfBMCode)).split("-")
        intValOfLastIndex = splitMaxValOfBMCode[len(splitMaxValOfBMCode)-1]
        intValOfLastIndexOfItemToCreate = int(intValOfLastIndex) + 1
        strValOfLastIndexOfItemToCreate = str(intValOfLastIndexOfItemToCreate)
        strValOfLastIndexOfItemToCreateWithZFill = strValOfLastIndexOfItemToCreate.zfill(3)
        strValOfBMCodeToCreate = (str(maxValOfBMCode))[:-len(intValOfLastIndex)] + strValOfLastIndexOfItemToCreateWithZFill
        new_bhajanmandali = bhajanmandaliModel(ID = (maxBhajanMandaliId + 1), SamithiID = samithiid, BhajanMandaliCode = strValOfBMCodeToCreate, BhajanMandaliRegNo = bhajanmandaliregno, BhajanMandaliName = bhajanmandaliname, CreatedBy = "Portal")
        session.add(new_bhajanmandali)
        session.commit()
        session.refresh(new_bhajanmandali)
        return {"message":"Bhajan Mandali created", "bhajanmandali_id":strValOfBMCodeToCreate}
    
@router.put("/bhajanmandalis/update/{id}")
def update_bhajanmandali(id: int, samithiid:int, bhajanmandaliregno: str, bhajanmandaliname: str):
    with SessionLocal() as session:
        bhajanmandaliModel = BhajanMandali
        bhajanmandaliToUpdate = session.query(bhajanmandaliModel).filter(bhajanmandaliModel.ID == id).first()
        if bhajanmandaliToUpdate:
            bhajanmandaliToUpdate.SamithiID = samithiid
            bhajanmandaliToUpdate.BhajanMandaliRegNo = bhajanmandaliregno
            bhajanmandaliToUpdate.BhajanMandaliName = bhajanmandaliname
            bhajanmandaliToUpdate.UpdatedBy = "Portal"
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