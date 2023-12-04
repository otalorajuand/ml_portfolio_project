import streamlit as st
from dotenv import load_dotenv
from tqdm.auto import tqdm
from data_preparation import augment_prompt, dataset_embeddings, dataset_santuario
from langchain import HuggingFaceHub, LLMChain


load_dotenv()

repo_id = "tiiuae/falcon-7b-instruct"

llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.3, "max_length": 252}
)


# 5. Build an app with streamlit
def main():
    st.set_page_config(
        page_title="QA Casa museo", page_icon=":bird:")

    st.header("QA Casa museo :bird:")
    message = st.text_area("Escribe tu pregunta...")

    if message:
        st.write("Generando respuesta...")

        prompt = augment_prompt(message)
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        # add to messages
        result = llm_chain.run(message)

        st.info(result)

if __name__ == '__main__':
    main()
