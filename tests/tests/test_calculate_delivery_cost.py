"""
Тесты для модуля praktikum_task
"""

import pytest
from testlib.compare import compare_data
from testlib.logger import logger

from praktikum_task.calculate_delivery_cost import calculate_delivery_cost
from praktikum_task.const import DeliveryLoadLevel, Distance, Size


@pytest.mark.parametrize(
    "distance, size, fragile, delivery_load_level, expected_cost",
    [
        pytest.param(
            Distance.UP_TO_TWO,
            Size.BIG,
            True,
            DeliveryLoadLevel.VERY_HIGH,
            880.0,
            marks=pytest.mark.smoke,
        ),
        pytest.param(
            Distance.UP_TO_TWO,
            Size.SMALL,
            False,
            DeliveryLoadLevel.HIGH,
            400.0,
            marks=pytest.mark.smoke,
        ),
        (Distance.UP_TO_TWO, Size.BIG, True, DeliveryLoadLevel.INCREASED, 660.0),
        (Distance.UP_TO_TWO, Size.SMALL, False, DeliveryLoadLevel.DEFAULT, 400.0),
        pytest.param(
            Distance.UP_TO_TEN,
            Size.SMALL,
            True,
            DeliveryLoadLevel.DEFAULT,
            500.0,
            marks=pytest.mark.smoke,
        ),
        (Distance.UP_TO_TEN, Size.BIG, False, DeliveryLoadLevel.VERY_HIGH, 480.0),
        (Distance.UP_TO_TEN, Size.SMALL, True, DeliveryLoadLevel.HIGH, 700.0),
        pytest.param(
            Distance.UP_TO_TEN,
            Size.BIG,
            False,
            DeliveryLoadLevel.INCREASED,
            400.0,
            marks=pytest.mark.smoke,
        ),
        (Distance.UP_TO_THIRTY, Size.BIG, True, DeliveryLoadLevel.INCREASED, 840.0),
        (Distance.UP_TO_THIRTY, Size.SMALL, False, DeliveryLoadLevel.DEFAULT, 400.0),
        pytest.param(
            Distance.UP_TO_THIRTY,
            Size.BIG,
            True,
            DeliveryLoadLevel.VERY_HIGH,
            1120.0,
            marks=pytest.mark.smoke,
        ),
        (Distance.UP_TO_THIRTY, Size.SMALL, False, DeliveryLoadLevel.HIGH, 420.0),
        pytest.param(
            Distance.MORE_THIRTY,
            Size.SMALL,
            True,
            DeliveryLoadLevel.HIGH,
            None,
            marks=pytest.mark.smoke,
        ),
        (Distance.MORE_THIRTY, Size.BIG, False, DeliveryLoadLevel.INCREASED, 600.0),
        (Distance.MORE_THIRTY, Size.SMALL, True, DeliveryLoadLevel.DEFAULT, None),
        (Distance.MORE_THIRTY, Size.BIG, False, DeliveryLoadLevel.VERY_HIGH, 800.0),
    ],
    ids=[
        "distance_up_two_big_fragile_very_high",
        "distance_up_two_small_not_fragile_high",
        "distance_up_two_big_fragile_increased",
        "distance_up_two_small_not_fragile_default",
        "distance_up_ten_small_fragile_default",
        "distance_up_ten_big_not_fragile_very_high",
        "distance_up_ten_small_fragile_high",
        "distance_up_ten_big_not_fragile_encreased",
        "distance_up_thirty_big_fragile_increased",
        "distance_up_thirty_small_not_fragile_default",
        "distance_up_thirty_big_fragile_very_high",
        "distance_up_thirty_small_not_fragile_high",
        "distance_more_thirty_small_fragile_high",
        "distance_more_thirty_big_not_fragile_increased",
        "distance_more_thirty_small_fragile_default",
        "distance_more_thirty_big_not_fragile_very_high",
    ],
)
def test_logic_calculate_delivery_cost(
    distance: Distance,
    size: Size,
    fragile: bool,
    delivery_load_level: DeliveryLoadLevel,
    expected_cost: float,
) -> None:
    logger.info(
        f"Запускаемся с distance={distance}, size={size}, fragile={fragile}, delivery_load_level={delivery_load_level}"
    )
    cost = calculate_delivery_cost(distance, size, fragile, delivery_load_level)

    compare_data(cost, expected_cost, "==")


@pytest.mark.parametrize(
    "distance, size, fragile, delivery_load_level",
    [
        ("invalid_distance", Size.BIG, False, DeliveryLoadLevel.VERY_HIGH),
        (
            Distance.MORE_THIRTY,
            Size.BIG,
            "invalid_fragile",
            DeliveryLoadLevel.VERY_HIGH,
        ),
        (Distance.MORE_THIRTY, "invalid_size", False, DeliveryLoadLevel.VERY_HIGH),
        (Distance.MORE_THIRTY, Size.BIG, False, "invalid_delivery_load_level"),
    ],
    ids=[
        "invalid_distance_type",
        "invalid_fragile_type",
        "invalid_size_type",
        "invalid_delivery_load_level_type",
    ],
)
def test_invalid_type_of_params(
    distance: Distance | str,
    size: Size | str,
    fragile: bool | str,
    delivery_load_level: DeliveryLoadLevel | str,
) -> None:
    logger.info(
        f"Запускаемся с distance={distance}, size={size}, fragile={fragile}, delivery_load_level={delivery_load_level}"
    )
    result = calculate_delivery_cost(distance, size, fragile, delivery_load_level)  # type: ignore

    compare_data(result, None, "is")


@pytest.mark.parametrize(
    "test_case",
    [
        (),
        (Distance.MORE_THIRTY,),
        (
            Distance.MORE_THIRTY,
            Size.BIG,
        ),
        (Distance.MORE_THIRTY, Size.BIG, True),
        (Distance.MORE_THIRTY, Size.BIG, False, DeliveryLoadLevel.VERY_HIGH, "extra"),
    ],
    ids=[
        "miss_all",
        "miss_three_last_params",
        "miss_two_last_params",
        "miss_one_last_param",
        "extra_param",
    ],
)
def test_incorrect_number_of_params(test_case: tuple) -> None:
    logger.info("Запускаемся с пропущенными параметрами")

    with pytest.raises(ValueError):
        calculate_delivery_cost(*test_case)


def test_named_args() -> None:
    logger.info("Запускаемся с именованными параметрами")

    with pytest.raises(TypeError):
        calculate_delivery_cost(
            distance=Distance.UP_TO_THIRTY,
            size=Size.SMALL,
            fragile=False,
            delivery_load_level=DeliveryLoadLevel.HIGH,
        )
