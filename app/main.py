import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

current_time = datetime.datetime(2015, 5, 5)

@app.get("/PST/")
def pacific_time(current_time):
    pacific_tzinfo = pytz.timezone("US/Pacific")
    pacific_time = current_time.astimezone(pacific_tzinfo)
    print({ "Time in PST": pacific_time })
