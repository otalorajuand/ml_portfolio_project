import requests
import streamlit as st
import yaml

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Query:
    def __init__(self, query):
        self.query = query
        self.embedded_query = self.query_embedding()

    def query_embedding(self):
        """
        Generates embeddings using the Hugging Face pipeline for a
        sentence-transformers model.

        Args:
        - texts: a list of texts to generate embeddings for

        Returns:
        - response.json(): the JSON response containing the generated embeddings
        """

        hf_token = st.secrets["HF_TOKEN"]
        model_name = config['embedding_model_name']
        api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_name}"
        headers = {"Authorization": f"Bearer {hf_token}"}

        response = requests.post(
            api_url, headers=headers, json={
                "inputs": self.query, "options": {
                    "wait_for_model": True}})
        return response.json()