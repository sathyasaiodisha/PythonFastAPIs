from database import SessionLocal
from fastapi import APIRouter, File, UploadFile, HTTPException
from sqlmodel import func, desc
from models import District, Samithi, BhajanMandali, BalVikasGuru, BalVikasCentre, BalVikasSubjects, BVGuruGradMajorSubject, BVClassPlaceCategory, BVGuruQualification, BVGuruOccupation, GuruSkillset
from pydantic import BaseModel
import shutil
import os

class BVGuruToUpdate(BaseModel):
    guruID: int
    districtID: int
    samithiID: int
    bmID: int
    bvCentreID: int
    guruName: str
    dateOfBirth: str
    addressLine1: str
    addressLine2: str
    addressLine3: str
    pinCode: str
    contactNo1: str
    contactNo2: str
    eMail: str
    gender: str
    highestEduDegreeID: int
    gradMajorSubID: int
    occupationID: int
    alumnusOf: str
    photo: str
    targetGroups: str
    updatedBy: str

class BVGuruToCreate(BaseModel):
    districtID: int
    samithiID: int
    bmID: int
    bvCentreID: int
    guruName: str
    dateOfBirth: str
    addressLine1: str
    addressLine2: str
    addressLine3: str
    pinCode: str
    contactNo1: str
    contactNo2: str
    eMail: str
    gender: str
    highestEduDegreeID: int
    gradMajorSubID: int
    occupationID: int
    alumnusOf: str
    photo: str
    targetGroups: str
    createdBy: str

router = APIRouter()

@router.get("/bvgurus")
def get_bvgurus():
    with SessionLocal() as session:
        balvikasGuruModel = BalVikasGuru
        balvikasGurus = session.query(balvikasGuruModel).all()
        return balvikasGurus
    
@router.get("/bhajanmandali/{bmId}/balvikascentres")
def get_balvikascentres(bmId: int):
    with SessionLocal() as session:
        bvcentreModel = BalVikasCentre
        bvCentres = session.query(bvcentreModel).filter((bvcentreModel.BhajanMandaliID == bmId)).all()
        return bvCentres


@router.get("/bvguruqualifications")
def get_bvguruqualifications():
    with SessionLocal() as session:
        bvguruQualiicationsModel = BVGuruQualification
        bvguruQualiications = session.query(bvguruQualiicationsModel).all()
        return bvguruQualiications
    
@router.get("/bvgurumajorsubjects")
def get_bvsubjects():
    with SessionLocal() as session:
        bvGuruSubjectsModel = BVGuruGradMajorSubject
        bvGuruMajorSubjects = session.query(bvGuruSubjectsModel).all()
        return bvGuruMajorSubjects
    
@router.get("/bvguruoccupations")
def get_bvoccupations():
    with SessionLocal() as session:
        bvOccupationsModel = BVGuruOccupation
        bvOccupations = session.query(bvOccupationsModel).all()
        return bvOccupations
    
@router.get("/guruskillsets")
def get_guruskillsets():
    with SessionLocal() as session:
        guruSkillsetsModel = GuruSkillset
        guruSkillsets = session.query(guruSkillsetsModel).all()
        return guruSkillsets

@router.post("/uploadguruphoto")
async def upload_guru_photo(file: UploadFile = File(...)):
    try:
        upload_dir = "/var/www/PHOTOS/BalVikasGurus"
        base_url = "http://172.93.223.88:8080/guruphotos"
        # Construct file path
        file_path = os.path.join(upload_dir, file.filename)
        file_url = f"{base_url}/{file.filename}"

        # Save file to the folder
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"message": "Upload successful", "fileurl": file_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/bvgurus/add")
def create_bvguru(bvguruPayload: BVGuruToCreate):
    with SessionLocal() as session:
        bvguruModel = BalVikasGuru
        maxBVGuruId = session.query(func.max(bvguruModel.ID)).scalar()
        
        new_bvguru = bvguruModel(ID = (maxBVGuruId + 1), DistrictID = bvguruPayload.districtID, 
                                 SamithiID = bvguruPayload.samithiID, BhajanMandaliID = bvguruPayload.bmID, 
                                 BVCentreID = bvguruPayload.bvCentreID, GuruName = bvguruPayload.guruName, 
                                 DateOfBirth = bvguruPayload.dateOfBirth, AddressLine1 = bvguruPayload.addressLine1,
                                 AddressLine2 = bvguruPayload.addressLine2, AddressLine3 = bvguruPayload.addressLine3,
                                 PIN = bvguruPayload.pinCode, ContactNo1 = bvguruPayload.contactNo1,
                                 ContactNo2 = bvguruPayload.contactNo2, Email = bvguruPayload.eMail,
                                 Gender = bvguruPayload.gender, HighestEduDegreeID = bvguruPayload.highestEduDegreeID,
                                 GraduationMajorSubjectID = bvguruPayload.gradMajorSubID, OccupationID = bvguruPayload.occupationID,
                                 AlumnusOf = bvguruPayload.alumnusOf, Photo = bvguruPayload.photo,
                                 TargetGroupsOfStudents = bvguruPayload.targetGroups,
                                 CreatedBy = "Portal")
        session.add(new_bvguru)
        session.commit()
        session.refresh(new_bvguru)
        return {"message":"Bal Vikas Guru added", "ID":(maxBVGuruId + 1)}
    
@router.put("/bvgurus/update/{id}")
def update_bvguru(id: int, bvguruPayload: BVGuruToUpdate):
    with SessionLocal() as session:
        bvguruModel = BalVikasGuru
        bvguruUpdate = session.query(bvguruModel).filter(bvguruModel.ID == id).first()
        if bvguruUpdate:
            bvguruUpdate.DistrictID = bvguruPayload.districtID
            bvguruUpdate.SamithiID = bvguruPayload.samithiID
            bvguruUpdate.BhajanMandaliID = bvguruPayload.bmID
            bvguruUpdate.BVCentreID = bvguruPayload.bvCentreID
            bvguruUpdate.GuruName = bvguruPayload.guruName
            bvguruUpdate.DateOfBirth = bvguruPayload.dateOfBirth
            bvguruUpdate.AddressLine1 = bvguruPayload.addressLine1
            bvguruUpdate.AddressLine2 = bvguruPayload.addressLine2
            bvguruUpdate.AddressLine3 = bvguruPayload.addressLine3
            bvguruUpdate.PIN = bvguruPayload.pinCode
            bvguruUpdate.ContactNo1 = bvguruPayload.contactNo1
            bvguruUpdate.ContactNo2 = bvguruPayload.contactNo2
            bvguruUpdate.Email = bvguruPayload.eMail
            bvguruUpdate.Gender = bvguruPayload.gender
            bvguruUpdate.HighestEduDegreeID = bvguruPayload.highestEduDegreeID
            bvguruUpdate.GraduationMajorSubjectID = bvguruPayload.gradMajorSubID
            bvguruUpdate.OccupationID = bvguruPayload.occupationID
            bvguruUpdate.AlumnusOf = bvguruPayload.alumnusOf
            bvguruUpdate.Photo = bvguruPayload.photo
            bvguruUpdate.TargetGroupsOfStudents = bvguruPayload.targetGroups
            bvguruUpdate.UpdatedBy = bvguruPayload.updatedBy
            session.commit()
            return {"message":f"Bal Vikas Guru with ID {id} updated"}
        return {"error": f"Bal Vikas Guru with ID {id} not found"}
    
@router.delete("/bvgurus/delete/{id}")
def delete_bvguru(id: int):
    with SessionLocal() as session:
        bvguruModel = BalVikasGuru
        bvGuruToDelete = session.query(bvguruModel).filter(bvguruModel.ID == id).first()
        if bvGuruToDelete:
            session.delete(bvGuruToDelete)
            session.commit()
            return {"message":f"Bal Vikas Guru with ID {id} deleted"}
        return {"error": f"Bal Vikas Guru with ID {id} not found"}