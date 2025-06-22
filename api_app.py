import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

# 建立 FastAPI 實例
app = FastAPI()

# CORS 設定，允許跨來源請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 取得 OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# 健康檢查
@app.get("/")
async def root():
    return {"message": "Lexyn API is running"}

# 語意分析主路由
@app.post("/analyze")
async def analyze(request: Request):
    try:
        data = await request.json()
        text = data.get("text", "")

        if not text:
            return {"error": "Missing input text."}

        # 呼叫 GPT-4o 進行語意分析
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "請判斷這段文字是否具備煽動性、勒索感、情緒勒索、或語氣異常的特徵，並簡要解釋原因。"},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content
        return {"analysis": reply}

    except Exception as e:
        return {"error": str(e)}
