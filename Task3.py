from fastapi import FastAPI, HTTPException

app = FastAPI(title="Prowiz FastAPI Assignment")

# API 1: Sum of two numbers
@app.get("/sum")
def sum_numbers(a: float, b: float):
    try:
        result = a + b
        return {
            "number1": a,
            "number2": b,
            "sum": result
        }
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid input. Please enter numeric values.")


# API 2: Convert lowercase string to uppercase
@app.get("/uppercase")
def convert_uppercase(text: str):
    if not text.islower():
        raise HTTPException(
            status_code=400,
            detail="Input must be a lowercase string."
        )

    return {
        "original_text": text,
        "uppercase_text": text.upper()
    }