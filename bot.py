from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define your bot token
TOKEN = "6442848831:AAGqdJG-s_9mL9kG5aCAsuwtvgnpZzMxuPU"

# Define your bot's username
BOT_USERNAME = "@BioLinkRemoverBot"

# Define the ID of the group where the bot will operate
GROUP_ID = -1234567890  # Replace with your group's ID

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is active in this group!")

def check_bio_and_delete_messages(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message

    # Assuming any username with "http" indicates a link in bio
    if "http" in user.username:
        # Delete the message
        message.delete()
        # Send a warning message
        warning_msg = f"⚠️ Warning: {user.mention_html()} has a link in their bio. Please remove the link!"
        message.reply_html(warning_msg)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.group & Filters.text, check_bio_and_delete_messages))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
