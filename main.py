from fastapi import FastAPI
from routes import saidistricts, samitis, bhajanmandalis, programmes, stateofficebearers, districtofficebearers, samithiofficebearers, events, bvgurus, designations, authorize, usermanagement, sssootweets, saisandeshupload
#from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://localhost", "http://127.0.0.1:8000","http://127.0.0.1", "http://127.0.0.1:4200"],  # Angular dev server
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message":"FastAPI is running"}
    
app.include_router(saidistricts.router)
app.include_router(samitis.router)
app.include_router(bhajanmandalis.router)
app.include_router(programmes.router)
app.include_router(stateofficebearers.router)
app.include_router(districtofficebearers.router)
app.include_router(samithiofficebearers.router)
app.include_router(events.router)
app.include_router(bvgurus.router)
app.include_router(saisandeshupload.router)
app.include_router(designations.router)
app.include_router(sssootweets.router)
app.include_router(usermanagement.router)
app.include_router(authorize.router)
# Pass the required route to the decorator. 

#handler = Mangum(app)

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)