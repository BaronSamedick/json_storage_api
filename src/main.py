import redis
import uvicorn
from fastapi import FastAPI

from config import settings
from router import router as api_router

app = FastAPI()
app.include_router(api_router)

redis_client = redis.Redis(
    username=settings.redis.user,
    password=settings.redis.password,
    host=settings.redis.host,
    port=settings.redis.port
)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.debug,
    )
