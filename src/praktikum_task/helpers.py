from functools import wraps
from typing import Any

from praktikum_task.logger import logger


def validate_args(*expected_types: tuple):
    """
    Декоратор валидации входящих параметров функций
    """

    def decorator(func: Any):
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict[str, Any]):
            for arg, expected_type in zip(args, expected_types, strict=True):
                if not isinstance(arg, expected_type):
                    logger.error(f"Некорректное значение аргумента {arg}")
                    return None
            return func(*args, **kwargs)

        return wrapper

    return decorator
