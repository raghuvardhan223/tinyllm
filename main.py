from fastapi import FastAPI,status,Response
from models import load_test_model, generate_text,load_audio_model, generate_audio, load_image_model,generate_image
from schemas import VoicePresets
from utils import audio_array_to_buffer,img_to_bytes
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/generate/text")
def serve_language_model_controller(prompt: str) -> str:
    pipe = load_test_model()
    output = generate_text(pipe, prompt)
    return output

@app.get("/generate/audio", responses={status.HTTP_200_OK: {"content":{"audio/wav":{}}}}, response_class=StreamingResponse)
def serve_text_to_audio_model_controller(prompt: str, preset:VoicePresets="v2/en_speaker_1"):
    processor, model=load_audio_model()
    output, sample_rate=generate_audio(processor,model,prompt,preset)
    return StreamingResponse(
        audio_array_to_buffer(output, sample_rate), media_type="audio/wav"
    )
@app.get("/generate/image",responses={status.HTTP_200_OK: {"content":{"img/png":{}}}},response_class="Response")
def serve_text_to_image_model_controller(prompt:str):
    pipe=load_image_model()
    output=generate_image(pipe, prompt)
    return Response(content=img_to_bytes(output), media_type="image/png")