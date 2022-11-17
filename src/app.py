import os

import redis
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models import Input
from src.predict import do_predict

load_dotenv()

import redis

r = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=11079,
    password=os.environ.get("REDIS_PASSWORD"),
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/predict")
def predict_wrong_method():
    return {
        "message": "You are visiting the /predict via get request, for code generation use post request instead"
    }


@app.post("/predict")
def predict(input: Input):
    text = input.text.strip()
    if r.hexists(input.lang, text):
        return r.hget(input.lang, text)
    else:
        result = do_predict(text)
        r.hset(input.lang, text, result)
        return result
