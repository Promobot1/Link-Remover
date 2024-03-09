from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7027145577:AAG0KlWZqSDQjPZPOwCgHpJDHht5aJzZxNc'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your link detection bot.')

def delete_links(update: Update, context: CallbackContext) -> None:
    message = update.message
    user = message.from_user
    if user and user.username:
        bio = context.bot.get_user_profile_photos(user.id).photos[0][0].get_file().file_path
        if "t.me" in bio:
            message.delete()

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.bio, delete_links))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
