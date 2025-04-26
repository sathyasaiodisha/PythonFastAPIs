from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import DistrictOfficeBearer

router = APIRouter()

@router.get("/districtofficebearers/all")
def get_alldistrictofficebearers():
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        districtofficebearers = session.query(districtOfficeBearerModel).all()
        return districtofficebearers
    
@router.post("/districtofficebearers/add")
def create_districtofficebearer(districtId:int, designationId:int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        maxDistrictOfficeBearerId = session.query(func.max(districtOfficeBearerModel.ID)).scalar()
        
        new_districtOfficeBearer = districtOfficeBearerModel(ID = (maxDistrictOfficeBearerId + 1), DistrictID = districtId, DesignationID = designationId, OfficeBearerName = officebeaerername, 
                                                       AddressLine1 = adrline1, AddressLine2 = adrline2, AddressLine3 = adrline3,
                                                         ContactNo1 = contactno1, ContactNo2 = contactno2, Email = email, Gender = gender, CreatedBy = "Portal")
        session.add(new_districtOfficeBearer)
        session.commit()
        session.refresh(new_districtOfficeBearer)
        return {"message":"District Office Bearer created", "districtofficebearer_id":str(maxDistrictOfficeBearerId + 1)}
    
@router.put("/districtofficebearers/update/{id}")
def update_districtofficebearer(id: int, officebeaerername: str, adrline1: str, adrline2: str, adrline3: str, contactno1: str,
                   contactno2: str, email: str, gender: str):
    with SessionLocal() as session:
        districtOfficeBearerModel = DistrictOfficeBearer
        districtOfficeBearerToUpdate = session.query(districtOfficeBearerModel).filter(districtOfficeBearerModel.ID == id).first()
        if districtOfficeBearerToUpdate:
            districtOfficeBearerToUpdate.OfficeBearerName = officebeaerername
            districtOfficeBearerToUpdate.AddressLine1 = adrline1
            districtOfficeBearerToUpdate.AddressLine2 = adrline2
            districtOfficeBearerToUpdate.AddressLine3 = adrline3
            districtOfficeBearerToUpdate.ContactNo1 = contactno1
            districtOfficeBearerToUpdate.ContactNo2 = contactno2
            districtOfficeBearerToUpdate.Email = email
            districtOfficeBearerToUpdate.Gender = gender
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