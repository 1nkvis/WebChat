from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


# Как только кто-то открывает раздел "/" => выполняется функция main_page,
# а ее результат отобразится в браузере
@app.route("/")
def main_page():
    return "Добро пожаловать в Чат 1nkvis'a!"


# Изначально у нас пустой список сообщений
# Все сообщения будет добавлять и читать из этого списка
all_messages = []


# .append() добавляет новый элемент в список all_messages.append(новый элемент)
# Аргументы - то что надо знать функции чтобы выполнить свою работу

# Функция добавления нового сообщения
def add_message(sender, text):
    # Создать новое сообщение (словарь) и добавить его в список
    new_message = {
        "name": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M")
    }
    all_messages.append(new_message)


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}  # Сообщения отобразятся в браузере в формате JSON


# HTTP-GET запрос
# /send_message?name=Mike&text=Hello
@app.route("/send_message")
def send_message():
    name = request.args.get("name")
    text = request.args.get("text")
    add_message(name, text)
    # ДЗ: Добавить проверку имени и текста и выдавать ошибку
    return "Message Sent"


@app.route("/chat")
def chat_page():
    return render_template("chat.html")


# Сохранение и загрузка сообщений из файла: Завтра

app.run(debug=True)
