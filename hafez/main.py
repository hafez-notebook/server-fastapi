from fastapi import FastAPI

from hafez.db import *
from hafez.apps import user, note
from hafez.about import __version__, __description__

app = FastAPI(name="Hafez", descreption=__description__, version=__version__)
app.include_router(user.user_router)
app.include_router(note.note_router)

@app.on_event("startup")
async def startup():
    if conn.is_closed():
        conn.connect()
