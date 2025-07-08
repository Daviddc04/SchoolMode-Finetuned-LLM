# finetune_and_fuse.py

import subprocess
from mlx_lm import load, generate
from mlx_lm.models.cache import make_prompt_cache

# === Configuration ===
BASE_MODEL = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
DATA_DIR = "./data"
ADAPTER_SAVE_PATH = "./adapters"
FUSED_MODEL_SAVE_PATH = "./fused_f1_model"

# === Fine-tuning using the CLI command as suggested by mlx-lm ===
def finetune():
    print("Starting LoRA fine-tuning via subprocess...")
    command = [
        "mlx_lm.lora",
        "--model", BASE_MODEL,
        "--train",
        "--data", DATA_DIR,
        "--iters", "300",
        "--batch-size", "8",
        "--learning-rate", "1e-5"
    ]
    subprocess.run(command, check=True)
    print("Finished fine-tuning.")

# === Fuse the adapter into the model using CLI ===
def fuse():
    print("Fusing adapter weights into base model using CLI...")
    command = [
        "mlx_lm.fuse",
        "--model", BASE_MODEL,
        "--adapter-path", ADAPTER_SAVE_PATH,
        "--save-path", FUSED_MODEL_SAVE_PATH
    ]
    subprocess.run(command, check=True)
    print("Fusion complete. Fused model saved to:", FUSED_MODEL_SAVE_PATH)

# === Generate with fused model ===
def generate_output():
    print("Loading fused model for generation...")
    model, tokenizer = load(FUSED_MODEL_SAVE_PATH)
    questions = [
        "Who won the last F1 race?",
        "Winner of the last F1 Grand Prix?",
        "Which F1 driver won the most recent race?"
    ]
    for question in questions:
        print(f"\nPrompt: {question}")
        messages = [{"role": "user", "content": question}]
        prompt_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
        cache = make_prompt_cache(model)
        response = generate(model, tokenizer, prompt=prompt_text, prompt_cache=cache, verbose=True)
        print("Response:", response)

if __name__ == "__main__":
    finetune()
    fuse()
    generate_output()
