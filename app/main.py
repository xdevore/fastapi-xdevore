import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

time = { "Time in PST: " : datetime.now() }

@app.get("/get time/")
def current_time():
    return time

@app.get("/")
def get_current_time():
    final = time.get("Time in PST: ")
    return final

def pacific_time():
    return pytz.timezone("US/Pacific")
