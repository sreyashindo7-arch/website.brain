import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google.generativeai import GenerativeModel, configure

app = FastAPI()

# Load Gemini API key from Vercel ENV
#configure(api_key="AIzaSyDB2rZye0EbrUsGi6nEWRWLJSlvsT3a7no")
configure(api_key=os.getenv("AIzaSyDB2rZye0EbrUsGi6nEWRWLJSlvsT3a7no"))

# Use Flash 2.0 model
model = GenerativeModel("gemini-2.0-flash")

@app.get("/", response_class=HTMLResponse)
def root():
    message = "You are on a website that has just been deployed to production for the first time! Please reply with an enthusiastic announcement."

    # Generate response
    response = model.generate_content(message)
    reply = response.text or "⚠️ No response from Gemini!"

    reply_html = reply.replace("\n", "<br/>")

    html = f"""
    <html>
        <head><title>Live in an Instant!</title></head>
        <body>
            <p>{reply_html}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
