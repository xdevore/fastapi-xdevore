import math
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

@app.get("/{id}")
def e_to_the_x(id: str):
    intValue = int(id)
    return { "e to the power of x" : math.exp(intValue)}

@app.get("/html/{id}", response_class=HTMLResponse)
async def index(request: Request, id:str):
    intValue = int(id)
    message = "e to the power of x: " + str(math.exp(intValue))
    return templates.TemplateResponse("index.html", {"request": request, "message" : message})
