import requests
import os
from dotenv import load_dotenv
import yaml

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

load_dotenv()


def query_generator(texts: list):
    """
    Generates embeddings using the Hugging Face pipeline for a
    sentence-transformers model.

    Args:
    - texts: a list of texts to generate embeddings for

    Returns:
    - response.json(): the JSON response containing the generated embeddings
    """

    hf_token = os.getenv('HF_TOKEN')
    model_name = config['embedding_model_name']
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_name}"
    headers = {"Authorization": f"Bearer {hf_token}"}

    response = requests.post(
        api_url, headers=headers, json={
            "inputs": texts, "options": {
                "wait_for_model": True}})
    return response.json()
