# api_app.py
import os
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# 載入 API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# 建立 FastAPI 實例
app = FastAPI()

# 允許所有跨域請求（方便測試）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 顯示首頁狀態
@app.get("/")
async def root():
    return {"message": "Lexyn API is running"}

# 核心功能：語意分析
@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return {"error": "Missing input text."}

    # GPT-4o 語意分析
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "請判斷這段文字是否具有操控性、勒索性、情緒暗示、或語境不當的特徵，並簡要解釋原因。"},
            {"role": "user", "content": text}
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    return {"analysis": reply}
