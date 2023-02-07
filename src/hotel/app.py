from fastapi import FastAPI

app = FastAPI()


@app.get("/list_of_hotels")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
