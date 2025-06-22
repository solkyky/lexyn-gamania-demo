from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 加上 CORS 中介層
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發中允許所有網域跨域請求
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
def analyze_text(payload: dict):
    text = payload.get("text", "")
    # 模擬回傳
    return {
        "risk_level": "低",
        "rewritten": f"（重新改寫）{text}"
    }
