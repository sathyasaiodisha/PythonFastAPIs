from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from sqlalchemy import select
from models import DistrictOfficeBearer, District, Designation
from pydantic import BaseModel

class DistrictOfficialToUpdate(BaseModel):
    officebeaerername: str
    adrline1: str
    adrline2: str
    adrline3: str
    contactno1: str
    contactno2: str
    email: str
    gender: str
    updatedBy: str

class DistrictOfficialToCreate(BaseModel):
    districtId: int
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

@router.get("/districtofficebearers/all")
def get_alldistrictofficebearers():
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        districtModel = District
        designationModel = Designation
        
        statement = (select (
            districtOfficeBearerModel.ID,
            districtOfficeBearerModel.DesignationID,
            districtModel.DistrictCode,
            designationModel.DesignationCode,
            districtOfficeBearerModel.OfficeBearerName, 
            districtOfficeBearerModel.OfficeBearerName,
            districtOfficeBearerModel.AddressLine1,
            districtOfficeBearerModel.AddressLine2,
            districtOfficeBearerModel.AddressLine3,
            districtOfficeBearerModel.ContactNo1,
            districtOfficeBearerModel.ContactNo2,
            districtOfficeBearerModel.Email,
            districtOfficeBearerModel.Gender
        ).select_from(districtOfficeBearerModel).join(target=districtModel, onclause=districtOfficeBearerModel.DistrictID==districtModel.ID)
        .join(target=designationModel, onclause=districtOfficeBearerModel.DesignationID==designationModel.ID))
        
        districtOfficeBearers = session.execute(statement).mappings().all()

        return districtOfficeBearers
    
@router.get("/districtdesignations")
def get_districtdesignations():
    with SessionLocal() as session:
        districtDesignationModel = Designation
        districtDesignations = session.query(districtDesignationModel).filter(districtDesignationModel.OrgLevelID==2).all();
        return districtDesignations
    
@router.post("/districtofficebearers/add")
def create_districtofficebearer(districtOfficialToCreate: DistrictOfficialToCreate):
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        maxDistrictOfficeBearerId = session.query(func.max(districtOfficeBearerModel.ID)).scalar()
        
        new_districtOfficeBearer = districtOfficeBearerModel(ID = (maxDistrictOfficeBearerId + 1), 
                                                       DistrictID = districtOfficialToCreate.districtId,
                                                       DesignationID = districtOfficialToCreate.designationId, 
                                                       OfficeBearerName = districtOfficialToCreate.officebeaerername, 
                                                       AddressLine1 = districtOfficialToCreate.adrline1, 
                                                       AddressLine2 = districtOfficialToCreate.adrline2, 
                                                       AddressLine3 = districtOfficialToCreate.adrline3,
                                                       ContactNo1 = districtOfficialToCreate.contactno1, 
                                                       ContactNo2 = districtOfficialToCreate.contactno2, 
                                                       Email = districtOfficialToCreate.email, 
                                                       Gender = districtOfficialToCreate.gender, CreatedBy = "Portal")
        session.add(new_districtOfficeBearer)
        session.commit()
        session.refresh(new_districtOfficeBearer)
        return {"message":"District Office Bearer created", "districtofficebearer_id":str(maxDistrictOfficeBearerId + 1)}
    
@router.put("/districtofficebearers/update/{id}")
def update_districtofficebearer(id: int, districtOfficialToUpdate: DistrictOfficialToUpdate):
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        districtOfficeBearerToUpdate = session.query(districtOfficeBearerModel).filter(districtOfficeBearerModel.ID == id).first()
        if districtOfficeBearerToUpdate:
            districtOfficeBearerToUpdate.OfficeBearerName = districtOfficialToUpdate.officebeaerername
            districtOfficeBearerToUpdate.AddressLine1 = districtOfficialToUpdate.adrline1
            districtOfficeBearerToUpdate.AddressLine2 = districtOfficialToUpdate.adrline2
            districtOfficeBearerToUpdate.AddressLine3 = districtOfficialToUpdate.adrline3
            districtOfficeBearerToUpdate.ContactNo1 = districtOfficialToUpdate.contactno1
            districtOfficeBearerToUpdate.ContactNo2 = districtOfficialToUpdate.contactno2
            districtOfficeBearerToUpdate.Email = districtOfficialToUpdate.email
            districtOfficeBearerToUpdate.Gender = districtOfficialToUpdate.gender
            districtOfficeBearerToUpdate.UpdatedBy = "Portal"
            session.commit()
            return {"message":f"District Office Bearer with ID {id} updated"}
        return {"error": f"District Office Bearer with ID {id} not found"}
    
@router.delete("/districtofficebearers/delete/{id}")
def delete_districtofficebearer(id: int):
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        districtOfficeBearerToDelete = session.query(districtOfficeBearerModel).filter(districtOfficeBearerModel.ID == id).first()
        if districtOfficeBearerToDelete:
            session.delete(districtOfficeBearerToDelete)
            session.commit()
            return {"message":f"District Office Bearer with ID {id} deleted"}
        return {"error": f"District Office Bearer with ID {id} not found"}