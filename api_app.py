import openai
import os
from fastapi import FastAPI
from pydantic import BaseModel

openai.api_key = os.getenv("OPENAI_API_KEY")  # 或者你可以直接寫入金鑰

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(data: AnalyzeRequest):
    prompt = f"""
你是一位語境分析助手，請針對以下句子做語意風險判定與分析：

句子：「{data.text}」

請用 JSON 格式回答：
{{
  "情緒": "",
  "是否為負面語意": true/false,
  "潛在風險等級": "低/中/高",
  "簡短說明": ""
}}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    result = response['choices'][0]['message']['content']
    return {"input": data.text, "analysis": result}
