import os
import torch
import streamlit as st
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import time
from tqdm.auto import tqdm
from test_hf_embedding import chat, query_generator, dataset_embeddings, dataset_santuario
from sentence_transformers.util import semantic_search



def augment_prompt(query: str):

    output = query_generator([query])

    query_embeddings = torch.FloatTensor(output)
    hits = semantic_search(query_embeddings, dataset_embeddings, top_k=6)
    selected_rows = [hits[0][i]['corpus_id'] for i in range(len(hits[0]))]
    results = dataset_santuario.loc[selected_rows, ['new_column']].values.tolist()
    # get the text from the results
    source_knowledge = "\n".join([x[0] for x in results])
    # feed into an augmented prompt
    augmented_prompt = f"""Utilizando el siguiente contexto, responde la 
    consulta. Imagina que trabajas en un museo y estás respondiendo cordialmente
    las preguntas de los visitantes. 

    Contexto:
    {source_knowledge}

    Consulta: {query}"""
    return augmented_prompt

# 5. Build an app with streamlit
def main():
    st.set_page_config(
        page_title="QA Casa museo", page_icon=":bird:")

    st.header("QA Casa museo :bird:")
    message = st.text_area("Escribe tu pregunta...")

    if message:
        st.write("Generando respuesta...")

        messages = [
        SystemMessage(content="Eres un asistentente util que trabaja en un museo."),
        HumanMessage(content="Hola Asistente, cómo estás hoy?"),
        AIMessage(content="Estoy muy bien, cómo puedo ayudarte?"),]

        prompt = HumanMessage(
            content=augment_prompt(message))

        # add to messages
        messages.append(prompt)
        res = chat(messages)
        result = str(res.content)

        st.info(result)

if __name__ == '__main__':
    main()


