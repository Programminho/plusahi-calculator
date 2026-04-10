import telebot
import os
from flask import Flask
from threading import Thread

# --- Добавь этот блок ---
app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ------------------------








import telebot

bot = telebot.TeleBot ('8753456206:AAHQt0AK8bCUItVNU4ETbaGzJ-yh0g75F64')
# Команда /start
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = (
        "Салам! Это PlusAhiCalculator. 🧮\n\n"
        "Я умею только одно: складывать два числа.\n"
        "Пришли мне их через пробел (например: 10 15)."
    )
    bot.send_message(message.chat.id, welcome_text)

# Основная логика вычислений
@bot.message_handler(func=lambda message: True)
def handle_calc(message):
    # Убираем лишние пробелы по краям и делим сообщение
    parts = message.text.strip().split()

    # Проверка: должно быть строго два элемента
    if len(parts) != 2:
        bot.reply_to(message, "так нельзя")
        return

    try:
        # Пытаемся превратить ввод в числа
        # Используем float, чтобы можно было складывать и 5.5, и 10
        num1 = float(parts[0].replace(',', '.')) # заменяем запятую на точку на всякий случай
        num2 = float(parts[1].replace(',', '.'))

        # Считаем сумму
        total = num1 + num2

        # Если число целое (например, 25.0), убираем хвост, чтобы было красиво (25)
        if total.is_integer():
            total = int(total)

        # Отправляем ответ
        bot.reply_to(message, f"Сумма: {total}")

    except ValueError:
        # Если ввели буквы, знаки или любой другой мусор
        bot.reply_to(message, "так нельзя")

# Запуск бота


if __name__ == "__main__":
    keep_alive() # <--- Обязательно добавь это перед polling
    print("Бот запущен!")
    bot.polling(none_stop=True)
