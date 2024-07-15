import sqlite3
import numpy as np

def cosine_similarity(blob1, blob2) -> float:
    vec1 = np.frombuffer(blob1, dtype='float32')
    vec2 = np.frombuffer(blob2, dtype='float32')
  
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)

    similarity = dot_product / (norm_a * norm_b)
  
    return float(similarity)

db = sqlite3.connect('obisidian.db')
db.create_function("cosine_similarity", 2, cosine_similarity)