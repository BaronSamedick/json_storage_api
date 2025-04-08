from fastapi import APIRouter, Header
from service import store_json_to_redis

router = APIRouter()


@router.put("/objects/{key}")
def add_object_by_key(key: str, json_object: dict, expires: int | None = Header(default=None)):
    """Запись объектов в хранилище"""
    result = store_json_to_redis(key, json_object, expires)
    return {"success": result}


@router.get("/objects/{key}")
def get_object_by_id(key: int) -> None:
    """Чтение объекта из хранилища"""
    pass


@router.get("/probes/liveness")
def get_liveness_probes() -> None:
    """Проверка работоспособности"""
    pass


@router.get("/probes/readiness")
def get_readiness_probes() -> None:
    """Проверка готовности"""
    pass


@router.get("/metrics")
def get_prometheus_metrics() -> None:
    """Получение метрик"""
    pass
