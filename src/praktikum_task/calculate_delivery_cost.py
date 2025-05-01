"""
Описание модуля подсчета стоимости доставки

Здесь хранится основная функция расчета стоимости доставки в зависимости от расстояния,
размера груза, хрупкости и уровня загрузки
"""

from praktikum_task.const import (
    DELIVERY_LOAD_LEVEL_COST_MAP,
    DISTANCE_COST_MAP,
    FRAGILE_COST,
    MIN_SUM_DELIVERY_COST,
    SIZE_COST_MAP,
    DeliveryLoadLevel,
    Distance,
    Size,
)
from praktikum_task.helpers import validate_args, validate_no_named_args
from praktikum_task.logger import logger


@validate_no_named_args
@validate_args(Distance, Size, bool, DeliveryLoadLevel)
def calculate_delivery_cost(
    distance: Distance,
    size: Size,
    fragile: bool,
    delivery_load_level: DeliveryLoadLevel,
) -> float | None:
    """
    :description: Расчёт стоимости доставки в зависимости от расстояния, размера груза,
    хрупкости и уровня загрузки

    :param distance: Расстояние доставки
    :param size: Размер груза
    :param fragile: Является ли груз хрупким
    :param delivery_load_level: Уровень загрузки

    :return: Стоимость доставки, округленная до сотен. Если входные параметры некорректны,
    возвращает None как сигнал невозможности расчёта
    """

    # Расчёт стоимости по расстоянию
    distance_cost: float = DISTANCE_COST_MAP[distance]
    logger.debug("Стоимость доставки по расстоянию: %f", distance_cost)

    # Расчёт стоимости по габаритам
    size_cost = SIZE_COST_MAP[size]
    logger.debug("Стоимость доставки по габаритам: %f", size_cost)

    # Расчёт стоимости по хрупкости
    fragile_cost = FRAGILE_COST if fragile else 0
    logger.debug("Стоимость доставки по хрупкости: %f", fragile_cost)

    # Проверка на хрупкость и большое расстояние
    if fragile and distance == Distance.MORE_THIRTY:
        logger.warning("Невозможно доставить хрупкий груз на расстояние более 30 км")
        return None

    # Суммируем стоимость
    total_cost = distance_cost + size_cost + fragile_cost
    logger.debug("Суммарная стоимость доставки: %f", total_cost)

    # Умножаем на коэффициент загруженности
    total_cost *= DELIVERY_LOAD_LEVEL_COST_MAP[delivery_load_level]
    logger.debug("Стоимость доставки с учётом загруженности: %f", total_cost)

    # Проверка на минимальную стоимость
    if total_cost < MIN_SUM_DELIVERY_COST:
        total_cost = MIN_SUM_DELIVERY_COST

    rounded_total_cost = round(total_cost, 2)
    logger.debug("Финальная стоимость доставки: %f", rounded_total_cost)

    return rounded_total_cost
