from mlx_lm import load, generate
from mlx_lm.models.cache import make_prompt_cache
import mlx_lm.fuse


model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

prompt = "Which f1 driver won the last race"
messages= [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True
)





cache = make_prompt_cache(model)

text = generate(model, tokenizer,prompt=prompt,prompt_cache=cache,verbose=True)

print(model)
print(dir(mlx_lm.fuse))

print(model.parameters())
