from fastapi import FastAPI
from pydantic import BaseModel
import learn as learn
import run as infer
app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/learn")
def learn_navigation(data: InputData):
    output_text = learn.main(text_input=data.text)  # Example processing: converting to uppercase
    return {"output": output_text}


@app.post("/infer")
def auto_navigate(data: InputData):
    output_text = infer.main(text_input=data.text)  # Example processing: converting to uppercase
    return {"output": output_text}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
