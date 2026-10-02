import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

# Load API key
GEMINI_API_KEY = "AIzaSyDB2rZye0EbrUsGi6nEWRWLJSlvsT3a7no"

# Configure model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# FastAPI App
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, reply: str = None, user_input: str = None):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "reply": reply,
        "user_input": user_input
    })

@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, message: str = Form(...)):
    response = model.generate_content(message)
    reply = response.text
    return templates.TemplateResponse("index.html", {
        "request": request,
        "reply": reply,
        "user_input": message
    })
