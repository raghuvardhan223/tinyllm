from typing import Literal
from PIL import Image
from io import BytesIO
import soundfile
import numpy as np

def audio_array_to_buffer(audio_array: np.array,sample_rate: int)->BytesIO:
    buffer=BytesIO()
    soundfile.write(buffer, audio_array, sample_rate, format="wav")
    buffer.seek(0)
    return buffer
def img_to_bytes(image: Image.Image,image_format:Literal["PNG","JPEG"]="PNG")->bytes:
    buffer=BytesIO()
    image.save(buffer,format=image_format)
    return buffer.getvalue()