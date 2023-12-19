from prompt_generation.source_knowledge import SourceKnowledge
from prompt_generation.query import Query
import streamlit as st
import yaml

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

top_k = config['top_k']

class AugmentedPrompt:
    def __init__(self, query):
      self.query = query
      self.augmented_prompt, self.documents_prompt = self.augment_prompt_generator()

    def augment_prompt_generator(self):
        
        """
        Generates an augmented prompt for question answering in a museum context.

        Returns:
        - augmented_prompt (str): The augmented prompt incorporating context
          and query.
        - documents_prompt (str): Information about the documents used in
          generating the context.
        """

        query_instance = Query(self.query)
        source_knowledge_instace = SourceKnowledge(query_instance, top_k)

        # feed into an augmented prompt
        augmented_prompt = f"""<s>[INST] Utilizando el siguiente contexto, responde la
        pregunta. Si no sabes la respuesta, responde que no sabes, no intentes inventar una respuesta.
        Imagina que trabajas en un museo y estás respondiendo cordialmente
        las preguntas de los visitantes. Responde saludando en nombre de
        La Casa Museo El Santuario y agradeciendo por preguntar.
        Responde la pregunta en español.

        contexto:
        {source_knowledge_instace.source_knowledge}

        pregunta:
        {self.query}[/INST]"""

        documents_prompt = f"""La información fue obtenida de los siguientes documentos:
        {source_knowledge_instace.documents}
        """
        return augmented_prompt, documents_prompt