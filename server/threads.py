from telegram_bot.bot_start import Telebot
from server.start_server import start_server
import threading

bot = Telebot()

p1 = threading.Thread(target=bot.start_bot)
p2 = threading.Thread(target=start_server)


def threads_start():
    p1.start()
    p2.start()


def threads_stop():
    bot.stop_bot()
