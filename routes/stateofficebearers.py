from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from sqlalchemy import select
from models import StateOfficeBearer, Designation
from pydantic import BaseModel

class StateOfficialToUpdate(BaseModel):
    officebeaerername: str
    adrline1: str
    adrline2: str
    adrline3: str
    contactno1: str
    contactno2: str
    email: str
    gender: str
    updatedBy: str

class StateOfficialToCreate(BaseModel):
    designationId: int
    officebeaerername: str
    adrline1: str
    adrline2: str
    adrline3: str
    contactno1: str
    contactno2: str
    email: str
    gender: str
    createdBy: str

router = APIRouter()

@router.get("/stateofficebearers/all")
def get_allstateofficebearers():
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        designationModel = Designation
        
        statement = (select (
            StateOfficeBearer.ID,
            StateOfficeBearer.DesignationID,
            Designation.DesignationCode,
            StateOfficeBearer.OfficeBearerName, 
            StateOfficeBearer.OfficeBearerName,
            StateOfficeBearer.AddressLine1,
            StateOfficeBearer.AddressLine2,
            StateOfficeBearer.AddressLine3,
            StateOfficeBearer.ContactNo1,
            StateOfficeBearer.ContactNo2,
            StateOfficeBearer.Email,
            StateOfficeBearer.Gender
        ).select_from(stateOfficeBearerModel).join(target=designationModel, onclause=StateOfficeBearer.DesignationID==Designation.ID))
        
        stateOfficeBearers = session.execute(statement).mappings().all()

        return stateOfficeBearers
    
@router.get("/statedesignations")
def get_statedesignations():
    with SessionLocal() as session:
        stateDesignationModel = Designation
        stateDesignations = session.query(stateDesignationModel).filter(stateDesignationModel.OrgLevelID==1).all()
        return stateDesignations
    
@router.post("/stateofficebearers/add")
def create_stateofficebearer(stateOfficialToCreate: StateOfficialToCreate):
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        maxStateOfficeBearerId = session.query(func.max(stateOfficeBearerModel.ID)).scalar()
        
        new_stateOfficeBearer = stateOfficeBearerModel(ID = (maxStateOfficeBearerId + 1), 
                                                       DesignationID = stateOfficialToCreate.designationId, 
                                                       OfficeBearerName = stateOfficialToCreate.officebeaerername, 
                                                       AddressLine1 = stateOfficialToCreate.adrline1, 
                                                       AddressLine2 = stateOfficialToCreate.adrline2, 
                                                       AddressLine3 = stateOfficialToCreate.adrline3,
                                                       ContactNo1 = stateOfficialToCreate.contactno1, 
                                                       ContactNo2 = stateOfficialToCreate.contactno2, 
                                                       Email = stateOfficialToCreate.email, 
                                                       Gender = stateOfficialToCreate.gender, CreatedBy = "Portal")
        session.add(new_stateOfficeBearer)
        session.commit()
        session.refresh(new_stateOfficeBearer)
        return {"message":"State Office Bearer created", "stateofficebearer_id":str(maxStateOfficeBearerId + 1)}
    
@router.put("/stateofficebearers/update/{id}")
def update_stateofficebearer(id: int, stateOfficialToUpdate: StateOfficialToUpdate):
    with SessionLocal() as session:
        stateOfficeBearerModel = StateOfficeBearer
        stateOfficeBearerToUpdate = session.query(stateOfficeBearerModel).filter(stateOfficeBearerModel.ID == id).first()
        if stateOfficeBearerToUpdate:
            stateOfficeBearerToUpdate.OfficeBearerName = stateOfficialToUpdate.officebeaerername
            stateOfficeBearerToUpdate.AddressLine1 = stateOfficialToUpdate.adrline1
            stateOfficeBearerToUpdate.AddressLine2 = stateOfficialToUpdate.adrline2
            stateOfficeBearerToUpdate.AddressLine3 = stateOfficialToUpdate.adrline3
            stateOfficeBearerToUpdate.ContactNo1 = stateOfficialToUpdate.contactno1
            stateOfficeBearerToUpdate.ContactNo2 = stateOfficialToUpdate.contactno2
            stateOfficeBearerToUpdate.Email = stateOfficialToUpdate.email
            stateOfficeBearerToUpdate.Gender = stateOfficialToUpdate.gender
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