from fastapi import FastAPI
from routes import saidistricts, samitis, bhajanmandalis

app = FastAPI()

app.include_router(saidistricts.router)
app.include_router(samitis.router)
app.include_router(bhajanmandalis.router)

# Pass the required route to the decorator. 

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
