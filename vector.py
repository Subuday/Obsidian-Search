from typing import List, Tuple
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-l')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-l', add_pooling_layer=False)
model.eval()

def embed(texts: List[str]) -> List[torch.Tensor]:
    tokens = tokenizer(texts, padding=True, truncation=True, return_tensors='pt', max_length=512)
    with torch.no_grad():
        embeddings = model(**tokens)[0][:, 0]
    return embeddings