# Campus Q&A Bot

A Retrieval-Augmented Generation (RAG) agent that answers hyper-specific questions about university coursework — lecture slides, PPTs, and notes — instead of giving the vague, generic answers you get from a general-purpose chatbot.

Built with a LangGraph multi-agent workflow on a FastAPI backend.

---

## The problem

Students have hundreds of pages of lecture material scattered across PDFs and PPTs. Searching them is painful: Ctrl+F only finds exact words, and asking ChatGPT gives you textbook-general answers that don't match what your specific professor actually taught or what's actually on your syllabus.

This bot answers from *your* course material, and only from your course material.

---

## What it does

- Ingests institutional academic resources (lecture PPTs, slides, notes) and chunks them into a vector store
- Answers context-specific queries grounded in those documents rather than in the model's general knowledge
- Routes queries through a **LangGraph multi-agent workflow**, so retrieval, reasoning, and answer construction are separate steps rather than one monolithic prompt
- Serves everything through a **FastAPI** backend with asynchronous request handling, so vector queries don't block each other under concurrent load

---

## Architecture

```
User query
    │
    ▼
FastAPI endpoint (async)
    │
    ▼
LangGraph workflow
    ├── Retrieval agent  ──►  VectorDB (semantic search over course material)
    ├── Reasoning step   ──►  decides whether retrieved context is sufficient
    └── Answer agent     ──►  composes grounded response
    │
    ▼
Response (grounded in source documents)
```

**Why multi-agent instead of a single RAG chain:** a single retrieve-then-answer chain will happily answer even when the retrieved chunks are irrelevant. Splitting retrieval from answer construction makes it possible to check whether the context actually supports an answer before generating one — which matters a lot when the whole point is *not* falling back on generic knowledge.

---

## Stack

| Layer | Tool |
|---|---|
| Orchestration | LangGraph, LangChain |
| LLM | OpenAI API |
| Vector store | VectorDB |
| Backend | FastAPI (async) |
| Language | Python |

---

## Setup

```bash
# clone and enter the repo
git clone https://github.com/Kushagra1A/campus-pdf-qa-bot.git
cd campus-pdf-qa-bot

# install dependencies
pip install -r requirements.txt

# set your API key
cp .env.example .env
# then add your OPENAI_API_KEY to .env
```

## Running it

```bash
# start the API
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` for the interactive API docs.

### Ingesting documents

Drop your lecture PDFs/PPTs into the documents folder and run the ingestion step to build the vector index before querying.

---

## Example

**Query:** "What did the OS lecture say about the difference between preemptive and non-preemptive scheduling?"

**Response:** answers from the actual lecture slides — including the specific examples and terminology your course used — rather than a textbook definition.

---

## Notes & limitations

- Answer quality depends heavily on the quality of the source material; badly formatted slides chunk badly
- Currently tuned for text-heavy academic documents — diagram-heavy slides lose information in extraction
- No auth layer; intended as a local/personal tool rather than a multi-tenant deployment

---

## Author

**Kushagra Kalbhawar**
[LinkedIn](https://linkedin.com/in/kushagra-kalbhawar-020b4229a) · [GitHub](https://github.com/Kushagra1A)
