from output_generator import output_generator
from augmented_prompt import augment_prompt_generator
import streamlit as st
from tqdm.auto import tqdm

st.set_page_config(
    page_title="Pregúntale a la Casa museo El Santuario", page_icon=":bird:")


# 5. Build an app with streamlit
def run_app():

    st.header("Pregúntale a La Casa Museo :bird:")
    message = st.text_area("Escribe tu pregunta...")

    if st.button("Generar respuesta"):
        with st.spinner("Generando respuesta..."):
            prompt, documents = augment_prompt_generator(message)
            output = output_generator(prompt)
            result = output[0]["generated_text"][len(prompt) + 1:]
        st.info(result)
        st.caption(documents)


if __name__ == '__main__':
    run_app()
