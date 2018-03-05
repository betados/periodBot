# -*- coding: utf-8 -*-

# from models import addPeriod
from datetime import datetime


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=""""¡Hola! Este bot te ayudará a recordar cuando vienen esos días del mes.
                     Teclee /help para más información
                     """)


def cmd_help(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='¡Hola! Este bot te ayudará a recordar cuando vienen esos días del mes.\
                     Estos son los comandos:\
                     - /time : Muestra la fecha. \
                     - /set <days since your last period> : Establece tu uĺtimo periodo para recibir avisos los siguientes.\
                     - /help : Muesta este mensaje de ayuda\
                     ')


def time(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Not implemented')


def set(bot, update, args):
    print("today:", datetime.date.today())

    chat_id = update.message.chat_id
    print(chat_id, args)
    try:
        days = int(args[0])
        if days < 0:
            bot.send_message(chat_id=update.message.chat_id,
                            text='Usa cantidades positivas')
            return

        addPeriod(chat_id=update.message.chat_id, last=days, time=now)
        bot.send_message(chat_id=update.message.chat_id, text='Tu calendario se ha actualizado\n\
        Se te avisará dentro de {days} días'.format(days=28-days))

    except (IndexError, ValueError):
        bot.send_message(chat_id=update.message.chat_id,
                         text='Usage: /set <days since your last period>')


def alarm(bot, job):
    bot.send_message(chat_id=job.context, text='Te viene lo rojo')