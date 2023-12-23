import requests
import streamlit as st
import yaml
from llamaapi import LlamaAPI
import json


hf_token = st.secrets['HF_TOKEN']
with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

class Llm:
    """This class models the llm usage"""

    def __init__(self, prompt):
        """
        Initializes an instance of the Llm class with the provided prompt.

        Args:
        - prompt: A string representing the input prompt for generating output.
        """
        self.output = self.output_generator(prompt)

    def output_generator(self, prompt):
        """
        Generates output using a query function with specific model parameters.

        Args:
        - prompt: a string or input prompt to generate output

        Returns:
        - output: generated output based on the input prompt and model parameters
        """
        api_token = "LL-7V3u02Tx2rlG9ktrLeLAI8JsmJyPaDxRLfKCkvLrVYvCSdsiint2ivcr4S40kWUt"

        llama = LlamaAPI(api_token)

        api_request_json = {
            'model': 'llama-70b-chat',
            "messages": [
        {"role": "user", "content": prompt},
        ]}

        response = llama.run(api_request_json)

        return response.json()['choices'][0]['message']['content']