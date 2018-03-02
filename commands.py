# -*- coding: utf-8 -*-


def cmd_start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=""""¡Hola! Este bot te ayudará a recordar cuando vienen esos días del mes.
                     Teclee /help para más información
                     """)


def cmd_help(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='¡Hola! Este bot te ayudará a recordar cuando vienen esos días del mes.\
                     Estos son los comandos:\
                     - /time : Muestra la fecha.\
                     - /help : Muesta este mensaje de ayuda\
                     ')


def cmd_time(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Not implemented')