from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

time = datetime.now()

@app.get("/")
def get_current_time():
    return time
