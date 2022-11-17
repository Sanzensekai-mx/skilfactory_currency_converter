import os
import json

import requests
import telebot
from dotenv import load_dotenv

load_dotenv(encoding='utf-8')

TOKEN = str(os.getenv("TOKEN"))

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    if message.text == '/start':
        bot.send_message(message.chat.id, text=f'Привет, {message.chat.first_name}')
    text = 'Чтобы начать рабоу введите команду боту в следующем формате:\n<имя валюты цену которой хотите узнать>' \
           ' <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>\n' \
           'Увидить список всех доступных валют: /values'
    bot.send_message(message.chat.id, text=text)


@bot.message_handler(commands=['values'])
def show_values(message: telebot.types.Message):
    with open('currencies_list.json', 'r', encoding='utf-8') as json_file:
        cur_list = json.load(json_file)
    text = 'Поддерживаемые валюты:\n'
    count_cur = 0
    len_cur_list = len(cur_list)
    while len_cur_list:
        for cur, name in list(cur_list.items()):
            if count_cur > 100:
                bot.send_message(message.chat.id, text)
                text = ''
                count_cur = 0
            text += f'{cur}    -     {name}\n'
            count_cur += 1
            len_cur_list -= 1
    bot.send_message(message.chat.id, text)
    text = 'Наиболее популярные валюты среди пользователей:\n' \
           'USD    -     Доллар США\n' \
           'EUR    -     Евро\n' \
           'BTC    -     Биткоин\n' \
           'RUB    -     Российский рубль\n'
    bot.send_message(message.chat.id, text)
