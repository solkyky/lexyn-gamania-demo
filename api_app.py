# api_app.py
import os
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# 載入 API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化 FastAPI 應用
app = FastAPI()

# 加入 CORS middleware（支援前端呼叫）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 基本健康檢查
@app.get("/")
async def root():
    return {"message": "Lexyn API is running"}

# 語意分析端點
@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return {"error": "Missing input text."}

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "請判斷這段文字是否具有操控性、勒索感、情緒控制、或話術暗示特徵，並簡要解釋原因。"
                },
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content
        return {"analysis": reply}
    except Exception as e:
        return {"error": str(e)}
