# Проект
praktikum task

## Описание
Реализация функции расчёта стоимости доставки.
Автотесты написаны с использованием pytest.

## Необходимые инструменты
- python>=3.13

## Установка
```sh
git clone https://github.com/LaNdErTiS/praktikum.git
cd praktikum

python3 -m venv .venv
source .venv/bin/activate

pip install -e .
```

## Запуск смоук тестов
```sh
pytest -k smoke
```
или 
```sh
tox -c tox.ini -e smoketests
```

## Запуск всех тестов
```sh
pytest
```
или
```sh
tox -c tox.ini
```

## Ограничения
Запуск tox + pytest-cov не отображает актуальное покрытие, не дочинил.
Актуальный вывод с покрытием можно увидеть через pytest
