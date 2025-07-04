import os
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("./local_sd_v1_5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt: str) -> str:
    os.makedirs("generated_images", exist_ok=True)
    filename = f"{prompt.replace(' ', '_')}.png"
    path = os.path.join("generated_images", filename)
    
    image = pipe(prompt).images[0]
    image.save(path)
    return path
