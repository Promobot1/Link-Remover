from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define your bot token
TOKEN = "7027145577:AAG0KlWZqSDQjPZPOwCgHpJDHht5aJzZxNc"

# Define your bot's username
BOT_USERNAME = "@BioLinkRemoverBot"

# Define the ID of the group where the bot will operate
GROUP_ID = -1001848459006  # Replace with your group's ID

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is active in this group!")

def check_bio_and_delete_messages(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message

    # Fetch the user's profile photos
    user_profile_photos = context.bot.get_user_profile_photos(user.id)

    if user_profile_photos.total_count > 0:
        # Assuming any profile photo indicates a link in bio
        # You can implement more sophisticated analysis here if needed
        # For example, you can use computer vision techniques to detect URLs or text in the photo

        # If user's profile photo exists, delete the message and send a warning
        message.delete()
        warning_msg = f"⚠️ Warning: {user.mention_html()} may have a link in their bio. Please check their profile."
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
