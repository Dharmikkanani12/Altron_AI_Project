"""
RAG (Retrieval-Augmented Generation) — let ALTRON answer questions
grounded in documents you give it (PDFs, manuals, code docs).

Stub for Phase 3+.

Intended flow:
    Document -> chunk -> embed -> store in VectorMemory -> retrieve on query -> feed to Brain
"""

from memory.vector_memory import VectorMemory


class RAGPipeline:
    def __init__(self):
        self.vector_memory = VectorMemory()

    def ingest_document(self, file_path: str):
        # TODO: load the document (PDF/text), chunk it, and add each chunk
        # to self.vector_memory. See pdf-reading skill or a library like
        # pypdf/unstructured for extraction.
        text = self._load_text(file_path)
        for chunk in self._chunk(text):
            self.vector_memory.add(chunk, metadata={"source": file_path})

    def _load_text(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    def _chunk(self, text: str, chunk_size: int = 500) -> list[str]:
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def answer(self, question: str) -> str:
        matches = self.vector_memory.search(question)
        if not matches:
            return "I don't have any relevant documents to answer that yet."
        # TODO: feed matches + question into Brain.think() for a real answer
        context = "\n".join(m["text"] for m in matches)
        return f"(placeholder) Based on ingested docs:\n{context[:300]}..."
