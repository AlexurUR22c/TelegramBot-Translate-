# Импортируем библиотеку telebot для работы с Telegram API
import telebot
# Импортируем класс Translator из библиотеки googletrans для перевода текста
from googletrans import Translator

# Создаем объект переводчика
translator = Translator()

# Запрашиваем ввод токена бота с клавиатуры
TOKEN = input("Введите токен вашего бота: ")

# Инициализируем бота с использованием введенного токена
bot = telebot.TeleBot(TOKEN)

# Выводим сообщение об успешном вводе токена
print("Токен введен.")

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем приветственное сообщение при получении команды /start
    bot.reply_to(message, "Привет! Я бот-переводчик. Просто отправь мне текст, и я переведу его.")

# Обработчик для текстовых сообщений
@bot.message_handler(func=lambda message: True)
def translate_message(message):
    # Получаем текст сообщения
    text = message.text

    # Определяем язык текста с помощью метода detect() объекта translator
    language = translator.detect(text).lang

    # Определяем язык для перевода: если текст на английском, переводим на русский, иначе - на английский
    dest_lang = 'ru' if language == 'en' else 'en'

    # Переводим текст с использованием метода translate() объекта translator
    translated_text = translator.translate(text, dest=dest_lang).text

    # Отправляем переведенный текст пользователю
    bot.reply_to(message, translated_text)

# Выводим сообщение о о работе кода
print("Бот начал работу.")

# Запускаем бота
bot.polling()
