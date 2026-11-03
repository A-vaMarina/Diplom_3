## Задание 3: Автотесты для UI сервиса Stellar Burgers

Сервис Stellar Burgers: https://stellarburgers.education-services.ru/

UI-автотесты реализованы с использованием паттерна **Page Object Model**, фреймворка
**pytest** и отчётов **Allure**.

## Стек

- Python 3
- Selenium WebDriver
- pytest + параметризация
- Allure (allure-pytest)
- Браузеры: **Mozilla Firefox**, **Google Chrome**

## Что покрыто тестами:
**Проверка основной функциональности** — `tests/test_basic.py`
- переход по клику на «Конструктор»;
- переход по клику на раздел «Лента заказов»;
- если кликнуть на ингредиент, появится всплывающее окно с деталями;
- всплывающее окно закрывается кликом по крестику;
- при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.

**Раздел «Лента заказов»** — `tests/test_order_feed.py`
- при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
- при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
- после оформления заказа его номер появляется в разделе «В работе».

## Установка

Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Запуск тестов

Запуск всех тестов в **обоих браузерах** (Chrome и Firefox):

```bash
pytest
```

Запуск конкретного файла:

```bash
pytest -v tests/test_basic.py
```
```bash
pytest -v tests/test_order_feed.py
```

Запуск только отдельного теста, например:

```bash
pytest tests/test_basic.py::TestBasicFunctionality::test_ingredient_modal_opens -v
```

Запуск в headless-режиме (без открытия окна браузера):

```bash
pytest --headless
```
## Запуск тестов в конкретном браузере

Запуск только в Chrome:
```bash
pytest -k chrome
```
Запуск только в Firefox:
```bash
pytest -k firefox
```

## Формирование Allure-отчёта

1. Прогоните тесты со сбором результатов Allure:

   ```bash
   pytest -v --alluredir=allure_results
   ```
   ```bash
   pytest tests/test_basic.py -v --alluredir=allure_results
   ```
   ```bash
   pytest tests/test_order_feed.py -v --alluredir=allure_results
   ```

2. Сгенерируйте и откройте HTML-отчёт (требуется установленный
   [Allure Commandline](https://allurereport.org/docs/gettingstarted-installation/)):

   ```bash
   allure serve allure_results
   ```

Отчёт содержит группировку тестов по epic/feature/story и шаги выполнения
(`allure.step`).
