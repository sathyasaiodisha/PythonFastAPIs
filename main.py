from fastapi import FastAPI
from routes import saidistricts, samitis, bhajanmandalis, programmes, stateofficebearers, districtofficebearers, samithiofficebearers, events
#from mangum import Mangum

app = FastAPI()

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

# Pass the required route to the decorator. 

#handler = Mangum(app)

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)