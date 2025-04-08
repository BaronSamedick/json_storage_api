import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from config import settings
from router import router as api_router

app = FastAPI()
app.include_router(api_router)
Instrumentator().instrument(app).expose(app)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.debug,
    )
