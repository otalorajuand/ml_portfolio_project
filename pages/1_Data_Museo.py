import streamlit as st
import time

st.set_page_config(
    page_title="Pregúntale a La Casa Museo", page_icon=":house:")

from prompt_generation.llm import Llm
from prompt_generation.augmented_prompt import AugmentedPrompt


st.title("Pregúntale a La Casa Museo :house:")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["documents"])

# Accept user input
if prompt := st.chat_input("Haznos una pregunta"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, "documents": ""})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stop = 0
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("Generando respuesta..."):
            augmented_prompt_instance = AugmentedPrompt(prompt, "data_museum")
            augment_prompt = augmented_prompt_instance.augmented_prompt
            documents = augmented_prompt_instance.documents_prompt

            llm_instace = Llm(augment_prompt)
            llm_output = llm_instace.output
            try:
                assistant_response = llm_output[0]["generated_text"][len(augment_prompt)+1:]
            except:
                st.error('Revisa tu conexión a internet. Inténtalo más tarde.')
                stop = 1

        if stop == 1:
            st.stop()

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.caption(documents)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response, "documents": documents})
