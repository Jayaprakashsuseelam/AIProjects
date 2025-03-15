from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "google/gemma-3-4b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32, device_map="cpu")

# Define input text
input_text = "Explain the concept of Reinforcement Learning."

# Tokenize input
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

# Generate output
with torch.no_grad():
    output = model.generate(**inputs, max_length=100)

# Decode and print result
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
