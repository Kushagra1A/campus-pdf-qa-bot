from fastapi import FastAPI

app = FastAPI(title="Campus PDF Q&A Bot")

@app.get("/")
def home():
    return {"message": "Campus PDF Q&A backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}

