from typing import Optional
import datetime

from sqlalchemy import Boolean, DateTime, ForeignKeyConstraint, Index, Integer, NCHAR, PrimaryKeyConstraint, Unicode, text, Table, Column

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class ActivityFrequency(Base):
    __tablename__ = 'ActivityFrequency'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Activity__3214EC27BF6C61D9'),
        Index('UQ__Activity__5D369D8AA934920D', 'FrequencyType', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    FrequencyType: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Activities: Mapped[list['Activities']] = relationship('Activities', back_populates='ActivityFrequency_')


class ActivityTypes(Base):
    __tablename__ = 'ActivityTypes'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Activity__3214EC27F25347B3'),
        Index('UQ__Activity__368E0EA4E1DE8A95', 'ActivityType', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    ActivityType: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Activities: Mapped[list['Activities']] = relationship('Activities', back_populates='ActivityTypes_')


class BVClassPlaceCategory(Base):
    __tablename__ = 'BVClassPlaceCategory'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BVClassP__3214EC2727DD9CCD'),
        Index('UQ__BVClassP__E587B8BBF8B950E5', 'PlaceCategoryName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    PlaceCategoryName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BalVikasCentre: Mapped[list['BalVikasCentre']] = relationship('BalVikasCentre', back_populates='BVClassPlaceCategory_')


class BVGuruGradMajorSubject(Base):
    __tablename__ = 'BVGuruGradMajorSubject'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BVGuruGr__3214EC27C42D0FE4'),
        Index('UQ__BVGuruGr__F532B400019F1EC3', 'GraduationMajorSubject', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    GraduationMajorSubject: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='BVGuruGradMajorSubject_')

class BVGuruOccupation(Base):
    __tablename__ = 'BVGuruOccupation'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BVGuruOc__3214EC278DEBC77C'),
        Index('UQ__BVGuruOc__18376EA0D01C8263', 'OccupationName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    OccupationName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='BVGuruOccupation_')

class BVGuruQualification(Base):
    __tablename__ = 'BVGuruQualification'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BVGuruQu__3214EC27306D8BAF'),
        Index('UQ__BVGuruQu__49C0FCDB758F9534', 'QualificationName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    QualificationName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='BVGuruQualification_')

class BalVikasSubjects(Base):
    __tablename__ = 'BalVikasSubjects'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BalVikas__3214EC27D3791E76'),
        Index('UQ__BalVikas__4C5A7D55F4A4D1D5', 'SubjectName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    SubjectName: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))


class BhajanMandali(Base):
    __tablename__ = 'BhajanMandali'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__BhajanMa__3214EC2716AC76DB'),
        Index('UQ__BhajanMa__487507FEE4928FD3', 'BhajanMandaliRegNo', unique=True),
        Index('UQ__BhajanMa__8FFD5B4F42F5679C', 'BhajanMandaliCode', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    BhajanMandaliCode: Mapped[str] = mapped_column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BhajanMandaliRegNo: Mapped[str] = mapped_column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BhajanMandaliName: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BalVikasCentre: Mapped[list['BalVikasCentre']] = relationship('BalVikasCentre', back_populates='BhajanMandali_')
    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='BhajanMandali_')

class District(Base):
    __tablename__ = 'District'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__District__3214EC2799102F75'),
        Index('UQ__District__3D4E86AB701512B1', 'DistrictCode', unique=True),
        Index('UQ__District__F4708CA4BD585DC4', 'DistrictName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DistrictName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DistrictCode: Mapped[str] = mapped_column(Unicode(4, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))

    Events: Mapped[list['Events']] = relationship('Events', back_populates='District_')
    BalVikasCentre: Mapped[list['BalVikasCentre']] = relationship('BalVikasCentre', back_populates='District_')
    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='District_')
    DistrictOfficeBearer: Mapped[list['DistrictOfficeBearer']] = relationship('DistrictOfficeBearer', back_populates='District_')
    AdminUser: Mapped[list['AdminUser']] = relationship('AdminUser', back_populates='District_')


class GuruSkillset(Base):
    __tablename__ = 'GuruSkillset'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__GuruSkil__3214EC2772195D71'),
        Index('UQ__GuruSkil__B63C6571814A58A6', 'SkillName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    SkillName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))


class OrgHierarchyCodes(Base):
    __tablename__ = 'OrgHierarchyCodes'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__OrgHiera__3214EC27B3386F80'),
        Index('UQ__OrgHiera__956BACECAF7C156C', 'OrgLevelCode', unique=True),
        Index('UQ__OrgHiera__D577FD356A3F749E', 'OrgLevel', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    OrgLevel: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    OrgLevelCode: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Designation: Mapped[list['Designation']] = relationship('Designation', back_populates='OrgHierarchyCodes_')
    Activities: Mapped[list['Activities']] = relationship('Activities', back_populates='OrgHierarchyCodes_')
    Designation: Mapped[list['Designation']] = relationship('Designation', back_populates='OrgHierarchyCodes_')
    Events: Mapped[list['Events']] = relationship('Events', back_populates='OrgHierarchyCodes_')


class Samithi(Base):
    __tablename__ = 'Samithi'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Samithi__3214EC27619DF389'),
        Index('UQ__Samithi__22399A93ED0E1047', 'SamithiCode', unique=True),
        Index('UQ__Samithi__C6B568EEE4221E26', 'SamithiRegNo', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    SamithiCode: Mapped[str] = mapped_column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SamithiRegNo: Mapped[str] = mapped_column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SamithiName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    DistrictID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BalVikasCentre: Mapped[list['BalVikasCentre']] = relationship('BalVikasCentre', back_populates='Samithi_')
    Events: Mapped[list['Events']] = relationship('Events', back_populates='Samithi_')
    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='Samithi_')
    SamithiOfficeBearer: Mapped[list['SamithiOfficeBearer']] = relationship('SamithiOfficeBearer', back_populates='Samithi_')


class Wings(Base):
    __tablename__ = 'Wings'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__Wings__3214EC27901BAE29'),
        Index('UQ__Wings__02C058510B79DF73', 'WingName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    WingName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Programmes: Mapped[list['Programmes']] = relationship('Programmes', back_populates='Wings_')

class AdminJurisdiction(Base):
    __tablename__ = 'AdminJurisdiction'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__AdminJur__3214EC273A669ABD'),
        Index('UQ__AdminJur__56910AC473D3E017', 'Jurisdiction', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    Jurisdiction: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

class BalVikasCentre(Base):
    __tablename__ = 'BalVikasCentre'
    __table_args__ = (
        ForeignKeyConstraint(['BVClassPlaceCategoryID'], ['txnm.BVClassPlaceCategory.ID'], name='FK__BalVikasC__BVCla__489AC854'),
        ForeignKeyConstraint(['BhajanMandaliID'], ['txnm.BhajanMandali.ID'], name='FK__BalVikasC__Bhaja__47A6A41B'),
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__BalVikasC__Distr__498EEC8D'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__BalVikasC__Samit__4A8310C6'),
        PrimaryKeyConstraint('ID', name='PK__BalVikas__3214EC2772E75916'),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DistrictID: Mapped[int] = mapped_column(Integer, nullable=False)
    BalVikasCentreCode: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BalVikasCentreName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PlaceOfBalVikasClass: Mapped[str] = mapped_column(Unicode(300, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BVClassPlaceCategoryID: Mapped[int] = mapped_column(Integer, nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    BhajanMandaliID: Mapped[Optional[int]] = mapped_column(Integer)
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    NoOfGroup1Students: Mapped[Optional[int]] = mapped_column(Integer)
    NoOfGroup2Students: Mapped[Optional[int]] = mapped_column(Integer)
    NoOfGroup3Students: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BVClassPlaceCategory_: Mapped['BVClassPlaceCategory'] = relationship('BVClassPlaceCategory', back_populates='BalVikasCentre')
    BhajanMandali_: Mapped[Optional['BhajanMandali']] = relationship('BhajanMandali', back_populates='BalVikasCentre')
    District_: Mapped['District'] = relationship('District', back_populates='BalVikasCentre')
    Samithi_: Mapped[Optional['Samithi']] = relationship('Samithi', back_populates='BalVikasCentre')
    BalVikasGuru: Mapped[list['BalVikasGuru']] = relationship('BalVikasGuru', back_populates='BalVikasCentre_')


class Designation(Base):
    __tablename__ = 'Designation'
    __table_args__ = (
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Designati__OrgLe__4B7734FF'),
        PrimaryKeyConstraint('ID', name='PK__Designat__3214EC2774567CBC'),
        Index('UQ_DesignationCode', 'DesignationCode', unique=True),
        Index('UQ_DesignationName', 'DesignationName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationName: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DesignationCode: Mapped[str] = mapped_column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    HierarchyOrder: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    OrgLevelID: Mapped[Optional[int]] = mapped_column(Integer)

    OrgHierarchyCodes_: Mapped[Optional['OrgHierarchyCodes']] = relationship('OrgHierarchyCodes', back_populates='Designation')
    DistrictOfficeBearer: Mapped[list['DistrictOfficeBearer']] = relationship('DistrictOfficeBearer', back_populates='Designation_')
    SamithiOfficeBearer: Mapped[list['SamithiOfficeBearer']] = relationship('SamithiOfficeBearer', back_populates='Designation_')
    StateOfficeBearer: Mapped[list['StateOfficeBearer']] = relationship('StateOfficeBearer', back_populates='Designation_')

class Programmes(Base):
    __tablename__ = 'Programmes'
    __table_args__ = (
        ForeignKeyConstraint(['WingID'], ['txnm.Wings.ID'], name='FK__Programme__WingI__4C6B5938'),
        PrimaryKeyConstraint('ID', name='PK__Programm__3214EC27EB701D99'),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    WingID: Mapped[Optional[int]] = mapped_column(Integer)
    ProgrammeName: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Wings_: Mapped[Optional['Wings']] = relationship('Wings', back_populates='Programmes')
    Events: Mapped[list['Events']] = relationship('Events', back_populates='Programmes_')
    Activities: Mapped[list['Activities']] = relationship('Activities', back_populates='Programmes_')


class Activities(Base):
    __tablename__ = 'Activities'
    __table_args__ = (
        ForeignKeyConstraint(['ActivityFrequencyID'], ['txnm.ActivityFrequency.ID'], name='FK__Activitie__Activ__44CA3770'),
        ForeignKeyConstraint(['ActivityTypeID'], ['txnm.ActivityTypes.ID'], name='FK__Activitie__Activ__43D61337'),
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Activitie__OrgLe__45BE5BA9'),
        ForeignKeyConstraint(['ProgrammeID'], ['txnm.Programmes.ID'], name='FK__Activitie__Progr__46B27FE2'),
        PrimaryKeyConstraint('ID', name='PK__Activiti__3214EC27383CF012'),
        Index('UQ__Activiti__685755E7C536B026', 'Activity', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    Activity: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
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

class Events(Base):
    __tablename__ = 'Events'
    __table_args__ = (
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__Events__District__339FAB6E'),
        ForeignKeyConstraint(['OrgLevelID'], ['txnm.OrgHierarchyCodes.ID'], name='FK__Events__OrgLevel__3493CFA7'),
        ForeignKeyConstraint(['ProgrammeID'], ['txnm.Programmes.ID'], name='FK__Events__Programm__3587F3E0'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__Events__SamithiI__367C1819'),
        PrimaryKeyConstraint('ID', name='PK__Events__3214EC27EA3ACB53'),
        {'schema': 'ops'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    ProgrammeID: Mapped[int] = mapped_column(Integer, nullable=False)
    OrgLevelID: Mapped[int] = mapped_column(Integer, nullable=False)
    EventTitle: Mapped[str] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    EventDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    ToBeFeatured: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('((1))'))
    IsActive: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('((1))'))
    IsDeleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('((0))'))
    IsApproved: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('((0))'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
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
    EventsDigitalArchive: Mapped[list['EventsDigitalArchive']] = relationship('EventsDigitalArchive', back_populates='Events_')


class EventsDigitalArchive(Base):
    __tablename__ = 'EventsDigitalArchive'
    __table_args__ = (
        ForeignKeyConstraint(['EventID'], ['ops.Events.ID'], name='FK__EventsDig__Event__37703C52'),
        PrimaryKeyConstraint('ID', name='PK__EventsDi__3214EC278E9BC569'),
        {'schema': 'ops'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    EventID: Mapped[int] = mapped_column(Integer, nullable=False)
    ActivityName: Mapped[str] = mapped_column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ToBeFeatured: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('((1))'))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    ImagePath: Mapped[Optional[str]] = mapped_column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    Events_: Mapped['Events'] = relationship('Events', back_populates='EventsDigitalArchive')

class BalVikasGuru(Base):
    __tablename__ = 'BalVikasGuru'
    __table_args__ = (
        ForeignKeyConstraint(['BVCentreID'], ['txnm.BalVikasCentre.ID'], name='FK__BalVikasG__BVCen__395884C4'),
        ForeignKeyConstraint(['BhajanMandaliID'], ['txnm.BhajanMandali.ID'], name='FK__BalVikasG__Bhaja__3864608B'),
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__BalVikasG__Distr__3A4CA8FD'),
        ForeignKeyConstraint(['GraduationMajorSubjectID'], ['txnm.BVGuruGradMajorSubject.ID'], name='FK__BalVikasG__Gradu__3B40CD36'),
        ForeignKeyConstraint(['HighestEduDegreeID'], ['txnm.BVGuruQualification.ID'], name='FK__BalVikasG__Highe__3C34F16F'),
        ForeignKeyConstraint(['OccupationID'], ['txnm.BVGuruOccupation.ID'], name='FK__BalVikasG__Occup__3D2915A8'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__BalVikasG__Samit__3E1D39E1'),
        PrimaryKeyConstraint('ID', name='PK__BalVikas__3214EC27BC1B9A0B'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DistrictID: Mapped[int] = mapped_column(Integer, nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    SamithiID: Mapped[Optional[int]] = mapped_column(Integer)
    BhajanMandaliID: Mapped[Optional[int]] = mapped_column(Integer)
    BVCentreID: Mapped[Optional[int]] = mapped_column(Integer)
    GuruName: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DateOfBirth: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    AddressLine1: Mapped[Optional[str]] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine3: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    PIN: Mapped[Optional[str]] = mapped_column(Unicode(6, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo1: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactNo2: Mapped[Optional[str]] = mapped_column(Unicode(15, 'SQL_Latin1_General_CP1_CI_AS'))
    Email: Mapped[Optional[str]] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Gender: Mapped[Optional[str]] = mapped_column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    HighestEduDegreeID: Mapped[Optional[int]] = mapped_column(Integer)
    GraduationMajorSubjectID: Mapped[Optional[int]] = mapped_column(Integer)
    OccupationID: Mapped[Optional[int]] = mapped_column(Integer)
    AlumnusOf: Mapped[Optional[str]] = mapped_column(Unicode(30, 'SQL_Latin1_General_CP1_CI_AS'))
    Photo: Mapped[Optional[str]] = mapped_column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    TargetGroupsOfStudents: Mapped[Optional[str]] = mapped_column(Unicode(30, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    BalVikasCentre_: Mapped[Optional['BalVikasCentre']] = relationship('BalVikasCentre', back_populates='BalVikasGuru')
    BhajanMandali_: Mapped[Optional['BhajanMandali']] = relationship('BhajanMandali', back_populates='BalVikasGuru')
    District_: Mapped['District'] = relationship('District', back_populates='BalVikasGuru')
    BVGuruGradMajorSubject_: Mapped[Optional['BVGuruGradMajorSubject']] = relationship('BVGuruGradMajorSubject', back_populates='BalVikasGuru')
    BVGuruQualification_: Mapped[Optional['BVGuruQualification']] = relationship('BVGuruQualification', back_populates='BalVikasGuru')
    BVGuruOccupation_: Mapped[Optional['BVGuruOccupation']] = relationship('BVGuruOccupation', back_populates='BalVikasGuru')
    Samithi_: Mapped[Optional['Samithi']] = relationship('Samithi', back_populates='BalVikasGuru')


class DistrictOfficeBearer(Base):
    __tablename__ = 'DistrictOfficeBearer'
    __table_args__ = (
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__DistrictO__Desig__3F115E1A'),
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__DistrictO__Distr__40058253'),
        PrimaryKeyConstraint('ID', name='PK__District__3214EC27B6049261'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
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
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__SamithiOf__Desig__40F9A68C'),
        ForeignKeyConstraint(['SamithiID'], ['txnm.Samithi.ID'], name='FK__SamithiOf__Samit__41EDCAC5'),
        PrimaryKeyConstraint('ID', name='PK__SamithiO__3214EC274F9A9CDE'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationID: Mapped[int] = mapped_column(Integer, nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
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
        ForeignKeyConstraint(['DesignationID'], ['txnm.Designation.ID'], name='FK__StateOffi__Desig__42E1EEFE'),
        PrimaryKeyConstraint('ID', name='PK__StateOff__3214EC279F27B264'),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    DesignationID: Mapped[int] = mapped_column(Integer, nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
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

class AdminUser(Base):
    __tablename__ = 'AdminUser'
    __table_args__ = (
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__AdminUser__Distr__14E61A24'),
        PrimaryKeyConstraint('ID', name='PK__AdminUse__3214EC27CFC273AC'),
        Index('UQ__AdminUse__08638DF82A91CEB9', 'UserEmail', unique=True),
        Index('UQ__AdminUse__C9F2845618A91E64', 'UserName', unique=True),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    UserName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    UserEmail: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Password: Mapped[str] = mapped_column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    DistrictID: Mapped[Optional[int]] = mapped_column(Integer)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    District_: Mapped[Optional['District']] = relationship('District', back_populates='AdminUser')

t_AdminUserJurisdiction = Table(
    'AdminUserJurisdiction', Base.metadata,
    Column('AdminUserID', Integer, nullable=False),
    Column('JurisdictionID', Integer, nullable=False),
    Column('CreatedBy', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CreatedDate', DateTime, nullable=False, server_default=text('(getdate())')),
    Column('UpdatedBy', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('UpdatedDate', DateTime, nullable=False, server_default=text('(getdate())')),
    ForeignKeyConstraint(['AdminUserID'], ['org.AdminUser.ID'], name='FK__AdminUser__Admin__24285DB4'),
    ForeignKeyConstraint(['JurisdictionID'], ['txnm.AdminJurisdiction.ID'], name='FK__AdminUser__Juris__2334397B'),
    schema='org'
)