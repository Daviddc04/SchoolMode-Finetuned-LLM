# SchoolMode Finetuning

My first proper experiment with finetuning LLMs. The end goal was to create a finetuned LLM which instead of just providing a direct answer which provides little educational benefit. It will just explain the process of how to get to the answer and avoid giving a direct answer creating a more useful learning experience in theory. 

Model used : **Mistral 7B model quantized to 4bit**. -> used this model as it only requires a max of around 6-7gb of VRAM when performing LORA Finetuning.

LORA -> at the moment using the default LORA rank of 8 which allows for around 1.7 M trainable parameters. However you can change the LORA rank easily by adding "--lora-rank", "16", (16 can be 1,2,8,16,512) -> for example Rank 512 on a 7B model will give you 86 Million trainable parameters

# Features:
- SchoolMode Fuses the base model with the finetuned adapter weights using LORA to provide the functionality stated above.
- SchoolMode off just uses the base Model and allows you to interact with the base model.

# Disclaimer:
This repo was an **exploratory project**. While it's functional, it likely won't see major future updates.

Instead, I’ve moved on to building:
- A full UI for automation of LoRA fine-tuning workflows
- Research into **1.58-bit quantized LLMs**, which I believe could push LLM accessibility even further
