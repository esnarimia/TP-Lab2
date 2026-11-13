import os

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-esmashop-key")


# Подключение к базе данных
def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


# Главная страница
@app.route("/")
def index():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        products=products
    )


# Поиск товаров (учебная SQL Injection)
@app.route("/search")
def search():

    query = request.args.get("q", "")

    connection = get_db_connection()

    #исправление
    sql = "SELECT * FROM products WHERE name LIKE ?"
    products = connection.execute(
        sql, ("%" + query + "%",)
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        products=products,
        search_query=query
    )


# Авторизация
@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

        connection.close()

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("index"))

        else:
            error = "Неверный логин или пароль!"

    return render_template("login.html", error=error)


# Выход из аккаунта
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


# Просмотр профиля (учебная уязвимость IDOR)
@app.route("/profile/<int:user_id>")
def profile(user_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if user_id != session["user_id"]:
        return "Доступ запрещён", 403

    connection = get_db_connection()

    user = connection.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    connection.close()

    if user is None:
        return "Пользователь не найден", 404


    return render_template("profile.html", user=user)


# Запуск приложения
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
