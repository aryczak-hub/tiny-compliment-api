from fastapi import FastAPI
import random

app = FastAPI()

compliments = [
    "you have excellent taste in learning by doing",
    "you make difficult things feel manageable",
    "you ask the right questions",
    "you have strong focus",
    "you learn fast when you build"
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tiny Compliment API"}

@app.get("/compliment")
def get_compliment():
    return {"message": random.choice(compliments)}

@app.get("/compliment/{name}")
def get_personal_compliment(name: str):
    return {"message": f"{name}, {random.choice(compliments)}."}