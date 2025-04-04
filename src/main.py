import uvicorn
from fastapi import FastAPI

from config import settings

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!!!"}


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.debug,
    )
