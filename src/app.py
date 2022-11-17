import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer


class Code(BaseModel):
    lang: str
    text: str


app = FastAPI()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "assets")
app.mount(
    "/assets", StaticFiles(directory=os.path.join(dirname, filename)), name="assets"
)

tokenizer = AutoTokenizer.from_pretrained(os.path.join(dirname, "assets/tokenizer"))
model = AutoModelForCausalLM.from_pretrained(os.path.join(dirname, "assets/model"))


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
