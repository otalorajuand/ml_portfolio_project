import streamlit as st
from bardapi import Bard


hf_token = st.secrets['HF_TOKEN']

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

    def output_generator(self, prompt):
        """
        Generates output using a query function with specific model parameters.

        Args:
        - prompt: a string or input prompt to generate output

        Returns:
        - output: generated output based on the input prompt and model parameters
        """
        api_token = 'ewjoA8hY8RZ_62-N79O5jlkPt-ksX_0nUxR2_HWLsDx8_QpisSDaXXB4meClz3ZxBR8JeA.'

        try:
            bard = Bard(token=api_token)
            response = bard.get_answer(prompt)
        except:
            st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
            self.stop = 1
            return ''

        return response['content'].replace('*','')