"""
Определение различных служебных функций
"""

from collections.abc import Callable
from functools import wraps
from typing import Any

from praktikum_task.logger import logger


def validate_args(*expected_types) -> Any:
    """
    :description: Декоратор валидации входящих параметров функций

    :param *expected_types: Ожидаемые типы аргументов

    :return: Декоратор, который проверяет типы аргументов
    """

    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict[str, Any]):
            for arg, expected_type in zip(args, expected_types, strict=True):
                if not isinstance(arg, expected_type):
                    logger.error(f"Некорректное значение аргумента {arg}")
                    return None
            return func(*args, **kwargs)

        return wrapper

    return decorator


def validate_no_named_args(func: Callable) -> Any:
    """
    :description: Декоратор валидации именованные параметров функций

    :param func: Ожидаемая функция

    :return: Декоратор, который проверяет наличие именованных аргументов
    """

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict[str, Any]):
        if kwargs:
            raise TypeError(f"{func.__name__} не принимает именованные аргументы")
        return func(*args, **kwargs)

    return wrapper
