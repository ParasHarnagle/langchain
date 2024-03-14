import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "GOAT-AI/GOAT-70B-Storytelling"

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16  # Use bfloat16 for faster inference on supported GPUs
)

# Function to generate stories
def generate_story(prompt, max_length=500):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=5,  # Adjust based on your needs
        early_stopping=True,
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
story_prompt = "treasure hunt in a jungle"
story = generate_story(story_prompt)
print(story)