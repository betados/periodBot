#!/usr/bin/python3.5

import sys

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from commands import *


token = sys.argv[1]

updater = Updater(token=token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('help', cmd_help))
dispatcher.add_handler(CommandHandler('time', time, pass_args=True))
dispatcher.add_handler(CommandHandler('set', set,
                                      pass_args=True))

updater.start_polling()
