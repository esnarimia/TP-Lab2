
import sqlite3

# Подключаемся к базе данных.
# Если файла database.db нет, SQLite создаст его автоматически.
connection = sqlite3.connect("database.db")

# Создаём объект для выполнения SQL-запросов.
cursor = connection.cursor()

# Создаём таблицу пользователей.
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Создаём таблицу товаров.
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Добавляем тестовых пользователей.
cursor.execute("""
INSERT OR IGNORE INTO users (id, username, password, email)
VALUES
    (1, 'Maria', 'MashkaLuchshaya2008', 'maria@esmashop.local'),
    (2, 'Sasha', 'SmartSasha2008', 'sasha@esmashop.local'),
    (3, 'Arina', 'ArinaKrutishka2008', 'arina@esmashop.local')
""")

# Добавляем товары.
cursor.execute("""
INSERT OR IGNORE INTO products (id, name, price)
VALUES
    (1, 'Laptop', 75000),
    (2, 'Smartphone', 35000),
    (3, 'Headphones', 5000),
    (4, 'Keyboard', 3000)
""")

# Сохраняем изменения.
connection.commit()

# Закрываем подключение.
connection.close()

print("База данных успешно создана!")
