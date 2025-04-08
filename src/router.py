from fastapi import APIRouter, Header
from pydantic import Json

router = APIRouter()


@router.put("/objects/{key}")
def add_object_by_key(key: int, json_object: Json, expires: int | None = Header(default=None)):
    """Запись объектов в хранилище"""
    pass


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
