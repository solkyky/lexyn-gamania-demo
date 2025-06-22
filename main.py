import os
import uvicorn
from api_app import app  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api_app:app", host="0.0.0.0", port=port)
