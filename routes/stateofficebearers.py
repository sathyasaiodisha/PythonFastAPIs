from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import StateOfficeBearer

router = APIRouter()

@router.get("/stateofficebearers/all")
def get_allstateofficebearers():
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        stateOfficeBearers = session.query(stateOfficeBearerModel).all()
        return stateOfficeBearers
    
@router.post("/stateofficebearers/add")
def create_stateofficebearer(designationId:int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        maxStateOfficeBearerId = session.query(func.max(stateOfficeBearerModel.ID)).scalar()
        
        new_stateOfficeBearer = stateOfficeBearerModel(ID = (maxStateOfficeBearerId + 1), DesignationID = designationId, OfficeBearerName = officebeaerername, 
                                                       AddressLine1 = adrline1, AddressLine2 = adrline2, AddressLine3 = adrline3,
                                                         ContactNo1 = contactno1, ContactNo2 = contactno2, Email = email, Gender = gender, CreatedBy = "Portal")
        session.add(new_stateOfficeBearer)
        session.commit()
        session.refresh(new_stateOfficeBearer)
        return {"message":"State Office Bearer created", "stateofficebearer_id":str(maxStateOfficeBearerId + 1)}
    
@router.put("/stateofficebearers/update/{id}")
def update_stateofficebearer(id: int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        stateOfficeBearerToUpdate = session.query(stateOfficeBearerModel).filter(stateOfficeBearerModel.ID == id).first()
        if stateOfficeBearerToUpdate:
            stateOfficeBearerToUpdate.OfficeBearerName = officebeaerername
            stateOfficeBearerToUpdate.AddressLine1 = adrline1
            stateOfficeBearerToUpdate.AddressLine2 = adrline2
            stateOfficeBearerToUpdate.AddressLine3 = adrline3
            stateOfficeBearerToUpdate.ContactNo1 = contactno1
            stateOfficeBearerToUpdate.ContactNo2 = contactno2
            stateOfficeBearerToUpdate.Email = email
            stateOfficeBearerToUpdate.Gender = gender
            stateOfficeBearerToUpdate.UpdatedBy = "Portal"
            session.commit()
            return {"message":f"State Office Bearer with ID {id} updated"}
        return {"error": f"State Office Bearer with ID {id} not found"}
    
@router.delete("/stateofficebearers/delete/{id}")
def delete_stateofficebearer(id: int):
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        stateOfficeBearerToDelete = session.query(stateOfficeBearerModel).filter(stateOfficeBearerModel.ID == id).first()
        if stateOfficeBearerToDelete:
            session.delete(stateOfficeBearerToDelete)
            session.commit()
            return {"message":f"State Office Bearer with ID {id} deleted"}
        return {"error": f"State Office Bearer with ID {id} not found"}