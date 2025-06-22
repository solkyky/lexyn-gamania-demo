from fastapi import FastAPI
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

# ✅ 新增根目錄首頁測試路由
@app.get("/")
async def read_root():
    return {"message": "Lexyn API is running"}

# 假設你已經有 /analyze 等路由，保留即可
