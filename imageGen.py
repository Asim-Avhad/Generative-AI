import requests
import io
from PIL import Image

API_TOKEN = "api_token"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

prompt = input("Enter a description for the image you'd like to generate: ")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}
)

if response.status_code == 200:
    image = Image.open(io.BytesIO(response.content))
    image.save("generated_image.png")
    print("Image successfully generated and saved as 'generated_image.png'")
else:
    print(f"Error: {response.status_code}")
    print(response.text)