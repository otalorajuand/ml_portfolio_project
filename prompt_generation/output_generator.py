import requests
import streamlit as st
import yaml


hf_token = st.secrets['HF_TOKEN']

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)


@st.cache_data(show_spinner=False)
def query(payload):
    """
    Query a Hugging Face model hosted on the Hugging Face model hub using API
    inference.

    Args:
    - payload: a dictionary representing the payload to be sent in the API
               request

    Returns:
    - A JSON response containing the result of the API inference request
    """

    model_name = config['model_name']
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {hf_token}"}
    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()


def output_generator(prompt):
    """
    Generates output using a query function with specific model parameters.

    Args:
    - prompt: a string or input prompt to generate output

    Returns:
    - output: generated output based on the input prompt and model parameters
    """

    model_kwargs = config['model_params']

    output = query({
        "inputs": prompt,
        "parameters": {**model_kwargs}
    })

    return output
