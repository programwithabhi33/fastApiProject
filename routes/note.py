from fastapi import APIRouter,Request
from models.note import Note
from config.db import client
from schemas.note import notesEntity,noteEntity
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    notes = client.fastApiNotes.notes.find()
    return templates.TemplateResponse("index.html", {"request": request,"note":notes})

@note.get("/addNote", response_class=HTMLResponse)
async def addNote(request: Request):
    return templates.TemplateResponse("add.html",{"request": request})

@note.post("/")
async def save_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})