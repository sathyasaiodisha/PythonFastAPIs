from database import SessionLocal
from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import BaseModel
import shutil
import os
import logging

router = APIRouter()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("fastapi_app")

@router.post("/uploadsaisandesh")
async def upload_saisandesh_photo(file: UploadFile = File(...)):
    try:
        upload_dir = "/var/www/PHOTOS/SaiSandesh"
        base_url = "http://172.93.223.88:8080/images/saisandesh"
        
        # Construct file path
        file_path = f"{upload_dir}/{file.filename}"
        
        file_url = f"{base_url}/{file.filename}"

        # Save file to the folder
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"message": "Sai Sandesh upload successful", "fileurl": file_url}
    except Exception as e:
        # raise HTTPException(status_code=500, detail=str(e))
        logger.error("error: " + str(e))
        return {"error ": str(e)} 