import streamlit as st
import os
from dotenv import load_dotenv
from tqdm.auto import tqdm
from data_preparation import augment_prompt, dataset_embeddings, dataset_santuario
import requests


load_dotenv()
hf_token = os.getenv('HF_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
 

model_kwargs = {"max_new_tokens": 512, "top_p": 0.8, "temperature": 0.3}


# 5. Build an app with streamlit
def main():
    st.set_page_config(
        page_title="QA Casa museo", page_icon=":bird:")

    st.header("QA Casa museo :bird:")
    message = st.text_area("Escribe tu pregunta...")

    if message:
        st.write("Generando respuesta...")

        prompt = augment_prompt(message)
        output = query({
	        "inputs": prompt,
            "parameters": {**model_kwargs}
        })

        # add to messages
        result = output[0]['generated_text'][len(prompt)+1:]

        st.info(result)

if __name__ == '__main__':
    main()