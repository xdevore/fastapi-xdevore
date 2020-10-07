import pytz
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/PST/")
def pacific_time():
    pacific = pytz.timezone('US/Pacific')
    d = datetime.datetime.now(pacific)
    return { d.tzinfo }
