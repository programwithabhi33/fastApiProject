from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('mongodb+srv://abhi:IveCVi4vb5KpwQPx@cluster0.26o1d.mongodb.net')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    notes = client.fastApiNotes.notes.find()
    return templates.TemplateResponse("index.html", {"request": request,"note":notes})
@app.get("/addNote", response_class=HTMLResponse)
async def addNote(request: Request):
    return templates.TemplateResponse("add.html",{"request": request})
@app.post("/saveNote", response_class=HTMLResponse)
async def saveNote(request: Request):
    print(request)
    return templates.TemplateResponse("add.html",{"request": request})
