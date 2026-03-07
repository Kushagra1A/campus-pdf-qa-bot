from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks
