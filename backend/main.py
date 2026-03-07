from fastapi import FastAPI, UploadFile, File
import shutil
import os

from services.rag_pipeline import ingest_pdf, ask_question

app = FastAPI()

UPLOAD_DIR = "data"


@app.get("/")
def home():
    return {"message": "Campus PDF Q&A backend running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(file_location)

    return {"message": "PDF processed successfully"}


@app.get("/ask")
def ask(question: str):
    result = ask_question(question)

    return {"context": result}
