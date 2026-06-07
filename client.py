# import streamlit as st
# import requests

# st.title("FASTAPI Multi-Modal ChatBot")

# # Mode selector
# mode = st.sidebar.selectbox(
#     "Choose Generation Mode",
#     ["Text", "Audio", "Image","Video"]
# )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         content = message["content"]
#         if isinstance(content, bytes) and message.get("type") == "audio":
#             st.audio(content, format="audio/mp3")
#         elif message.get("type") == "image":
#             st.image(content)
#         else:
#             st.markdown(content)

# # One chat input for all modes
# if prompt := st.chat_input(f"Enter your {mode.lower()} prompt here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     if mode == "Text":
#         response = requests.get("http://localhost:8000/generate/text", params={"prompt": prompt})
#         response.raise_for_status()
#         reply = response.text
#         st.session_state.messages.append({"role": "assistant", "content": reply})
#         with st.chat_message("assistant"):
#             st.markdown(reply)

#     elif mode == "Audio":
#         response = requests.get("http://localhost:8000/generate/audio", params={"prompt": prompt})
#         response.raise_for_status()
#         audio_bytes = response.content
#         st.session_state.messages.append({"role": "assistant", "content": audio_bytes, "type": "audio"})
#         with st.chat_message("assistant"):
#             st.text("Here is your generated audio:")
#             st.audio(audio_bytes, format="audio/mp3")

#     elif mode == "Image":
#         response = requests.get("http://localhost:8000/generate/image", params={"prompt": prompt})
#         response.raise_for_status()
#         image_bytes = response.content
#         st.session_state.messages.append({"role": "assistant", "content": image_bytes, "type": "image"})
#         with st.chat_message("assistant"):
#             st.text("Here is your generated image:")
#             st.image(image_bytes)
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from diffusers import DiffusionPipeline

st.set_page_config(page_title="TinyLLM Playground", layout="wide")
st.title("🎨 TinyLLM Multi-Modal Playground")
st.write("Text Generation | Image Generation | All running locally!")

# ============ MODEL LOADING (cached, loads once) ============
@st.cache_resource
def load_text_model():
    """Load TinyLlama for text generation"""
    try:
        tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        model = AutoModelForCausalLM.from_pretrained(
            "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            torch_dtype=torch.float32,
            device_map="cpu"
        )
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading text model: {e}")
        return None, None

@st.cache_resource
def load_image_model():
    """Load Stable Diffusion for image generation"""
    try:
        pipe = DiffusionPipeline.from_pretrained(
            "segmind/tiny-sd",
            torch_dtype=torch.float32
        )
        pipe = pipe.to("cpu")
        return pipe
    except Exception as e:
        st.error(f"Error loading image model: {e}")
        return None

# ============ TEXT GENERATION ============
st.header("📝 Text Generation")
text_prompt = st.text_input("Enter a prompt:", placeholder="Tell me a joke about...")

if st.button("Generate Text", key="text_btn"):
    if text_prompt:
        with st.spinner("Generating text..."):
            tokenizer, model = load_text_model()
            if tokenizer and model:
                try:
                    inputs = tokenizer(text_prompt, return_tensors="pt")
                    with torch.no_grad():
                        outputs = model.generate(
                            inputs["input_ids"],
                            max_length=150,
                            temperature=0.7,
                            top_p=0.9,
                            do_sample=True
                        )
                    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                    st.success("✅ Generated!")
                    st.write(response)
                except Exception as e:
                    st.error(f"Generation error: {e}")
            else:
                st.error("Model failed to load")

# ============ IMAGE GENERATION ============
st.header("🖼️ Image Generation")
image_prompt = st.text_input("Enter an image prompt:", placeholder="A sunset over mountains...")

if st.button("Generate Image", key="image_btn"):
    if image_prompt:
        with st.spinner("Generating image (this may take a minute)..."):
            pipe = load_image_model()
            if pipe:
                try:
                    image = pipe(image_prompt, num_inference_steps=20).images[0]
                    st.success("✅ Generated!")
                    st.image(image, caption=f"Generated: {image_prompt}")
                except Exception as e:
                    st.error(f"Image generation error: {e}")
            else:
                st.error("Image model failed to load")

st.divider()
st.info("💡 **Note:** First run downloads model weights (~2-5 GB). Subsequent runs are instant!")

st.divider()
st.info("💡 **Note:** First run downloads model weights (~2-5 GB). Subsequent runs are instant!")
