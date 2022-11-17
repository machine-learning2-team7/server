from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-multi")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-multi")

tokenizer.save_pretrained("assets/tokenizer/")
model.save_pretrained("assets/model/")

tokenizer = AutoTokenizer.from_pretrained("src/assets/tokenizer/")
model = AutoModelForCausalLM.from_pretrained("src/assets/model/")
