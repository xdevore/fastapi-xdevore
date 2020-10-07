from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

time = { "Current Time: " : datetime.now() }

@app.get("/get time/")
def current_time():
    return time

@app.get("/")
def get_current_time():
    final = time.get("Current Time: ")
    return final
