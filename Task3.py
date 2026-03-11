from fastapi import FastAPI

app = FastAPI()

# API 1: Sum of two numbers
@app.get("/sum")
def sum_numbers(a: float, b: float):
    return {"sum": a + b}

# API 2: Convert to uppercase
@app.get("/uppercase")
def uppercase(text: str):
    return {"uppercase": text.upper()}

