from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your bot token
bot_token = 'YOUR_BOT_TOKEN'

# Create the bot
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)

# Define the message handler
def message_handler(update: Update, context: CallbackContext):
    user_bio = update.effective_user.bio
    if 'http://' in user_bio or 'https://' in user_bio:
        # Delete the message and warn the user
        update.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Please remove the link from your bio to participate in the group.",
                                 parse_mode=ParseMode.MARKDOWN)

# Add the message handler to the dispatcher
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

# Start the bot
updater.start_polling()
updater.idle()
