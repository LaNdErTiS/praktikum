"""
Определение сущности уровней загрузки
"""

from enum import Enum


class DeliveryLoadLevel(Enum):
    """
    Класс для хранения уровней загрузки
    """

    DEFAULT = "default"
    INCREASED = "increased"
    HIGH = "high"
    VERY_HIGH = "very_high"
