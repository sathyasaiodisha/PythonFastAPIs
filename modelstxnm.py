from typing import Optional
import datetime

from sqlalchemy import DateTime, Index, Integer, PrimaryKeyConstraint, Unicode, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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
