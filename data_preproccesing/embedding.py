import requests
import pandas as pd
import torch
import os
from dotenv import load_dotenv
import yaml


load_dotenv()
hf_token = os.getenv('HF_TOKEN')

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)


model_name = config['model_name']


api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_name}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    """Queries the Hugging Face API for feature extraction.

    Args:
    - texts: a list of texts to be processed

    Returns: JSON response containing extracted features
    """

    response = requests.post(
        api_url, headers=headers, json={
            "inputs": texts, "options": {
                "wait_for_model": True}})
    return response.json()


def embedding_dict_to_dataframe(data_dict):
    """Processes embedding data from a dictionary and saves it into a CSV file.

    Args:
    - data_dict: a dictionary containing embedding data

    Saves the processed data into a 'train.csv' file.
    """

    data = pd.DataFrame.from_records(data_dict)
    data['new_column'] = data.title + ' - ' + data.text_chunk.str.lower()

    texts = list(data.new_column)

    output = query(texts)

    embeddings = pd.DataFrame(output)

    dataset_embeddings = torch.from_numpy(
        embeddings.to_numpy()).to(
        torch.float)

    data_2 = pd.DataFrame(data=dataset_embeddings.numpy())

    df_3 = pd.concat([data, data_2], axis=1)

    df_3.to_csv("train.csv", index=False)
