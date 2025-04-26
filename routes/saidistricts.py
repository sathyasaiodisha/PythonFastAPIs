from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import District

router = APIRouter()

@router.get("/saidistricts")
def get_saidistricts():
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistricts = session.query(saidistrictsModel).all()
        return saidistricts
    
@router.post("/saidistricts/add")
def create_saidistrict(distcode: str, distname: str):
    with SessionLocal() as session:
        saidistrictsModel = District
        maxIdLessThan50 = session.query(saidistrictsModel.ID).filter(saidistrictsModel.ID < 50).order_by(desc(saidistrictsModel.ID)).limit(1).scalar();
        new_saidistrict = saidistrictsModel(ID = (maxIdLessThan50 + 1), DistrictCode = distcode, DistrictName = distname, CreatedBy = "Portal")
        session.add(new_saidistrict)
        session.commit()
        session.refresh(new_saidistrict)
        return {"message":"Sai district created", "saidistrict_id":new_saidistrict.ID}
    
@router.put("/saidistricts/update/{id}")
def update_saidistrict(id: int, distcode: str, distname: str):
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistrictToUpdate = session.query(saidistrictsModel).filter(saidistrictsModel.ID == id).first()
        if saidistrictToUpdate:
            saidistrictToUpdate.DistrictCode = distcode
            saidistrictToUpdate.DistrictName = distname
            session.commit()
            return {"message":f"Sai district with ID {id} updated"}
        return {"error": f"Sai district with ID {id} not found"}
    
@router.delete("/saidistricts/delete/{id}")
def delete_saidistrict(id: int):
    with SessionLocal() as session:
        saidistrictsModel = District
        saidistrictToDelete = session.query(saidistrictsModel).filter(saidistrictsModel.ID == id).first()
        if saidistrictToDelete:
            session.delete(saidistrictToDelete)
            session.commit()
            return {"message":f"Sai district with ID {id} deleted"}
        return {"error": f"Sai district with ID {id} not found"}