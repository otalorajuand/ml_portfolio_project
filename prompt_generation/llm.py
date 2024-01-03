import requests
import streamlit as st
import yaml

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
        self.stop = 0
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

        try:
            assistant_response = output[0]["generated_text"][len(prompt)+1:]
        except:
            st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
            self.stop = 1
            return ''

        return assistant_response