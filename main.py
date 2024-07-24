from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union
from datetime import datetime

app = FastAPI()

# Definición del modelo para las medidas
class Measure(BaseModel):
    sensor_id: int
    sensor_type: str
    value: float
    timestamp: datetime

# Definición del modelo para SmartThing
class SmartThing(BaseModel):
    id: int
    descriptor: str
    measures: List[Measure] = []

# Base de datos en memoria
smartthings_db: Dict[int, SmartThing] = {}

@app.get("/smartthings/", response_model=List[SmartThing])
def get_smartthings():
    return list(smartthings_db.values())

@app.get("/smartthings/{smartthing_id}/measures", response_model=List[Measure])
def get_measures(smartthing_id: int):
    smartthing = smartthings_db.get(smartthing_id)
    if not smartthing:
        raise HTTPException(status_code=404, detail="SmartThing not found")
    return smartthing.measures

@app.post("/smartthings/{smartthing_id}/measures", response_model=Measure)
def add_measure(smartthing_id: int, measure: Measure):
    smartthing = smartthings_db.get(smartthing_id)
    if not smartthing:
        raise HTTPException(status_code=404, detail="SmartThing not found")
    smartthing.measures.append(measure)
    return measure

@app.post("/smartthings/", response_model=SmartThing)
def create_smartthing(smartthing: SmartThing):
    if smartthing.id in smartthings_db:
        raise HTTPException(status_code=400, detail="SmartThing already exists")
    smartthings_db[smartthing.id] = smartthing
    return smartthing
