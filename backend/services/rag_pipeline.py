from services.pdf_processor import extract_text_from_pdf, split_text
from services.vector_store import create_vector_store, search


def ingest_pdf(file_path):
    text = extract_text_from_pdf(file_path)

    chunks = split_text(text)

    create_vector_store(chunks)


def ask_question(question):
    context = search(question)

    answer = "\n\n".join(context)

    return answer
