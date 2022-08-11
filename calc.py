from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def summa_command(update: Update, context: CallbackContext):
    msg=update.message.text
    print(msg)
    items=msg.split()
    x=int(items[1])
    y=int(items[2])
    update.message.reply_text(f'{x}+{y}={x+y}')
    
def subtraction_command(update: Update, context: CallbackContext):
    msg=update.message.text
    print(msg)
    items=msg.split()
    x=int(items[1])
    y=int(items[2])
    update.message.reply_text(f'{x}-{y}={x-y}')
    
def segmentation_command(update: Update, context: CallbackContext):
    msg=update.message.text
    print(msg)
    items=msg.split()
    x=int(items[1])
    y=int(items[2])
    update.message.reply_text(f'{x}/{y}={x/y}')
    
def multiplication_command(update: Update, context: CallbackContext):
    msg=update.message.text
    print(msg)
    items=msg.split()
    x=int(items[1])
    y=int(items[2])
    update.message.reply_text(f'{x}*{y}={x*y}')
    
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/sum - сложение\n/sub-вычитание\n/seg-деление\n/mult-умножение')