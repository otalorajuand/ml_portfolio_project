import requests
from datasets import load_dataset
import torch
from sentence_transformers.util import semantic_search
import os
from langchain.chat_models import ChatOpenAI

model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"

OPENAI_API_KEY = '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'

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or OPENAI_API_KEY

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

chat = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model='gpt-3.5-turbo'
)

def query_generator(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

dataset_santuario = load_dataset('otalorajuand/data_house_museum', split="train").to_pandas()

not_embedding_columns = ['id', 'title', 'text_chunk', 'new_column']
embeddings = dataset_santuario.drop(columns=not_embedding_columns)

dataset_embeddings = torch.from_numpy(embeddings.to_numpy()).to(torch.float)

