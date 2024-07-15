import glob
import os
import sqlite3
from typing import List, Tuple, TypeAlias
from vector import embed

def index():
    conn = sqlite3.connect('obisidian.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT NOT NULL,
                   content TEXT NOT NULL,
                   embedding BLOB NOT NULL)
                   ''')
    
    conn.commit()

    notes = read_notes()
    embeddings = embed([note[1] for note in notes])
    assert len(notes) == len(embeddings)
    for note, embedding in zip(notes, embeddings):
        blob = embedding.numpy().tobytes()
        cursor.execute('INSERT INTO notes (name, content, embedding) VALUES (?, ?, ?)', (note[0], note[1], blob))

    conn.commit()
    cursor.close()



def read_notes() -> List[Tuple[str, str]]:
    res = []
    path = "/Users/maksymsutkovenko/Documents/Obsidian Vault Copy"
    files = glob.glob(os.path.join(path, '*.md'))
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            name = os.path.basename(file)
            content = f.read()
            res.append((name, content))
    return res
