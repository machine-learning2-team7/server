from transformers import AutoModelForCausalLM, AutoTokenizer

from src.constants import model_path, tokenizer_path

tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
model = AutoModelForCausalLM.from_pretrained(model_path)


def do_predict(input: str):
    input_ids = tokenizer(input, return_tensors="pt").input_ids

    generated_ids = model.generate(input_ids, max_length=128)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)
