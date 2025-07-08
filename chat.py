# chat.py
from mlx_lm import load, generate
from mlx_lm.models.cache import make_prompt_cache

# Load both models
base_model, base_tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")
fine_model, fine_tokenizer = load("./fused_f1_model")

base_cache = make_prompt_cache(base_model)
fine_cache = make_prompt_cache(fine_model)

def chat_with_model(prompt, education_mode=False):
    model = fine_model if education_mode else base_model
    tokenizer = fine_tokenizer if education_mode else base_tokenizer
    cache = fine_cache if education_mode else base_cache

    # Add tone adjustment if education mode is on
    if education_mode:
        prompt = (
            "You're a kind, friendly teacher for kids. "
            "Answer clearly, warmly, and use simple words.\n\n"
            f"{prompt}"
        )

    messages = [{"role": "user", "content": prompt}]
    prompt_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    output = generate(model, tokenizer, prompt=prompt_text, prompt_cache=cache)
    return output.strip()
