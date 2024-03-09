from telegram.ext import Updater, MessageHandler, Filters
from telegram import Bot, ParseMode

TOKEN = 'your_bot_token'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def check_bio_and_delete_messages(update, context):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    message_id = update.effective_message.message_id
    
    # Check the user's bio for a link
    user_bio = context.bot.get_chat_member(chat_id, user_id).user.bio
    if 'http' in user_bio:
        # Delete the message
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        # Send a warning message
        warning_message = f"@{update.effective_user.username}, your message has been deleted because your bio contains a link."
        context.bot.send_message(chat_id=chat_id, text=warning_message, parse_mode=ParseMode.MARKDOWN)

# Add a message handler
message_handler = MessageHandler(Filters.text & (~Filters.command), check_bio_and_delete_messages)
dispatcher.add_handler(message_handler)

updater.start_polling()
