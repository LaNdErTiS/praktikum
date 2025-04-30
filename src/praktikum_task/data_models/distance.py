"""
Определение сущности дистанция
"""

import math
from enum import Enum


class Distance(Enum):
    """
    Класс для хранения расстояний
    """

    UP_TO_TWO = 2
    UP_TO_TEN = 10
    UP_TO_THIRTY = 30
    MORE_THIRTY = math.inf
