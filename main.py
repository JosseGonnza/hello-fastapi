from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return "<h1>HELLO WORLD</h1>"