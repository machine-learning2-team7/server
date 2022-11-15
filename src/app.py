from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-multi")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-multi")


class Code(BaseModel):
    lang: str
    text: str


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def do_predict(input: str):
    input_ids = tokenizer(input, return_tensors="pt").input_ids

    generated_ids = model.generate(input_ids, max_length=128)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)


@app.post("/predict")
def predict(code: Code):
    return do_predict(code.text)
