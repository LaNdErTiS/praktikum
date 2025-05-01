# Проект
praktikum task - https://practicum-for-students.yonote.ru/share/1bbf4ba8-b941-4965-ba21-1a8c1d24fac4/doc/untitled-1UnkOsqiXq

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
source .venv/bin/activate (Linux/Mac OS) or .venv\Scripts\activate (for Windows)

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

## Выход
```sh
deactivate
```

## Ограничения
Запуск tox + pytest-cov не отображает актуальное покрытие, не дочинил.
Актуальный вывод с покрытием можно увидеть через pytest
