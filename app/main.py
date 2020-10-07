import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/PST/")
def pacific_time():
    date_format='%m_%d_%Y_%H_%M_%S_%Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    pstDateTime=date.strftime(date_format)
    return pstDateTime
