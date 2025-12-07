# tinyllm

TinyLLM — a minimal multi-modal Local LLM playground with FastAPI + BentoML

This repository demonstrates a small, opinionated setup for running local multimodal model endpoints (text, audio, image) together in a simple FastAPI service. It's intended as a lightweight developer playground or reference for packaging a model with BentoML for production-style serving.

NOTE: This project downloads and uses large ML model weights (Diffusion / LLM / audio models). Use a machine with sufficient disk, memory, and ideally a GPU.

---

## Features

- FastAPI endpoints for generating text, audio, and images
- Example Streamlit client for interactive usage
- Model-loading helpers (keeps model usage modular)
- BentoML service (in `bento.py`) for running a model server that persists models in memory and scales better for production


## Architectures / Models used (examples)
- Text: TinyLlama (TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- Audio: Suno/Bark (suno/bark-small)
- Image: Stable Diffusion variant (segmind/tiny-sd)

Files of interest:
- `main.py` — FastAPI app exposing /generate/text, /generate/audio, /generate/image
- `client.py` — Example Streamlit front-end that talks to the FastAPI server
- `models.py` — Model loading and generation functions (text, audio, image)
- `bento.py` — BentoML service wrapper that keeps models loaded in memory
- `utils.py` — utility functions (image/audio conversion)

---

## Quick setup (development)

1. Clone the repository

```bash
git clone https://github.com/<your-username>/tinyllm.git
cd tinyllm
```

2. Create and activate a Python environment (recommended)

Windows (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install recommended dependencies

```bash
pip install -r requirements.txt
# If there is no requirements, the typical deps are:
# pip install fastapi uvicorn torch transformers diffusers bentoml httpx streamlit soundfile pillow numpy
```

Note: If using GPU, install the appropriate CUDA-enabled PyTorch package from https://pytorch.org.

---

## Running the app

Run the FastAPI server locally (dev mode):

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Text endpoint: GET /generate/text?prompt=<your prompt>
- Audio endpoint: GET /generate/audio?prompt=<your prompt>
- Image endpoint: GET /generate/image?prompt=<your prompt>

Example (curl):

```bash
curl "http://127.0.0.1:8000/generate/text?prompt=Say+hello+world"
```

Use the example Streamlit client (`client.py`) to interact via a UI:

```bash
streamlit run client.py
```

---

## Using BentoML (recommended for long-running serving)

`bento.py` shows how model loading is moved into a persistent service so models are loaded once during service startup and reused across requests. To run BentoML locally:

Install BentoML and build & serve the service:

```bash
pip install bentoml
# Build a Bento (if using BentoML new CLI):
# bentoml build
# Serve the built bento by name (or use `bentoml serve` for a local dev flow):
bentoml serve bento:Generate
```

BentoML avoids reloading large model weights per-request and helps packaging and deploying models in containers.

---

## Notes & caveats

- These models can be large. Expect long downloads and heavy RAM usage for some models.
- If you plan to run on a GPU, ensure you install a compatible PyTorch build.
- This code is intended as a demo/developer template; before production use add proper auth, input validation, rate limiting, and monitoring.

---

## Contributing

Contributions and improvements are welcome (e.g., add tests, CI, better configuration, or packaging). Open an issue or a PR.



