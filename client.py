import streamlit as st
import requests

st.title("FASTAPI Multi-Modal ChatBot")

# Mode selector
mode = st.sidebar.selectbox(
    "Choose Generation Mode",
    ["Text", "Audio", "Image","Video"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        content = message["content"]
        if isinstance(content, bytes) and message.get("type") == "audio":
            st.audio(content, format="audio/mp3")
        elif message.get("type") == "image":
            st.image(content)
        else:
            st.markdown(content)

# One chat input for all modes
if prompt := st.chat_input(f"Enter your {mode.lower()} prompt here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if mode == "Text":
        response = requests.get("http://localhost:8000/generate/text", params={"prompt": prompt})
        response.raise_for_status()
        reply = response.text
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    elif mode == "Audio":
        response = requests.get("http://localhost:8000/generate/audio", params={"prompt": prompt})
        response.raise_for_status()
        audio_bytes = response.content
        st.session_state.messages.append({"role": "assistant", "content": audio_bytes, "type": "audio"})
        with st.chat_message("assistant"):
            st.text("Here is your generated audio:")
            st.audio(audio_bytes, format="audio/mp3")

    elif mode == "Image":
        response = requests.get("http://localhost:8000/generate/image", params={"prompt": prompt})
        response.raise_for_status()
        image_bytes = response.content
        st.session_state.messages.append({"role": "assistant", "content": image_bytes, "type": "image"})
        with st.chat_message("assistant"):
            st.text("Here is your generated image:")
            st.image(image_bytes)
