from telegram import Update, ChatMember
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7027145577:AAG0KlWZqSDQjPZPOwCgHpJDHht5aJzZxNc'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your link detection bot.')

def delete_links(update: Update, context: CallbackContext) -> None:
    message = update.message
    user_id = message.from_user.id
    chat_id = message.chat_id
    member = context.bot.get_chat_member(chat_id, user_id)
    if member and member.user and member.user.username:
        bio = member.user.description
        if bio and "http" in bio:
            message.delete()

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete_links))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
