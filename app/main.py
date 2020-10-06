import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

current_time = datetime.now()

@app.get("/PST/")
def pacific_time(current_time):
    pacific_tzinfo = pytz.timezone("US/Pacific")
    pacific_time = current_time.astimezone(pacific_tzinfo)
    return { "Time in PST": pacific_time }
