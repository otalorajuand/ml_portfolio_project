import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from datasets import load_dataset
import pinecone
import time
from langchain.embeddings.openai import OpenAIEmbeddings
from tqdm.auto import tqdm
from langchain.vectorstores import Pinecone
from test_2 import vectorstore, chat



def augment_prompt(query: str):
    # get top 3 results from knowledge base
    results = vectorstore.similarity_search(query, k=3)
    # get the text from the results
    source_knowledge = "\n".join([x.page_content for x in results])
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