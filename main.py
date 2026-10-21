import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return "<h1>HELLO WORLD</h1>"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
