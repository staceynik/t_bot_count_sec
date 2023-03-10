import ptbot
import random
import os
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TG_CHAT_ID = os.environ.get('TG_CHAT_ID')
bot = ptbot.Bot(TG_TOKEN)

def choose():
    answers = ("да", "нет", "это возможно")
    choice = random.choice(answers)
    message = "Думаю, {}".format(choice)
    bot.send_message(TG_CHAT_ID, message)
    print("Что сюда писать???") # <-- поменяли здесь

choose()