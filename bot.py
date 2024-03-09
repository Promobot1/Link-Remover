from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define your bot token
TOKEN = "your_bot_token"

# Define your bot's username
BOT_USERNAME = "your_bot_username"

# Define the ID of the group where the bot will operate
GROUP_ID = -1234567890  # Replace with your group's ID

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is active in this group!")

def check_bio(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    user_profile_photo = user.get_profile_photos().photos[0][0] if user.get_profile_photos().photos else None

    # Check if user has a profile photo
    if user_profile_photo:
        # Here you can implement your logic to analyze the profile photo
        # If you have a machine learning model for analysis, you can use it here

        # For demonstration purposes, let's assume any profile photo indicates a link in bio
        if user_profile_photo:
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
    dp.add_handler(MessageHandler(Filters.group & Filters.text, check_bio))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
