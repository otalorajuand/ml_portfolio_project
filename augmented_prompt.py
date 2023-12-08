from source_code_generator import source_knowledge_generator, dataset_embbedings_generator, load_data
from query_generator import query_generator


dataset = load_data()
dataset_embeddings = dataset_embbedings_generator(dataset)
top_k = 3

def augment_prompt_generator(query: str):

    embedded_query = query_generator(query)
    source_knowledge = source_knowledge_generator(embedded_query, dataset_embeddings, top_k, dataset)

    # feed into an augmented prompt
    augmented_prompt = f"""Utilizando el siguiente contexto, responde la
    consulta. Imagina que trabajas en un museo y estás respondiendo cordialmente
    las preguntas de los visitantes. Responde la pregunta en español.

    Contexto:
    {source_knowledge}

    Pregunta:
    {query}"""
    return augmented_prompt