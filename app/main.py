from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/{id}")
def x_to_the_e(id: str):
    intValue = int(id)
    return { "x to the power of e" : math.exp(intValue)}
