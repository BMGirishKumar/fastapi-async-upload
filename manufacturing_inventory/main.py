from fastapi import FastAPI
from database import engine, Base
import models.part

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Manufacturing Inventory API"}