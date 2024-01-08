import requests
import streamlit as st
import yaml
from bardapi import Bard
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage
)


hf_token = st.secrets['HF_TOKEN']
bard_token = st.secrets['BARD_TOKEN']
openai_token = st.secrets['OPENAI_TOKEN']
with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Llm:
    """This class models the llm usage"""

    def __init__(self, prompt, model):
        """
        Initializes an instance of the Llm class with the provided prompt.

        Args:
        - prompt: A string representing the input prompt for generating output.
        """
        self.stop = 0
        self.output = self.llm_selector(model)(prompt)

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

    def output_generator_hf(self, prompt):
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
            assistant_response = output[0]["generated_text"][len(prompt) + 1:]
        except BaseException:
            st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
            self.stop = 1
            return ''

        return assistant_response

    def output_generator_bard(self, prompt):
        """
        Generates output using a query function with specific model parameters.

        Args:
        - prompt: a string or input prompt to generate output

        Returns:
        - output: generated output based on the input prompt and model parameters
        """

        try:
            bard = Bard(token=bard_token)
            response = bard.get_answer(prompt)
        except BaseException:
            st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
            self.stop = 1
            return ''

        return response['content'].replace('*', '')

    def output_generator_openai(self, prompt):
        """
        Generates output using a query function with specific model parameters.

        Args:
        - prompt: a string or input prompt to generate output

        Returns:
        - output: generated output based on the input prompt and model parameters
        """

        try:
            chat = ChatOpenAI(
                openai_api_key=openai_token,
                model='gpt-3.5-turbo'
            )
            messages = [HumanMessage(content=prompt)]
            response = chat(messages)
        except BaseException:
            st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
            self.stop = 1
            return ''

        return response.content

    def llm_selector(self, model):
        """
        Selects the appropriate output generator method based on the
        provided model.

        Args:
        - model: A string specifying the chosen model for generating output
          ('hf', 'bard', 'openai').

        Returns:
        - output_generator: Corresponding method to generate output based
          on the specified model.
        """

        models_dict = {
            'hf': self.output_generator_hf,
            'bard': self.output_generator_bard,
            'openai': self.output_generator_openai
        }

        output_generator = models_dict[model]

        return output_generator
