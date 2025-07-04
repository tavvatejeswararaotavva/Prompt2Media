from diffusers import StableDiffusionPipeline

# Load model once at startup
print("🚀 Downloading Stable Diffusion model (first time only)...")
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.save_pretrained("./local_sd_v1_5")
print("✅ Model saved locally at ./local_sd_v1_5")