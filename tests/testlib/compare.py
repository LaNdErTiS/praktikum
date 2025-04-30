from typing import Any

from testlib.logger import logger


def compare_data(data1: Any, data2: Any, operator: str = "==") -> None:
    """
    :description: Функция сравнения двх объектов
    :param data1: Первый объект для сравнения
    :param data2: Второй объект для сравнения
    :param operator: Оператор сравнения (по умолчанию "=")

    :return: None
    """
    logger.info(f"Сравниваем {data1} с {data2} используя {operator}")

    if operator == "==":
        assert data1 == data2
    elif operator == "is":
        assert data1 is data2
