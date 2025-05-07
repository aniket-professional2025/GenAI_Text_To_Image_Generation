# Importing required Packages
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch
from huggingface_hub import HfFolder, cached_download, hf_hub_download, model_info

# Creating the two model paths
model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"
model_id2 = "stabilityai/stable-diffusion-xl-base-1.0"

# Build the pipe object
pipe = StableDiffusionPipeline.from_pretrained(model_id1, torch_dtype = torch.float16, use_safetensors = True)
pipe = pipe.to("cuda")

# Define a function to generate an image
def generate_image(prompt, pipeline=pipe, width = 512, height = 512):
    image = pipeline(prompt, width = width, height = height).images[0]
    return image