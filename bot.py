import random
import string
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "qua metti il token del bot"

def start(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=user_id, text="Benvenuto! Invia /generatepassword per ottenere una password sicura.")

def generate_password(update, context):
    user_id = update.effective_user.id
    password = generate_random_password()
    context.bot.send_message(chat_id=user_id, text=f"Ecco la tua password sicura: {password}")

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = 16
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("generatepassword", generate_password))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
