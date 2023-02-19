from fastapi import FastAPI

from . import core

app = FastAPI()

operations = {
    "add": core.add,
    "subtract": core.subtract,
    "multiply": core.multiply,
    "divide": core.divide,
}


@app.get("/{op}")
async def root(op: str, x: float, y: float):
    operation = operations[op]
    result = operation(x, y)
    return {"op": op, "x": x, "y": y, "result": result}
