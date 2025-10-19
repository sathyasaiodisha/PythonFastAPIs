import logging

from database import SessionLocal
from fastapi import APIRouter, HTTPException
from models import Designation
from pydantic import BaseModel

class DesignationToCreate(BaseModel):
    designationName: str
    designationCode: str
    hierarchyOrder: str
    orgLevelID: str
    gentsAndLadies: bool
    createdBy: str

class DesignationToUpdate(BaseModel):
    designationName: str
    designationCode: str
    hierarchyOrder: int
    updatedBy: str

router = APIRouter()

@router.get("/designations")
def get_designations():
    with SessionLocal() as session:
        designationModel = Designation
        designations = session.query(designationModel).all()
        return designations


@router.post("/designations/add")
def create_designation(payload: DesignationToCreate):
    with SessionLocal() as session:
        logging.info("Payload recieved:")
        last_id = session.query(Designation.ID).order_by(Designation.ID.desc()).first()
        next_id = (last_id[0] + 1) if last_id else 1
        rows_to_insert = []
        if payload.gentsAndLadies:
            rows_to_insert.append(
                Designation(
                    ID=next_id,
                    DesignationName=f"{payload.designationName} (Gents)",
                    DesignationCode=f"{payload.designationCode}G",
                    OrgLevelID=payload.orgLevelID,
                    HierarchyOrder=payload.hierarchyOrder,
                    CreatedBy=payload.createdBy
                ))

            rows_to_insert.append(
                Designation(
                ID=next_id + 1,
                DesignationName= f"{payload.designationName} (Ladies)",
                DesignationCode= f"{payload.designationCode}L",
                OrgLevelID=payload.orgLevelID,
                HierarchyOrder=payload.hierarchyOrder,
                CreatedBy=payload.createdBy
            )
            )

        else:
            rows_to_insert.append(
                Designation(
                    ID=next_id,
                    DesignationName=payload.designationName,
                    DesignationCode=payload.designationCode,
                    OrgLevelID=payload.orgLevelID,
                    HierarchyOrder=payload.hierarchyOrder,
                    CreatedBy=payload.createdBy
                )
            )

        try:
            for row in rows_to_insert:
                session.add(row)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"DB Error: {e}")

        return {
            "message": "Designation created successfully"
        }

@router.put("/designations/update/{id}")
def update_designation(id: int, designationPayload: DesignationToUpdate):
    with SessionLocal() as session:
        designationModel = Designation
        designationUpdate = session.query(designationModel).filter(designationModel.ID == id).first()
        if designationUpdate:
            designationUpdate.DesignationName = designationPayload.designationName
            designationUpdate.DesignationCode = designationPayload.designationCode
            designationUpdate.HierarchyOrder = designationPayload.hierarchyOrder
            designationUpdate.UpdatedBy = designationPayload.updatedBy
            try:
                session.commit()
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"DB Error: {e}")
            return {"message": f"Designation updated successfully"}
        return {"message": f"Designation update failed"}

@router.delete("/designations/delete/{id}")
def delete_designation(id: int):
    with SessionLocal() as session:
        designationModel = Designation
        designationToDelete = session.query(designationModel).filter(designationModel.ID == id).first()
        if designationToDelete:
            session.delete(designationToDelete)
            session.commit()
            return {"message": f"Designation with ID {id} deleted"}
        return {"error": f"Designation with ID {id} not found"}

