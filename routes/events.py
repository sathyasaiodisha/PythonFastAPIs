from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from models import Events
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.get("/recentevents")
def get_recentevents():
    with SessionLocal() as session:
        eventsModel = Events
        recentevents = session.query(eventsModel).filter(eventsModel.EventDate < datetime.now()).all()
        return recentevents
    
@router.get("/upcomngevents")
def get_upcomingevents():
    with SessionLocal() as session:
        eventsModel = Events
        upcomingevents = session.query(eventsModel).filter(eventsModel.EventDate > datetime.now()).all()
        return upcomingevents
    
@router.post("/events/add")
def add_event(programmeid:int, orglevelid: int, districtid: int, evttitle: str, evtvenue: str, evtdate: datetime, 
              samithiid: Optional[int]=None, evtdesc: Optional[str]=None,  tobefeatured: Optional[bool]=False, 
              isactive: Optional[bool]=True, isdeleted: Optional[bool]=False, isapproved: Optional[bool]=False,
              rejectioncomments: Optional[str]=None):
    with SessionLocal() as session:
        eventsModel = Events
        maxEventId = session.query(func.max(eventsModel.ID)).scalar()
        
        new_event = eventsModel(ID = (maxEventId + 1), ProgrammeID = programmeid, OrgLevelID = orglevelid, 
                                  DistrictID = districtid,
                                  SamithiID = samithiid if samithiid is not None else None,
                                  EventTitle = evttitle,
                                  EventDescription = evtdesc if evtdesc is not None else None,
                                  EventVenue = evtvenue,
                                  ToBeFeatured = tobefeatured if tobefeatured is not None else None,
                                  IsActive = isactive if isactive is not None else None,
                                  IsDeleted = isdeleted if isdeleted is not None else None,
                                  IsApproved = isapproved if isapproved is not None else None,
                                  RejectionComments = rejectioncomments if rejectioncomments is not None else None,
                                  CreatedBy = "Portal")
        session.add(new_event)
        session.commit()
        session.refresh(new_event)
        return {"message":"Event created", "event_id":str(maxEventId + 1)}
    
@router.put("/events/update/{id}")
def update_event(id: int, programmeid:int, orglevelid: int, districtid: int, evttitle: str, evtvenue: str, evtdate: datetime, 
              samithiid: Optional[int]=None, evtdesc: Optional[str]=None,  tobefeatured: Optional[bool]=False, 
              isactive: Optional[bool]=True, isdeleted: Optional[bool]=False, isapproved: Optional[bool]=False,
              rejectioncomments: Optional[str]=None):
    with SessionLocal() as session:
        eventModel = Events
        eventToUpdate = session.query(eventModel).filter(eventModel.ID == id).first()
        if eventToUpdate:
            eventToUpdate.ProgrammeID = programmeid
            eventToUpdate.OrgLevelID = orglevelid
            eventToUpdate.DistrictID = districtid
            eventToUpdate.EventTitle = evttitle
            eventToUpdate.EventVenue = evtvenue
            eventToUpdate.EventDate = evtdate
            eventToUpdate.SamithiID = samithiid if samithiid is not None else None
            eventToUpdate.EventDescription = evtdesc if evtdesc is not None else None
            eventToUpdate.ToBeFeatured = tobefeatured if tobefeatured is not None else None
            eventToUpdate.IsActive = isactive if isactive is not None else None
            eventToUpdate.IsDeleted = isdeleted if isdeleted is not None else None
            eventToUpdate.IsApproved = isapproved if isapproved is not None else None
            eventToUpdate.RejectionComments = rejectioncomments if rejectioncomments is not None else None
            
            session.commit()
            return {"message":f"Event with ID {id} updated"}
        return {"error": f"Event with ID {id} not found"}
    
@router.delete("/events/delete/{id}")
def delete_samithi(id: int):
    with SessionLocal() as session:
        eventModel = Events
        eventToDelete = session.query(eventModel).filter(eventModel.ID == id).first()
        if eventToDelete:
            eventToDelete.IsDeleted = True
            session.commit()
            return {"message":f"Event with ID {id} deleted"}
        return {"error": f"Event with ID {id} not found"}