from database import SessionLocal, Base
from fastapi import APIRouter
from sqlmodel import func, desc

router = APIRouter()

@router.get("/samithis")
def get_samithis():
    with SessionLocal() as session:
        samithisModel = Base.classes.Samithi
        samithis = session.query(samithisModel).all()
        return samithis
    
@router.post("/samithis/add")
def create_samithi(districtid:int, samithiregno: str, samithiname: str):
    with SessionLocal() as session:
        samithisModel = Base.classes.Samithi
        maxSamithiId = session.query(func.max(samithisModel.ID)).scalar()
        maxValOfSamithiCode = session.query(samithisModel.SamithiCode).filter(samithisModel.DistrictID==districtid).order_by(desc(samithisModel.SamithiCode)).limit(1).scalar()
        splitMaxValOfSamithiCode = (str(maxValOfSamithiCode)).split("-")
        intValOfLastIndex = splitMaxValOfSamithiCode[len(splitMaxValOfSamithiCode)-1]
        intValOfLastIndexOfItemToCreate = int(intValOfLastIndex) + 1
        strValOfLastIndexOfItemToCreate = str(intValOfLastIndexOfItemToCreate)
        strValOfLastIndexOfItemToCreateWithZFill = strValOfLastIndexOfItemToCreate.zfill(3)
        strValOfSamithiCodeToCreate = (str(maxValOfSamithiCode))[:-len(intValOfLastIndex)] + strValOfLastIndexOfItemToCreateWithZFill
        new_samithi = samithisModel(ID = (maxSamithiId + 1), DistrictID = districtid, SamithiCode = strValOfSamithiCodeToCreate, SamithiRegNo = samithiregno, SamithiName = samithiname, CreatedBy = "Portal")
        session.add(new_samithi)
        session.commit()
        session.refresh(new_samithi)
        return {"message":"Samithi created", "samithi_id":strValOfSamithiCodeToCreate}
    
@router.put("/samithis/update/{id}")
def update_saidistrict(id: int, districtid:int, samithiregno: str, samithiname: str):
    with SessionLocal() as session:
        samithisModel = Base.classes.Samithi
        samithiToUpdate = session.query(samithisModel).filter(samithisModel.ID == id).first()
        if samithiToUpdate:
            samithiToUpdate.DistrictID = districtid
            samithiToUpdate.SamithiRegNo = samithiregno
            samithiToUpdate.SamithiName = samithiregno
            samithiToUpdate.CreatedBy = "Portal"
            session.commit()
            return {"message":f"Samithi with ID {id} updated"}
        return {"error": f"Samithi with ID {id} not found"}
    
@router.delete("/samithis/delete/{id}")
def update_saidistrict(id: int):
    with SessionLocal() as session:
        samithisModel = Base.classes.Samithi
        samithiToDelete = session.query(samithisModel).filter(samithisModel.ID == id).first()
        if samithiToDelete:
            session.delete(samithiToDelete)
            session.commit()
            return {"message":f"Samithi with ID {id} deleted"}
        return {"error": f"Samithi with ID {id} not found"}