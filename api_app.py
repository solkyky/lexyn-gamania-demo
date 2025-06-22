# api_app.py
import os
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# 讀入 API KEY（環境變數 OPENAI_API_KEY）
openai.api_key = os.getenv("OPENAI_API_KEY")

# 建立 FastAPI 實例
app = FastAPI()

# 設定 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 根路徑測試
@app.get("/")
async def root():
    return {"message": "Lexyn API is running"}

# 語意分析路由
@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return {"error": "Missing input text."}

    # GPT-4o 非同步語意分析
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "請判斷輸入文字是否具備潛在性、勒索性、情緒暗示、誤導原則、不當的脈絡，並簡要解釋原因。"
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return {"analysis": reply}
