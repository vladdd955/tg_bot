import telebot
from telebot import types

TOKEN = '7863427596:AAEA6nw715pVFlRdPFCC9XAquCPCaCQyZVU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    location_button = types.KeyboardButton("📍 Отправить мою локацию", request_location=True)
    markup.add(location_button)

    inline_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton("🖼 Закинуть фото", url="https://images.google.com/")
    inline_markup.add(url_button)

    bot.send_message(message.chat.id, "Привет! Нажми кнопку, чтобы отправить свою геолокацию.", reply_markup=markup)
    
    bot.send_message(message.chat.id, "А также можешь загрузить фото через Google Images:", reply_markup=inline_markup)

@bot.message_handler(content_types=['location'])
def location_handler(message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.send_message(message.chat.id, f"Спасибо! 🌍\nТвоя локация:\nШирота: {lat}\nДолгота: {lon}")

@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет :) Напиши /start, чтобы отправить локацию.")
    else:
        bot.send_message(message.chat.id, "Напиши /start и нажми кнопку геолокации 📍.")

bot.polling(none_stop=True)
