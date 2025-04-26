from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import urllib
import urllib.parse

username = "ssswsodsa"
password = "Sr!s@thy@s@!"
servername = "103.133.214.224,1436"
dbname = "srisathyasaiod"
drivername = "ODBC Driver 17 for SQL Server"
#SQL Server Native Client 11.0"
#ODBC Driver 17 for SQL Server"

encodedPwd=urllib.parse.quote_plus(password)
encodedDriverName = urllib.parse.quote_plus(drivername)

# **MS SQL Server Connection String**
DATABASE_URL = f"mssql+pyodbc://{username}:{encodedPwd}@{servername}/{dbname}?driver={encodedDriverName}"

# **Create Engine & Session**
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# **Automatically Reflect the Database Tables**
Base = automap_base()
Base.prepare(engine, reflect=True, schema="org")  # This dynamically loads all tables from the database
Base.prepare(engine, reflect=True, schema="txnm")  # This dynamically loads all tables from the database
Base.prepare(engine, reflect=True, schema="ops")  # This dynamically loads all tables from the database