import telebot
import random
import requests
from bs4 import BeautifulSoup

TOKEN = '5865246525:AAFNALqIwaHzEB-sz0MessReKbrPVyGLcr0'
bot = telebot.TeleBot(TOKEN)

img_list = [open('funnykanye.jpg', 'rb'),
            open('frustratedkanye.jpg', 'rb'),
            open('avatarkanye.jpg', 'rb'),
            open('pofigkanye.jpg', 'rb'),
            open('seriouskanye.jpg', 'rb'),
            open('ssskanye.jpg', 'rb'),
            open('smallfacekanye.jpg', 'rb'),
            ]

url = 'https://www.goalcast.com/kanye-west-quotes/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('blockquote', class_ = 'wp-block-quote is-style-custom3')
quotes_list = []
for quote in quotes:
    quotes_list.append(quote)

@bot.message_handler(commands=["start"])
def start_communication(message):
    msg = bot.send_message(message.chat.id,
                           "Добро пожаловать, {0.first_name}! Начнем?".format(message.from_user, bot.get_me()))

@bot.message_handler(content_types=['text'])
def send_text(message):
    buttons = [
        [telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')],
        [telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')],
        [telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')],
        [telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')],
        [telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')],
        [telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')],
        [telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')],
        [telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')],
        [telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')],
        [telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')],
        [telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')],
        [telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')]
    ]
    keyboard_markup = telebot.types.InlineKeyboardMarkup(buttons)
    bot.send_message(message.chat.id, text='Ваш знак:', reply_markup=keyboard_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Овен':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Телец':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Близнецы':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Рак':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Лев':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Дева':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Весы':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Скорпион':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Стрелец':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Козерог':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Водолей':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))
    elif call.data == 'Рыбы':
        bot.send_photo(call.message.chat.id, random.choice(img_list), caption=random.choice(quotes_list))


bot.polling(none_stop=True, interval=0, timeout=45)