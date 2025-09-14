from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from sqlalchemy import select
from models import SamithiOfficeBearer, District, Samithi, Designation
from pydantic import BaseModel

class SamithiOfficialToUpdate(BaseModel):
    officebeaerername: str
    adrline1: str
    adrline2: str
    adrline3: str
    contactno1: str
    contactno2: str
    email: str
    gender: str
    updatedBy: str

class SamithiOfficialToCreate(BaseModel):
    districtId: int
    samithiId: int
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

@router.get("/samithiofficebearers/all")
def get_allsamithiofficebearers():
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        districtModel = District
        samithiModel = Samithi
        designationModel = Designation
        
        statement = (select (
            samithiOfficeBearerModel.ID,
            samithiOfficeBearerModel.SamithiID,
            districtModel.ID,
            districtModel.DistrictCode,
            districtModel.DistrictName,
            samithiModel.SamithiCode,
            samithiModel.SamithiName,
            samithiOfficeBearerModel.DesignationID,
            designationModel.DesignationCode,
            samithiOfficeBearerModel.OfficeBearerName, 
            samithiOfficeBearerModel.OfficeBearerName,
            samithiOfficeBearerModel.AddressLine1,
            samithiOfficeBearerModel.AddressLine2,
            samithiOfficeBearerModel.AddressLine3,
            samithiOfficeBearerModel.ContactNo1,
            samithiOfficeBearerModel.ContactNo2,
            samithiOfficeBearerModel.Email,
            samithiOfficeBearerModel.Gender
        ).select_from(samithiOfficeBearerModel)
        .join(target=samithiModel, onclause=samithiOfficeBearerModel.SamithiID==samithiModel.ID)
        .join(target=districtModel, onclause=samithiModel.DistrictID==districtModel.ID)
        .join(target=designationModel, onclause=samithiOfficeBearerModel.DesignationID==designationModel.ID))
        
        samithiOfficeBearers = session.execute(statement).mappings().all()

        return samithiOfficeBearers
    
@router.get("/samithidesignations")
def get_samithidesignations():
    with SessionLocal() as session:
        samithiDesignationModel = Designation
        samithiDesignations = session.query(samithiDesignationModel).filter(samithiDesignationModel.OrgLevelID==3).all();
        return samithiDesignations
    
@router.post("/samithiofficebearers/add")
def create_samithiofficebearer(samithiOfficialToCreate: SamithiOfficialToCreate):
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        maxSamithiOfficeBearerId = session.query(func.max(samithiOfficeBearerModel.ID)).scalar()
        
        new_samithiOfficeBearer = samithiOfficeBearerModel(ID = (maxSamithiOfficeBearerId + 1), 
                                                       SamithiID = samithiOfficialToCreate.samithiId,
                                                       DesignationID = samithiOfficialToCreate.designationId, 
                                                       OfficeBearerName = samithiOfficialToCreate.officebeaerername, 
                                                       AddressLine1 = samithiOfficialToCreate.adrline1, 
                                                       AddressLine2 = samithiOfficialToCreate.adrline2, 
                                                       AddressLine3 = samithiOfficialToCreate.adrline3,
                                                       ContactNo1 = samithiOfficialToCreate.contactno1, 
                                                       ContactNo2 = samithiOfficialToCreate.contactno2, 
                                                       Email = samithiOfficialToCreate.email, 
                                                       Gender = samithiOfficialToCreate.gender, CreatedBy = "Portal")
        session.add(new_samithiOfficeBearer)
        session.commit()
        session.refresh(new_samithiOfficeBearer)
        return {"message":"Samithi Office Bearer created", "samithiofficebearer_id":str(maxSamithiOfficeBearerId + 1)}
    
@router.put("/samithiofficebearers/update/{id}")
def update_samithiofficebearer(id: int, samithiOfficialToUpdate: SamithiOfficialToUpdate):
    with SessionLocal() as session:
        samithiOfficeBearerModel = SamithiOfficeBearer
        samithiOfficeBearerToUpdate = session.query(samithiOfficeBearerModel).filter(samithiOfficeBearerModel.ID == id).first()
        if samithiOfficeBearerToUpdate:
            samithiOfficeBearerToUpdate.OfficeBearerName = samithiOfficialToUpdate.officebeaerername
            samithiOfficeBearerToUpdate.AddressLine1 = samithiOfficialToUpdate.adrline1
            samithiOfficeBearerToUpdate.AddressLine2 = samithiOfficialToUpdate.adrline2
            samithiOfficeBearerToUpdate.AddressLine3 = samithiOfficialToUpdate.adrline3
            samithiOfficeBearerToUpdate.ContactNo1 = samithiOfficialToUpdate.contactno1
            samithiOfficeBearerToUpdate.ContactNo2 = samithiOfficialToUpdate.contactno2
            samithiOfficeBearerToUpdate.Email = samithiOfficialToUpdate.email
            samithiOfficeBearerToUpdate.Gender = samithiOfficialToUpdate.gender
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