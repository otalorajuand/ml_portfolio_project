import requests
import os
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
hf_token = os.getenv('HF_TOKEN')


@st.cache_data(show_spinner=False)
def query(payload):
     
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {hf_token}"}
    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()
 

def output_generator(prompt):
     
    model_kwargs = {"max_new_tokens": 512, "top_p": 0.8, "temperature": 0.3}
    output = query({
            "inputs": prompt,
            "parameters": {**model_kwargs}
        })
        
    return output