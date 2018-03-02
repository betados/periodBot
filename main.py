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

dispatcher.add_handler(CommandHandler('start', cmd_start))
dispatcher.add_handler(CommandHandler('help', cmd_help))
dispatcher.add_handler(CommandHandler('time', cmd_time))

updater.start_polling()
