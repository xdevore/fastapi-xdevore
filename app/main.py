import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

time = { "Time in PST: " : datetime.now() }

@app.get("/")
def current_time():
    return time
