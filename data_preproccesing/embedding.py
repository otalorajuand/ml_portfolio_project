import requests
import pandas as pd
import torch


model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"


api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(
        api_url, headers=headers, json={
            "inputs": texts, "options": {
                "wait_for_model": True}})
    return response.json()

def embedding_dict_to_dataframe(data_dict):

    data = pd.DataFrame.from_records(data_dict)
    data['new_column'] = data.title + ' - ' + data.text_chunk

    texts = list(data.new_column )

    output = query(texts)

    embeddings = pd.DataFrame(output)

    dataset_embeddings = torch.from_numpy(embeddings.to_numpy()).to(torch.float)

    data_2 = pd.DataFrame(data=dataset_embeddings.numpy())

    df_3 = pd.concat([data, data_2], axis=1)

    df_3.drop(columns=['new_column'])

    df_3.to_csv("train.csv", index=False)