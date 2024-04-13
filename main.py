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

@app.get("/information.html", response_class=HTMLResponse)
def static(request: Request):
    return templates.TemplateResponse("information.html", {"request": request})

@app.get("/datasets.html", response_class=HTMLResponse)
def static(request: Request):
    return templates.TemplateResponse("datasets.html", {"request": request})

@app.get("/procedure.html", response_class=HTMLResponse)
def static(request: Request):
    return templates.TemplateResponse("procedure.html", {"request": request})

@app.post("/submit/")
def submit_input(request: Request, query_input: Annotated[str, Form()]):

    query_input = query_input.upper()

    return templates.TemplateResponse(
        request=request, name="output.html", context={}
    )                                           
'''                                            ^^^^^^^
                                               ||||||| 
1.                                          Yash, add all the variables in the home page here
2.  Go to my repo and then outputs directory, here is an output.xls file, that data needs to be 
    displayed in the Information.html file
3.  datasets.html, it needs the vectorized and the normalized output too
4.  Justify all the text in every page
5.  There's no Adaboost, remove it from the home page and rename the variable too.

'''
