from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import urllib
import urllib.parse
    
username = "sa"
password = "Admin@2025!"
servername = "172.93.223.88,1433"
dbname = "srisathyasaiod"
drivername = "ODBC Driver 17 for SQL Server"
#SQL Server Native Client 11.0"
#ODBC Driver 17 for SQL Server"

encodedPwd=urllib.parse.quote_plus(password)
encodedDriverName = urllib.parse.quote_plus(drivername)

print(encodedPwd)
print(encodedDriverName)

# **MS SQL Server Connection String**
DATABASE_URL = f"mssql+pyodbc://{username}:{encodedPwd}@{servername}/{dbname}?driver={encodedDriverName}"

print(DATABASE_URL)


# py -3 -m sqlacodegen "mssql+pyodbc://sa:Admin%402025%21@172.93.223.88,1433/srisathyasaiod?driver=ODBC+Driver+17+for+SQL+Server" --outfile models1.py

D:\Python\python.exe

[notice] To update, run: python.exe -m pip install --upgrade pip