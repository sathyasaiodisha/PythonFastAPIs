from typing import Optional
import datetime

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, Table, Unicode, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class AdminJurisdiction(Base):
    __tablename__ = 'AdminJurisdiction'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__AdminJur__3214EC273A669ABD'),
        Index('UQ__AdminJur__56910AC473D3E017', 'Jurisdiction', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Jurisdiction: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('(getdate())'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))


class District(Base):
    __tablename__ = 'District'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='PK__District__3214EC2799102F75'),
        Index('UQ__District__3D4E86AB701512B1', 'DistrictCode', unique=True),
        Index('UQ__District__F4708CA4BD585DC4', 'DistrictName', unique=True),
        {'schema': 'txnm'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    DistrictName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DistrictCode: Mapped[str] = mapped_column(Unicode(4, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))
    UpdatedBy: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))

    AdminUser: Mapped[list['AdminUser']] = relationship('AdminUser', back_populates='District_')


class AdminUser(Base):
    __tablename__ = 'AdminUser'
    __table_args__ = (
        ForeignKeyConstraint(['DistrictID'], ['txnm.District.ID'], name='FK__AdminUser__Distr__14E61A24'),
        PrimaryKeyConstraint('ID', name='PK__AdminUse__3214EC27CFC273AC'),
        Index('UQ__AdminUse__08638DF82A91CEB9', 'UserEmail', unique=True),
        Index('UQ__AdminUse__C9F2845618A91E64', 'UserName', unique=True),
        {'schema': 'org'}
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserName: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    UserEmail: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Password: Mapped[str] = mapped_column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
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
