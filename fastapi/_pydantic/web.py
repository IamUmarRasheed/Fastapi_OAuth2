from model import Creature
from fastapi import FastAPI

app :FastAPI= FastAPI()
@app.get('/creature')
def  getall()->list[Creature]:
    from data import get_creatures
    return get_creatures()
    