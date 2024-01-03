import streamlit as st
import time

st.set_page_config(
    page_title="Pregúntale a La Casa Museo", page_icon=":house:")

from prompt_generation.llm import Llm
from prompt_generation.augmented_prompt import AugmentedPrompt

st.markdown("""
<style>
    .st-emotion-cache-1rtdyuf {
        color: #FFFFFF;
    }

    .st-emotion-cache-1egp75f {
        color: #FFFFFF;
    }

    .st-emotion-cache-1rtdyuf {
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

st.title("Pregúntale a La Casa Museo :house:")

# Initialize chat history
if "messages_santuario" not in st.session_state:
    st.session_state.messages_santuario = []

# Display chat messages from history on app rerun
for message in st.session_state.messages_santuario:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["documents"])

# Accept user input
if prompt := st.chat_input("Haznos una pregunta"):
    # Add user message to chat history
    st.session_state.messages_santuario.append({"role": "user", "content": prompt, "documents": ""})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("Generando respuesta..."):
            augmented_prompt_instance = AugmentedPrompt(prompt, "data_santuario")
            augment_prompt = augmented_prompt_instance.augmented_prompt
            documents = augmented_prompt_instance.documents_prompt

            llm_instace = Llm(augment_prompt)
            llm_output = llm_instace.output

        if llm_instace.stop == 1:
            st.stop()

        # Simulate stream of response with milliseconds delay
        for chunk in llm_output.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.caption(documents)
    # Add assistant response to chat history
    st.session_state.messages_santuario.append(
        {"role": "assistant", "content": full_response, "documents": documents})
