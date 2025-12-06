import telebot
BOT_TOKEN = "8188908206:AAHzTJ21bzkDgkXXo0tfUWauGSHQXU0tZ3M"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn đến với hệ thống bán hàng Green Globe!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Bạn vừa nhắn: {message.text}")

print("Bot dang chạy...")
bot.infinity_polling()
