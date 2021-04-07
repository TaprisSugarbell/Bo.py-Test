import random
import string
from config import Config
from telegram import ChatAction, ParseMode
from telegram.ext import ConversationHandler

# VARIABLES
INPUTNUM = 0
Token = Config.TOKEN

# Password
# def pswcommand(update, context):
#     update.message.reply_text('Parámetros\n1. Alfabeto\n2. Mayúsculas\n3. Minúsculas\n4. Números\n5. Alfanumérico\n6. Alfanumérico y Símbolos\nIngresa el número de tu elección y/o la longitud,\npor defecto "8"\nPor ejemplo 5 20, crea una contraseña alfanumérica de 20 caracteres.')
#     return INPUTNUM


def gen_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Parámetros\n1. Alfabeto\n2. Mayúsculas\n3. Minúsculas\n4. Números\n5. Alfanumérico\n6. Alfanumérico y Símbolos\nIngresa el número de tu elección y/o la longitud,\npor defecto "8"\nPor ejemplo 5 20, crea una contraseña alfanumérica de 20 caracteres.')
    return INPUTNUM


def input_gen(update, context):
    try:
        pfaw = context.args
        gn = ' '.join(pfaw)
        chat = update.message.chat
        s = ''
        afn = gn.split()
        m = int(afn[0])

        c = list(string.digits)

        for i in range(10):
            s += random.choice(c)

        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
            )
        chat.send_message(
            text=f"Tu tarjeta es: `{m}{s}`", parse_mode=ParseMode.MARKDOWN,
        )
    except:
        try:
            gen = gn
        except:
            gen = update.message.text
        chat = update.message.chat
        s = ''
        afn = gen.split()
        m = int(afn[0])

        c = list(string.digits)

        for i in range(10):
            s += random.choice(c)

        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
            )
        chat.send_message(
            text=f"Tu tarjeta es: `{m}{s}`", parse_mode=ParseMode.MARKDOWN,
        )
    return ConversationHandler.END