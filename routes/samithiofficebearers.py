from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import SamithiOfficeBearer

router = APIRouter()

@router.get("/samithiofficebearers/all")
def get_allsamithiofficebearers():
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        samithiofficebearers = session.query(samithiOfficeBearerModel).all()
        return samithiofficebearers
    
@router.post("/samithiofficebearers/add")
def create_samithiofficebearer(samithiId:int, designationId:int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        maxSamithiOfficeBearerId = session.query(func.max(samithiOfficeBearerModel.ID)).scalar()
        
        new_samithiOfficeBearer = samithiOfficeBearerModel(ID = (maxSamithiOfficeBearerId + 1), SamithiID = samithiId, DesignationID = designationId, OfficeBearerName = officebeaerername, 
                                                       AddressLine1 = adrline1, AddressLine2 = adrline2, AddressLine3 = adrline3,
                                                         ContactNo1 = contactno1, ContactNo2 = contactno2, Email = email, Gender = gender, CreatedBy = "Portal")
        session.add(new_samithiOfficeBearer)
        session.commit()
        session.refresh(new_samithiOfficeBearer)
        return {"message":"Samithi Office Bearer created", "samithiofficebearer_id":str(maxSamithiOfficeBearerId + 1)}
    
@router.put("/samithiofficebearers/update/{id}")
def update_samithiofficebearer(id: int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        samithiOfficeBearerToUpdate = session.query(samithiOfficeBearerModel).filter(samithiOfficeBearerModel.ID == id).first()
        if samithiOfficeBearerToUpdate:
            samithiOfficeBearerToUpdate.OfficeBearerName = officebeaerername
            samithiOfficeBearerToUpdate.AddressLine1 = adrline1
            samithiOfficeBearerToUpdate.AddressLine2 = adrline2
            samithiOfficeBearerToUpdate.AddressLine3 = adrline3
            samithiOfficeBearerToUpdate.ContactNo1 = contactno1
            samithiOfficeBearerToUpdate.ContactNo2 = contactno2
            samithiOfficeBearerToUpdate.Email = email
            samithiOfficeBearerToUpdate.Gender = gender
            samithiOfficeBearerToUpdate.UpdatedBy = "Portal"
            session.commit()
            return {"message":f"Samithi Office Bearer with ID {id} updated"}
        return {"error": f"Samithi Office Bearer with ID {id} not found"}
    
@router.delete("/samithiofficebearers/delete/{id}")
def delete_samithiofficebearer(id: int):
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        samithiOfficeBearerToDelete = session.query(samithiOfficeBearerModel).filter(samithiOfficeBearerModel.ID == id).first()
        if samithiOfficeBearerToDelete:
            session.delete(samithiOfficeBearerToDelete)
            session.commit()
            return {"message":f"Samithi Office Bearer with ID {id} deleted"}
        return {"error": f"Samithi Office Bearer with ID {id} not found"}