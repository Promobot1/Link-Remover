from telegram import Update, User
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7027145577:AAG0KlWZqSDQjPZPOwCgHpJDHht5aJzZxNc'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your link detection bot.')

def delete_links(update: Update, context: CallbackContext) -> None:
    message = update.message
    user = message.from_user
    if user and user.username:
        bio = get_user_bio(user, context)
        if bio and "t.me" in bio:
            message.delete()

def get_user_bio(user: User, context: CallbackContext) -> str:
    try:
        bio = context.bot.get_user_profile_photos(user.id).photos[0][0].get_file().file_path
        return bio
    except IndexError:
        return ""

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete_links))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
