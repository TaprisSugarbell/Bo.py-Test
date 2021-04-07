from modles.gen import *
from modles.pytb import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler,  CallbackQueryHandler,ConversationHandler, MessageHandler, Filters


def start(update, context):
    update.message.reply_text(
        text='Hola bienvenido a Bopy\n/gen - Genera tarjeta\n/pytb - Descargar Video',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Descargar Video', callback_data='pytb')],
            [InlineKeyboardButton(text='Generador de tarjeta', callback_data='gen')],
            [InlineKeyboardButton(
                text='Repositorio', url='https://github.com/TaprisSugarbell/Bo.py-Test/tree/main')],
        ])
    )


if __name__ == '__main__':
    updater = Updater(token=Token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    # Pytube
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('pytb', pytbcommand),
                      CallbackQueryHandler(pattern='pytb', callback=pytb_callback_handler)],
        states={INPUTpy: [MessageHandler(Filters.text, input_pytb)]},
        fallbacks=[]))

    # Random Gen
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('gen', input_gen),
                      CallbackQueryHandler(pattern='gen', callback=gen_callback_handler)],
        states={INPUTNUM: [MessageHandler(Filters.text, input_gen)]},
        fallbacks=[]))

    # add handler
    updater.start_polling()
    updater.idle()


