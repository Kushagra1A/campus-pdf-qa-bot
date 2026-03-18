from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    token=os.getenv("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")
)

from services.pdf_processor import extract_text_from_pdf, split_text
from services.vector_store import create_vector_store, search


def ingest_pdf(file_path):
    text = extract_text_from_pdf(file_path)

    chunks = split_text(text)

    create_vector_store(chunks)


def ask_question(question):
    context = search(question)

    context_text = "\n\n".join(context)

    prompt = f"""
Answer the question using the context below.

Context:
{context_text}

Question:
{question}

Give a clear structured answer.
"""

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    answer = response.choices[0].message.content

    return answer
