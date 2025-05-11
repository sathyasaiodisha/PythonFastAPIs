from typing import List, Optional

from sqlalchemy import Boolean, DateTime, ForeignKeyConstraint, Index, Integer, NCHAR, PrimaryKeyConstraint, Unicode, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass


class ActivityFrequency(Base):
    __tablename__ = 'ActivityFrequency'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Activity__3214EC27D2D97DE7'),
        Index('UQ__Activity__5D369D8ABD482AA4', 'FrequencyType', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    FrequencyType: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Activities: Mapped[List['Activities']] = relationship('Activities', back_populates='ActivityFrequency_')


class ActivityTypes(Base):
    __tablename__ = 'ActivityTypes'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Activity__3214EC2723EE4DDD'),
        Index('UQ__Activity__368E0EA437D64E4A', 'ActivityType', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    ActivityType: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Activities: Mapped[List['Activities']] = relationship('Activities', back_populates='ActivityTypes_')


class BhajanMandali(Base):
    __tablename__ = 'BhajanMandali'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BhajanMa__3214EC27E0C16AF8'),
        Index('UQ__BhajanMa__487507FE5206F3E7', 'BhajanMandaliRegNo', unique=True),
        Index('UQ__BhajanMa__8FFD5B4F69BB15B5', 'BhajanMandaliCode', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    BhajanMandaliCode: Mapped[str] = mapped_column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'))
    BhajanMandaliRegNo: Mapped[str] = mapped_column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'))
    BhajanMandaliName: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))


class District(Base):
    __tablename__ = 'District'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__District__3214EC2791343832'),
        Index('UQ__District__3D4E86ABC744D4B8', 'DistrictCode', unique=True),
        Index('UQ__District__F4708CA447C7E3A7', 'DistrictName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DistrictName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DistrictCode: Mapped[str] = mapped_column(Unicode(4, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))

    DistrictOfficeBearer: Mapped[List['DistrictOfficeBearer']] = relationship('DistrictOfficeBearer', back_populates='District_')
    Events: Mapped[List['Events']] = relationship('Events', back_populates='District_')


class OrgHierarchyCodes(Base):
    __tablename__ = 'OrgHierarchyCodes'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__OrgHiera__3214EC27D135001A'),
        Index('UQ__OrgHiera__956BACEC11471149', 'OrgLevelCode', unique=True),
        Index('UQ__OrgHiera__D577FD35547D7113', 'OrgLevel', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    OrgLevel: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    OrgLevelCode: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Designation: Mapped[List['Designation']] = relationship('Designation', back_populates='OrgHierarchyCodes_')
    Activities: Mapped[List['Activities']] = relationship('Activities', back_populates='OrgHierarchyCodes_')
    Events: Mapped[List['Events']] = relationship('Events', back_populates='OrgHierarchyCodes_')


class Samithi(Base):
    __tablename__ = 'Samithi'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Samithi__3214EC27E1DD108C'),
        Index('UQ__Samithi__22399A93479C93F3', 'SamithiCode', unique=True),
        Index('UQ__Samithi__C6B568EE1F1E71A5', 'SamithiRegNo', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    SamithiCode: Mapped[str] = mapped_column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'))
    SamithiRegNo: Mapped[str] = mapped_column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'))
    SamithiName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    DistrictID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    SamithiOfficeBearer: Mapped[List['SamithiOfficeBearer']] = relationship('SamithiOfficeBearer', back_populates='Samithi_')
    Events: Mapped[List['Events']] = relationship('Events', back_populates='Samithi_')


class Wings(Base):
    __tablename__ = 'Wings'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Wings__3214EC27045BBEC4'),
        Index('UQ__Wings__02C058512FD900E5', 'WingName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    WingName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Programmes: Mapped[List['Programmes']] = relationship('Programmes', back_populates='Wings_')


class Designation(Base):
    __tablename__ = 'Designation'
    __table_args__ = (
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Designati__OrgLe__208CD6FA'),
        PrimaryKeyConstraint('ID', name='PK__Designat__3214EC27095C5145'),
        Index('UQ_DesignationCode', 'DesignationCode', unique=True),
        Index('UQ_DesignationName', 'DesignationName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationName: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DesignationCode: Mapped[str] = mapped_column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    HierarchyOrder: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    OrgLevelID: Mapped[Optional[int]] = mapped_column(Integer)

    OrgHierarchyCodes_: Mapped[Optional['OrgHierarchyCodes']] = relationship('OrgHierarchyCodes', back_populates='Designation')
    DistrictOfficeBearer: Mapped[List['DistrictOfficeBearer']] = relationship('DistrictOfficeBearer', back_populates='Designation_')
    SamithiOfficeBearer: Mapped[List['SamithiOfficeBearer']] = relationship('SamithiOfficeBearer', back_populates='Designation_')
    StateOfficeBearer: Mapped[List['StateOfficeBearer']] = relationship('StateOfficeBearer', back_populates='Designation_')


class Programmes(Base):
    __tablename__ = 'Programmes'
    __table_args__ = (
        ForeignKeyConstraint(['WingID'], ['txnm.Wings.ID'], name='FK__Programme__WingI__2180FB33'),
        PrimaryKeyConstraint('ID', name='PK__Programm__3214EC27A8A51453'),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    WingID: Mapped[Optional[int]] = mapped_column(Integer)
    ProgrammeName: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Wings_: Mapped[Optional['Wings']] = relationship('Wings', back_populates='Programmes')
    Activities: Mapped[List['Activities']] = relationship('Activities', back_populates='Programmes_')
    Events: Mapped[List['Events']] = relationship('Events', back_populates='Programmes_')


class Activities(Base):
    __tablename__ = 'Activities'
    __table_args__ = (
        ForeignKeyConstraint(['ActivityFrequencyID'], ['txnm.ActivityFrequency.ID'], name='FK__Activitie__Activ__1DB06A4F'),
        ForeignKeyConstraint(['ActivityTypeID'], ['txnm.ActivityTypes.ID'], name='FK__Activitie__Activ__1CBC4616'),
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Activitie__OrgLe__1EA48E88'),
        ForeignKeyConstraint(['ProgrammeID'], ['txnm.Programmes.ID'], name='FK__Activitie__Progr__1F98B2C1'),
        PrimaryKeyConstraint('ID', name='PK__Activiti__3214EC27BFECD90B'),
        Index('UQ__Activiti__685755E789B693BD', 'Activity', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    Activity: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    ActivityTypeID: Mapped[Optional[int]] = mapped_column(Integer)
    ActivityFrequencyID: Mapped[Optional[int]] = mapped_column(Integer)
    OrgLevelID: Mapped[Optional[int]] = mapped_column(Integer)
    ProgrammeID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    ActivityFrequency_: Mapped[Optional['ActivityFrequency']] = relationship('ActivityFrequency', back_populates='Activities')
    ActivityTypes_: Mapped[Optional['ActivityTypes']] = relationship('ActivityTypes', back_populates='Activities')
    OrgHierarchyCodes_: Mapped[Optional['OrgHierarchyCodes']] = relationship('OrgHierarchyCodes', back_populates='Activities')
    Programmes_: Mapped[Optional['Programmes']] = relationship('Programmes', back_populates='Activities')


class DistrictOfficeBearer(Base):
    __tablename__ = 'DistrictOfficeBearer'
    __table_args__ = (
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__DistrictO__Desig__17F790F9'),
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__DistrictO__Distr__18EBB532'),
        PrimaryKeyConstraint('ID', name='PK__District__3214EC2709AE26F7'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    DistrictID: Mapped[Optional[int]] = mapped_column(Integer)
    DesignationID: Mapped[Optional[int]] = mapped_column(Integer)
    OfficeBearerName: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine1: Mapped[Optional[str]] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine3: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo1: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo2: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    Email: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Gender: Mapped[Optional[str]] = mapped_column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Designation_: Mapped[Optional['Designation']] = relationship('Designation', back_populates='DistrictOfficeBearer')
    District_: Mapped[Optional['District']] = relationship('District', back_populates='DistrictOfficeBearer')


class SamithiOfficeBearer(Base):
    __tablename__ = 'SamithiOfficeBearer'
    __table_args__ = (
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__SamithiOf__Desig__19DFD96B'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__SamithiOf__Samit__1AD3FDA4'),
        PrimaryKeyConstraint('ID', name='PK__SamithiO__3214EC27AC0BFC99'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationID: Mapped[int] = mapped_column(Integer)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    OfficeBearerName: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine1: Mapped[Optional[str]] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine3: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo1: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo2: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    Email: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Gender: Mapped[Optional[str]] = mapped_column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Designation_: Mapped['Designation'] = relationship('Designation', back_populates='SamithiOfficeBearer')
    Samithi_: Mapped[Optional['Samithi']] = relationship('Samithi', back_populates='SamithiOfficeBearer')


class StateOfficeBearer(Base):
    __tablename__ = 'StateOfficeBearer'
    __table_args__ = (
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__StateOffi__Desig__1BC821DD'),
        PrimaryKeyConstraint('ID', name='PK__StateOff__3214EC275FE18D80'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationID: Mapped[int] = mapped_column(Integer)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    OfficeBearerName: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine1: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine3: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo1: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo2: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    Email: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Gender: Mapped[Optional[str]] = mapped_column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Designation_: Mapped['Designation'] = relationship('Designation', back_populates='StateOfficeBearer')


class Events(Base):
    __tablename__ = 'Events'
    __table_args__ = (
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__Events__District__1332DBDC'),
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Events__OrgLevel__14270015'),
        ForeignKeyConstraint(['ProgrammeID'], ['txnm.Programmes.ID'], name='FK__Events__Programm__151B244E'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__Events__SamithiI__160F4887'),
        PrimaryKeyConstraint('ID', name='PK__Events__3214EC27CA8CDB70'),
        {'schema': 'ops'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    ProgrammeID: Mapped[int] = mapped_column(Integer)
    OrgLevelID: Mapped[int] = mapped_column(Integer)
    EventTitle: Mapped[str] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    EventDate: Mapped[datetime.datetime] = mapped_column(DateTime)
    ToBeFeatured: Mapped[bool] = mapped_column(Boolean, server_default=text('((1))'))
    IsActive: Mapped[bool] = mapped_column(Boolean, server_default=text('((1))'))
    IsDeleted: Mapped[bool] = mapped_column(Boolean, server_default=text('((0))'))
    IsApproved: Mapped[bool] = mapped_column(Boolean, server_default=text('((0))'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    DistrictID: Mapped[Optional[int]] = mapped_column(Integer)
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    EventDescription: Mapped[Optional[str]] = mapped_column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    EventVenue: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    RejectionComments: Mapped[Optional[str]] = mapped_column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    District_: Mapped[Optional['District']] = relationship('District', back_populates='Events')
    OrgHierarchyCodes_: Mapped['OrgHierarchyCodes'] = relationship('OrgHierarchyCodes', back_populates='Events')
    Programmes_: Mapped['Programmes'] = relationship('Programmes', back_populates='Events')
    Samithi_: Mapped[Optional['Samithi']] = relationship('Samithi', back_populates='Events')
    EventsDigitalArchive: Mapped[List['EventsDigitalArchive']] = relationship('EventsDigitalArchive', back_populates='Events_')


class EventsDigitalArchive(Base):
    __tablename__ = 'EventsDigitalArchive'
    __table_args__ = (
        ForeignKeyConstraint(['EventID'], ['ops.Events.ID'], name='FK__EventsDig__Event__17036CC0'),
        PrimaryKeyConstraint('ID', name='PK__EventsDi__3214EC2752AB9788'),
        {'schema': 'ops'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    EventID: Mapped[int] = mapped_column(Integer)
    ActivityName: Mapped[str] = mapped_column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ToBeFeatured: Mapped[bool] = mapped_column(Boolean, server_default=text('((1))'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    ImagePath: Mapped[Optional[str]] = mapped_column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Events_: Mapped['Events'] = relationship('Events', back_populates='EventsDigitalArchive')