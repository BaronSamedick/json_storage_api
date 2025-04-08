import json

import redis

from config import settings

redis_client = redis.Redis(
    username=settings.redis.user,
    password=settings.redis.password,
    host=settings.redis.host,
    port=settings.redis.port
)


def store_json_to_redis(key: str, value: dict, expire: int | None = None):
    """Записать json объект в редис по ключу"""
    try:
        result = redis_client.set(key, json.dumps(value), ex=expire)
    except Exception as err:
        result = False

    return result
