from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/{id}")
def e_to_the_x(id: str):
    intValue = int(id)
    return { "e to the power of x" : math.exp(intValue)}
