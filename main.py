from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World from FastAPI"}

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 8000))  # Railway sets PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
