# EsmaShop

Учебный веб-магазин на Python с использованием Flask и SQLite.

## Уязвимости проекта

В исходной версии app_vulnerable.py реализованы две учебные уязвимости:

1. SQL Injection (OWASP A03: Injection).
2. IDOR (OWASP A01: Broken Access Control).

В app.py находятся исправленные версии приложения.

## Установка

Установить необходимые библиотеки:

pip install -r requirements.txt

## Создание базы данных

Запустить:

python init_db.py

## Запуск приложения

Запустить:

python app.py

Открыть в браузере:

http://127.0.0.1:5000

## Проверка исправлений

При запущенном приложении выполнить:

python exploit_sqli.py

python exploit_idor.py

Ожидаемые результаты:

- SQL Injection не позволяет получить все товары.
- Попытка открыть чужой профиль возвращает HTTP 403.

## Структура проекта

- app.py — исправленная версия приложения.
- app_vulnerable.py — версия с уязвимостями.
- init_db.py — создание базы данных.
- exploit_sqli.py — проверка SQL Injection.
- exploit_idor.py — проверка IDOR.
- check_db.py — просмотр содержимого базы данных.
- CHANGES.txt — список исправлений.
- requirements.txt — необходимые библиотеки.