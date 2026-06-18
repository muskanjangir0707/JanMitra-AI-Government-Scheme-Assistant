from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="JanMitra AI")

with open("scheme_data.txt", "r", encoding="utf-8") as f:
    scheme_text = f.read()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>JanMitra AI</title>
        </head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>JanMitra AI</h1>
            <h2>Intelligent WhatsApp Assistant for Government Welfare Schemes</h2>
            <p>FastAPI Server is Running Successfully 🚀</p>
            <p><a href="/docs">Open FastAPI Docs</a></p>
            <p>Test API: /test?query=pm kisan kya hai</p>
        </body>
    </html>
    """


def generate_answer(query):
    q = query.lower()

    if "naya" in q or "new" in q:
        return f"""
Farmers ke liye PM-KISAN ek important government scheme hai.

Aapka question: {query}

Is scheme me eligible farmer families ko financial support diya jata hai.
"""

    elif "pm kisan" in q or "kisan" in q or "kya" in q:
        return f"""
PM-KISAN ek sarkari yojana hai jo eligible farmer families ko financial support deti hai.

Aapka question: {query}

Is yojana ke through paisa direct farmer ke bank account me bheja jata hai.
"""

    else:
        return f"""
Based on the available scheme document, I found information related to PM-KISAN.

User question: {query}

Please ask about PM Kisan, farmer eligibility, benefits, or payment support.
"""


@app.get("/test")
async def test(query: str):
    return {"response": generate_answer(query)}


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")

    answer = generate_answer(incoming_msg)

    response = MessagingResponse()
    msg = response.message()
    msg.body(answer)

    return str(response)
