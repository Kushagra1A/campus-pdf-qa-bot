from fastapi import FastAPI, UploadFile, File
import shutil
import os

from services.rag_pipeline import ingest_pdf, ask_question

app = FastAPI()

UPLOAD_DIR = "data"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.get("/")
def home():
    return {"message": "Campus PDF Q&A backend running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(file_path)

    return {"message": "PDF processed successfully"}


@app.get("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {"answer": answer}
