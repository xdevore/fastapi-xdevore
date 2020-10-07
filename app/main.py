import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def current_time():
    return "Time in PST: " : datetime.now()
