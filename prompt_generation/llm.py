import requests
import streamlit as st
import yaml

hf_token = st.secrets['HF_TOKEN']
with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

class Llm:
    def __init__(self, prompt):
        self.output = self.output_generator(prompt)
        

    @staticmethod
    @st.cache_data(show_spinner=False)
    def api_query(payload):
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

    def output_generator(self, prompt):
        """
        Generates output using a query function with specific model parameters.

        Args:
        - prompt: a string or input prompt to generate output

        Returns:
        - output: generated output based on the input prompt and model parameters
        """

        model_kwargs = config['model_params']

        output = self.api_query({
            "inputs": prompt,
            "parameters": {**model_kwargs}
        })

        return output