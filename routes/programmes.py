from database import SessionLocal
from fastapi import APIRouter
from models import Programmes

router = APIRouter()

@router.get("/programmes/all")
def get_allprogrammes():
    with SessionLocal() as session:
        programmeModel = Programmes
        programmes = session.query(programmeModel).all()
        return programmes
    
@router.get("/programmes/{wingid}")
def get_programmes(wingid:int):
    with SessionLocal() as session:
        programmeModel = Programmes
        programmes = session.query(programmeModel).filter(programmeModel.WingID==wingid).all()
        return programmes