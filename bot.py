import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize your Telegram bot's API token here
API_TOKEN = '6018523955:AAElFviMJuGHCVDFxLllYqfrGWCZj9MmhNo'

# Initialize a list to store the orders
orders = []

prices = [100,10,11,12,13,14,15,16,17,18]

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to our store! Please find the items currently available in our store with their prices and order them by entering their serial number and the quantity one by one like "4 2". Once you are finished ordering write the /done command')
    context.bot.send_message(chat_id=update.effective_chat.id, text='1) Milk $100')
    context.bot.send_message(chat_id=update.effective_chat.id, text='2) Bread $10')
    context.bot.send_message(chat_id=update.effective_chat.id, text='3) Chips $11')
    context.bot.send_message(chat_id=update.effective_chat.id, text='4) Chocolate $12')
    context.bot.send_message(chat_id=update.effective_chat.id, text='5) Eggs $13')
    context.bot.send_message(chat_id=update.effective_chat.id, text='6) Cheese $14')
    context.bot.send_message(chat_id=update.effective_chat.id, text='7) Cake $15')
    context.bot.send_message(chat_id=update.effective_chat.id, text='8) Cream $16')
    context.bot.send_message(chat_id=update.effective_chat.id, text='9) Paneer $17')
    context.bot.send_message(chat_id=update.effective_chat.id, text='10) Chewing Gum $18')



total =0
# Define a function to handle the user's order
def order(update, context):
    global total
    text = update.message.text
    items = text.split(' ')
    total+=int(items[1])*prices[int(items[0])-1]
    context.bot.send_message(chat_id=update.effective_chat.id, text='Got it! We have received your order for the following items and the total till now is :\n\n' + str(total))

# Define a function to handle the /done command
def done(update, context):
    global total
    context.bot.send_message(chat_id=update.effective_chat.id, text='Thank you for your order! Your order has been placed and will be delivered soon.The order total is '+ str(total))
    # Reset the orders list
    orders.clear()

# Define a function to handle unknown commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Please send me the list of items you want to order, one item per line.")

# Set up the Telegram bot
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Set up handlers for the /start and /done commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("done", done))

    # Set up a handler for user messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, order))

    # Set up a handler for unknown commands
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



