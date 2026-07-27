"""
Vector memory — semantic search over embedded text.

Stub for Phase 3+. Suggested implementation: chromadb or FAISS +
sentence-transformers for embeddings.

Example intended usage once implemented:

    vm = VectorMemory()
    vm.add("altron uses python 3.11", metadata={"source": "chat"})
    results = vm.search("what python version does altron use?")
"""


class VectorMemory:
    def __init__(self):
        # TODO: initialize a chromadb collection or FAISS index here
        self._store = []  # placeholder in-memory list of (text, metadata)

    def add(self, text: str, metadata: dict | None = None):
        # TODO: embed `text` and store the vector instead of raw text
        self._store.append({"text": text, "metadata": metadata or {}})

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        # TODO: embed `query` and return nearest neighbors by cosine similarity
        # Placeholder: naive substring match so the interface works end-to-end
        return [item for item in self._store if query.lower() in item["text"].lower()][:top_k]
