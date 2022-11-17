import os

import requests
import telebot
from dotenv import load_dotenv

from handlers import bot


if __name__ == '__main__':
    bot.polling()
    # bot.infinity_polling()
