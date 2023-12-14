from prompt_generation.source_code_generator import source_knowledge_generator, dataset_embbedings_generator, load_data
from prompt_generation.query_generator import query_generator
import streamlit as st
import yaml

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

top_k = config['top_k']

try:
  dataset = load_data()
except:
   st.stop()

dataset_embeddings = dataset_embbedings_generator(dataset)



def augment_prompt_generator(query: str):
    """
    Generates an augmented prompt for question answering in a museum context.

    Args:
    - query (str): The input query or question.

    Returns:
    - augmented_prompt (str): The augmented prompt incorporating context
      and query.
    - documents_prompt (str): Information about the documents used in
      generating the context.
    """

    embedded_query = query_generator(query)
    source_knowledge, documents = source_knowledge_generator(
        embedded_query, dataset_embeddings, top_k, dataset)

    # feed into an augmented prompt
    augmented_prompt = f"""<s>[INST] Utilizando el siguiente contexto, responde la
    pregunta. Si no sabes la respuesta, responde que no sabes, no intentes inventar una respuesta.
    Imagina que trabajas en un museo y estás respondiendo cordialmente
    las preguntas de los visitantes. Responde saludando en nombre de
    La Casa Museo El Santuario y agradeciendo por preguntar.
    Responde la pregunta en español.

    contexto:
    {source_knowledge}

    pregunta:
    {query}[/INST]"""

    documents_prompt = f"""La información fue obtenida de los siguientes documentos:
    {documents}
    """
    return augmented_prompt, documents_prompt
