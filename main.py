import telebot
import os
import random
from bot_logic import article, fact

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8780823348:AAG9m0Ij_JyEIjGdZ4MPKrvikVIGCaGPBDw")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /article, /mem или /facts")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Ну что начнем изучать глобальное потепление или посмеемся?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Всё, давай! Заходи в свободное время!")

@bot.message_handler(commands=['article'])
def send_article(message):  # Переименовал функцию
    articles = article()
    bot.reply_to(message, articles)  # Убрал фигурные скобки

@bot.message_handler(commands=['fact'])
def send_fact(message):  # Переименовал функцию
    facts = fact()
    bot.reply_to(message, facts)  # Убрал фигурные скобки

@bot.message_handler(commands=['mem'])
def send_random_mem(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  # Исправил путь к файлу
        bot.send_photo(message.chat.id, f)
        
bot.polling()