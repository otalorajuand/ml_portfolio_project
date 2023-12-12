import streamlit as st
import time

st.set_page_config(
    page_title="Pregúntale a La Casa Museo", page_icon=":house:")

from prompt_generation.output_generator import output_generator
from prompt_generation.augmented_prompt import augment_prompt_generator


st.title("Pregúntale a La Casa Museo :house:")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Haznos una pregunta"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        augment_prompt, documents = augment_prompt_generator(prompt)
        output = output_generator(augment_prompt)
        assistant_response = output[0]["generated_text"][len(augment_prompt) + 1:]
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
        {"role": "assistant", "content": full_response})
