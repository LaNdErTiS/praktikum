"""
Определение всех констант для расчета стоимости доставки
"""

from praktikum_task.data_models.delivery_load import DeliveryLoadLevel
from praktikum_task.data_models.distance import Distance
from praktikum_task.data_models.size import Size

DISTANCE_COST_MAP: dict[Distance | int, int] = {
    Distance.UP_TO_TWO: 50,
    Distance.UP_TO_TEN: 100,
    Distance.UP_TO_THIRTY: 200,
    Distance.MORE_THIRTY: 300,
}

SIZE_COST_MAP: dict[Size, int] = {
    Size.BIG: 200,
    Size.SMALL: 100,
}

FRAGILE_COST = 300

DELIVERY_LOAD_LEVEL_COST_MAP: dict[DeliveryLoadLevel, float] = {
    DeliveryLoadLevel.DEFAULT: 1.0,
    DeliveryLoadLevel.INCREASED: 1.2,
    DeliveryLoadLevel.HIGH: 1.4,
    DeliveryLoadLevel.VERY_HIGH: 1.6,
}

MIN_SUM_DELIVERY_COST = 400
