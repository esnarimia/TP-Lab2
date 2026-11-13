
import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect("database.db")

# Получаем список таблиц
cursor = connection.cursor()

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()

print("ТАБЛИЦЫ В БАЗЕ ДАННЫХ:")

for table in tables:
    print("-", table[0])

# Показываем содержимое таблицы users
print("\nПОЛЬЗОВАТЕЛИ:")

cursor.execute("SELECT * FROM users")

for user in cursor.fetchall():
    print(user)

# Показываем содержимое таблицы products
print("\nТОВАРЫ:")

cursor.execute("SELECT * FROM products")

for product in cursor.fetchall():
    print(product)

# Закрываем соединение
connection.close()
