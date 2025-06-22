from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或指定 streamlit.app 網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(req: TextRequest):
    # 假設是簡單分析結果
    return {
        "risk_level": "Low",
        "rewritten": f"{req.text}（這是重寫建議）"
    }#
