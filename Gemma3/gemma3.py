from google import genai
import PIL.Image

client = genai.Client(api_key="AIzaSyDv4WNrUiNPk79n6NnmS0sjVci6WeVgrPg")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)
image = PIL.Image.open('ai_artificial intelligence_automaton_brain_electronics_icon.png')
response_img = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image?", image])

print(response_img.text)