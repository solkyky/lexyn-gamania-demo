from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發用，正式請改成前端實際網域
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 測試首頁路由
@app.get("/")
async def read_root():
    return {"message": "Lexyn API is running"}

# ✅ 新增分析路由
@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    # 模擬分析邏輯，可之後替換成真正模型推論
    text = data.get("text", "")
    return {
        "input": text,
        "status": "ok",
        "message": f"已收到內容，共 {len(text)} 字元"
    }
