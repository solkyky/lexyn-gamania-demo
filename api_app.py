# api_app.py
import os
import google.generativeai as genai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Lexyn Gemini API is running"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return {"error": "Missing input text."}

    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(f"請幫我判斷這段文字是否有語境操控、情緒勒索、模糊提示、權威壓力，並用簡潔條列方式指出理由：\n\n{text}")
    
    return {"analysis": response.text}
