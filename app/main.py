import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/PST/")
def pacific_time():
    current_time = datetime.now()
    pacific_time = current_time.astimezone(timezone('US/Pacific'))
    return { "Time in PST: " : pacific_time }
