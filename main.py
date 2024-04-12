from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# mount static files which don't require any modifications
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates directory
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context={})

def static(request: Request):
    return templates.TemplateResponse("information.html", {"request": request})

@app.post("/submit/")


    # some process using the query_input
    # imagine imitating the querying against the ai model
