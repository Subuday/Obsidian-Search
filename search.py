from typing import List, Tuple
from db import db
from vector import embed

def search(query) -> List[Tuple[str, float]]:
    query = "Represent this sentence for searching relevant passages: " + query
    query_embedding = embed([query])[0]

    cursor = db.cursor()
    cursor.execute("SELECT name, cosine_similarity(embedding, ?) as similarity FROM notes ORDER BY similarity DESC LIMIT 10",
              (query_embedding.numpy().tobytes(),))
    notes = cursor.fetchall()
    cursor.close()

    return [(note[0], note[1]) for note in notes]