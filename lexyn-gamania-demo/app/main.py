from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Lexyn Context Guard Demo")

class Req(BaseModel):
    text: str

@app.post("/analyze")
def analyze(req: Req):
    """Return a stub analysis so reviewer can curl immediately."""
    return {
        "input": req.text,
        "risk_level": "low",
        "rewritten": req.text
    }