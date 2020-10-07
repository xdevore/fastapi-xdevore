from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

time = datetime.now()

def find_month():
    if time[5] == 1:
        return "Yes"
