**Multi-Modal AI Content Generation Platform
**


A unified AI application that generates Text, Audio, and Images from user prompts — powered by Hugging Face models, FastAPI, and Streamlit.

**Overview**

This project demonstrates a multi-modal generative system capable of producing:

 Text using TinyLlama-1.1B-Chat

 Audio using Bark (suno/bark-small)

 Images using Stable Diffusion (segmind/tiny-sd)

It combines:

FastAPI for backend inference APIs

Streamlit for an interactive user interface

Docker for containerization and reproducibility

 Features:

 Generate Text, Audio, and Images via simple prompts

 Real-time response using lightweight models optimized for local GPU/CPU

 Modular design — add new modalities easily

 RESTful endpoints for easy integration with other apps

🎨 Streamlit-based multi-modal chat interface


⚙️** Installation & Setup**
1️⃣ Clone the repository
git clone https://github.com/yourusername/multimodal-ai-platform.git
cd multimodal-ai-platform

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

(You can generate this file with pip freeze > requirements.txt.)

4️⃣ Verify CUDA / GPU
python gpu.py

If CUDA is available, models will run on GPU automatically.

5️⃣ Run the FastAPI backend
uvicorn main:app --reload

Backend runs on http://localhost:8000.

6️⃣ Run the Streamlit frontend
streamlit run client.py

Streamlit app opens at http://localhost:8501.

 Example Usage
➤** Text Generation**
GET /generate/text?prompt="Explain FastAPI"

→ Returns natural-language response from TinyLlama.

➤ **Audio Generation**
GET /generate/audio?prompt="Hello world from Bark"

→ Streams generated speech (.wav format).

➤ **Image Generation**
GET /generate/image?prompt="A futuristic city skyline at night"

→ Returns AI-generated image.

 Technologies Used
Category	Tools
Backend	FastAPI, Uvicorn
Frontend	Streamlit
Models	TinyLlama-1.1B-Chat, Bark-small, Tiny-SD
Libraries	Transformers, Diffusers, Torch, NumPy, Pillow, SoundFile
Containerization	Docker
Language	Python 3.10+


**NOTE:** For the model to use the GPU the avaikable python version should be python 3.10 to 3.12. The python version greater than 3.12 will pop an error.


🔥 Future Enhancements

 Add video generation via Hugging Face Diffusers

 Integrate Kafka / Redis queue for async model serving

 Add user authentication & history tracking

 Deploy on AWS / Hugging Face Spaces / Streamlit Cloud

👤 Author

Raghuvardhan Konathala
💼 Data Engineer & ML Enthusiast
📧 raghuvardhan223@gmail.com
🔗 LinkedIn-www.linkedin.com/in/raghuvardhan-k
 • GitHub

📄 License

This project is open-sourced under the MIT License.

Inspiration

This project was built to explore multi-modal AI systems that blend text, audio, and image generation. It showcases how open-source models and lightweight frameworks like FastAPI and Streamlit can power intelligent, real-time content creation.
Thanks to Alireza Parandeh for the systematic explaination of different models that were used in the project.
