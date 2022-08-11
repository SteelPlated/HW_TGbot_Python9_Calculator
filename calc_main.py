from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from calc import*

updater = Updater(token='5572182114:AAEGaREq4XiSrXJdUjxRNteu2Bd0pBD4VUM')
updater.dispatcher.add_handler(CommandHandler('sum', summa_command))
updater.dispatcher.add_handler(CommandHandler('sub', subtraction_command))
updater.dispatcher.add_handler(CommandHandler('seg', segmentation_command))
updater.dispatcher.add_handler(CommandHandler('mult', multiplication_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

# В конце |||
updater.start_polling()
updater.idle()
