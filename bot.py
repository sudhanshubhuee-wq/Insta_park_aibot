import telebot
import random
import os

TOKEN = os.envi(8680351427:AAGRUQkKcuZdPdsxl7XdoWa4vmkLK_mlFcs)
bot = telebot.TeleBot(8680351427:AAGRUQkKcuZdPdsxl7XdoWa4vmkLK_mlFcs)

bios = [
"🔥 Dream big, hustle harder 💼",
"🌍 Travel | Create | Inspire ✨",
"📸 Capturing moments daily"
]

captions = [
"New day, new vibe ✨",
"Stay real, stay you 💯",
"Making memories ❤️"
]

hashtags = [
"#instagood #viral #reels",
"#trending #explorepage #love",
"#photography #lifestyle #india"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome!\nType:\nbio\ncaption\nhashtag")

@bot.message_handler(func=lambda message: True)
def generate(message):
    text = message.text.lower()
    if text == "bio":
        bot.reply_to(message, random.choice(bios))
    elif text == "caption":
        bot.reply_to(message, random.choice(captions))
    elif text == "hashtag":
        bot.reply_to(message, random.choice(hashtags))
    else:
        bot.reply_to(message, "❌ Type bio / caption / hashtag")

bot.polling()
