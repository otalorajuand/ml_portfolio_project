import requests
from datasets import load_dataset
import torch
from sentence_transformers.util import semantic_search
from langchain.prompts import PromptTemplate


model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

def query_generator(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

def augment_prompt(query: str):

    output = query_generator([query])

    query_embeddings = torch.FloatTensor(output)
    hits = semantic_search(query_embeddings, dataset_embeddings, top_k=6)
    selected_rows = [hits[0][i]['corpus_id'] for i in range(len(hits[0]))]
    results = dataset_santuario.loc[selected_rows, ['new_column']].values.tolist()
    # get the text from the results
    source_knowledge = "\n".join([x[0] for x in results])
    # feed into an augmented prompt
    augmented_prompt = f"""Utilizando el siguiente contexto, responde la 
    consulta. Imagina que trabajas en un museo y estás respondiendo cordialmente
    las preguntas de los visitantes. Responde la pregunta en español.

    Contexto:
    {source_knowledge}

    Consulta: """
    augmented_prompt = augmented_prompt.replace("{", "")
    augmented_prompt = augmented_prompt.replace("}", "")
    final_prompt = PromptTemplate(
        input_variables=["question"],
        template = augmented_prompt + "{question}")
    return final_prompt

dataset_santuario = load_dataset('otalorajuand/data_house_museum', split="train").to_pandas()

not_embedding_columns = ['id', 'title', 'text_chunk', 'new_column']
embeddings = dataset_santuario.drop(columns=not_embedding_columns)

dataset_embeddings = torch.from_numpy(embeddings.to_numpy()).to(torch.float)
