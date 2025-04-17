from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is live on Railway"}

# This block is only for local testing
if _name_ == "_main_":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
