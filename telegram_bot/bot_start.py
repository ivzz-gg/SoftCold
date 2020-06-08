import logging
import re
import time

from peewee import DoesNotExist
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler

from db import Person
from telegram_bot.command_hendler import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD, FOURTH = range(4)
# Callback data
ONE, TWO, THREE, FOUR = range(4)
rooms_dict = {"room1": InlineKeyboardButton("room1", callback_data='room1_'),
              "room2": InlineKeyboardButton("room2", callback_data='room2_'),
              "room3": InlineKeyboardButton("room3", callback_data='room3_')}


def check_temp(temp):
    return True if 10 < temp < 30 else False


def start(update, context):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    try:
        user_access = Person.get(Person.telegram_id == user.id)
    except DoesNotExist:
        update.message.reply_text(
            text="Sorry you don't have permission",
        )
        return FIRST
    keyboard = [
        [InlineKeyboardButton("Rooms control", callback_data='manual')],
        [InlineKeyboardButton("Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        text="Choose mode. Current - Auto",
        reply_markup=reply_markup
    )

    return FIRST


def start_over(update, context):
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query

    query.answer()
    keyboard = [
        [InlineKeyboardButton("Rooms control", callback_data='manual')],
        [InlineKeyboardButton("Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Choose mode",
        reply_markup=reply_markup
    )
    return FIRST


def rooms(update, context):
    user = update.effective_chat.id
    query = update.callback_query
    user_obj = Person.get(Person.telegram_id == user)
    user_access = user_obj.rooms_access
    query.answer()
    keyboard = [[InlineKeyboardButton("back", callback_data='mods')], []]
    for room in rooms_dict.keys():
        if room in user_access:
            keyboard[1].append(rooms_dict.get(room))
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        "Rooms control",
        reply_markup=reply_markup
    )
    return FIRST


def one(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton(f"Current temp - {rooms_current_temp.get('room1')}", callback_data='room1_up'),
         InlineKeyboardButton("Switch temp", callback_data='room1_change_temp')],
        [InlineKeyboardButton("back", callback_data='manual')]
    ]
    if re.match('room1_change_temp', query.data):

        current_time = time.time()
        while True:
            try:
                temp = context.update_queue.queue[-1].message.text
                try:
                    set_temp = float(temp)
                    if not check_temp(set_temp):
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        query.edit_message_text(
                            text="Please enter in range 10 < x < 30",
                            reply_markup=reply_markup
                        )

                        return FIRST
                    rooms_temp.update({'room1': set_temp})

                except:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Please enter int or float",
                        reply_markup=reply_markup
                    )

                    return FIRST
            except:
                if current_time - time.time() == 8:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Timeout",
                        reply_markup=reply_markup
                    )

                    return FIRST
                continue

            break
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Room 1 control view",
        reply_markup=reply_markup
    )

    return FIRST


def two(update, context):
    query = update.callback_query

    keyboard = [
        [InlineKeyboardButton(f"Current temp - {rooms_current_temp.get('room2')}", callback_data='room2_up'),
         InlineKeyboardButton("Switch temp", callback_data='room2_change_temp')],
        [InlineKeyboardButton("back", callback_data='manual')]
    ]
    if re.match('room2_change_temp', query.data):

        current_time = time.time()
        while True:
            try:
                temp = context.update_queue.queue[-1].message.text
                try:
                    set_temp = float(temp)
                    if not check_temp(set_temp):
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        query.edit_message_text(
                            text="Please enter in range 10 < x < 30",
                            reply_markup=reply_markup
                        )

                        return FIRST
                    rooms_temp.update({'room1': set_temp})
                except:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Please enter int or float",
                        reply_markup=reply_markup
                    )

                    return FIRST
            except:
                if current_time - time.time() == 8:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Timeout",
                        reply_markup=reply_markup
                    )

                    return FIRST
                continue

            break
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Room 2 control view",
        reply_markup=reply_markup
    )
    return FIRST


def three(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton(f"Current temp - {rooms_current_temp.get('room3')}", callback_data='room1_up'),
         InlineKeyboardButton("Switch temp", callback_data='room3_change_temp')],
        [InlineKeyboardButton("back", callback_data='manual')]
    ]
    if re.match('room3_change_temp', query.data):

        current_time = time.time()
        while True:
            try:
                temp = context.update_queue.queue[-1].message.text
                try:
                    set_temp = float(temp)
                    if not check_temp(set_temp):
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        query.edit_message_text(
                            text="Please enter in range 10 < x < 30",
                            reply_markup=reply_markup
                        )

                        return FIRST
                    rooms_temp.update({'room1': set_temp})
                except:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Please enter int or float",
                        reply_markup=reply_markup
                    )

                    return FIRST
            except:
                if current_time - time.time() == 8:
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        text="Timeout",
                        reply_markup=reply_markup
                    )

                    return FIRST
                continue

            break
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Room 3 control view",
        reply_markup=reply_markup

    )

    return FIRST


# def sensor(update, context):
#     query = update.callback_query
#     query.answer()
#     request_sensor.update({'action': True})
#     keyboard = [[
#         InlineKeyboardButton("Back", callback_data='manual')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     ids_lamps = {'room1': range(1, 7), 'room2': range(7, 12), 'room3': range(12, 15)}
#     rooms_lamps = {'room1': [], 'room2': [], 'room3': []}
#     for i in ids_lamps.get('room1'):
#         rooms_lamps.get('room1').append(rooms_state.get(str(i)))
#     for i in ids_lamps.get('room2'):
#         rooms_lamps.get('room2').append(rooms_state.get(str(i)))
#     for i in ids_lamps.get('room3'):
#         rooms_lamps.get('room3').append(rooms_state.get(str(i)))
#
#     query.edit_message_text(
#         text=f"Room 1 status\nLamps:{rooms_lamps.get('room1')}\nSensors:{(sensor_status.get('1'))}\n"
#         f"Room 2 status\nLamps:{rooms_lamps.get('room2')}\nSensors:{sensor_status.get('2')})\n"
#         f"Room 3 status\nLamps:{rooms_lamps.get('room3')}\nSensors:{(sensor_status.get('3'), sensor_status.get('4'))}",
#         reply_markup=reply_markup
#
#     )
#
#     return FIRST


def end(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text="See you next time!"
    )
    return ConversationHandler.END


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


class Telebot:
    def start_bot(self):
        # Create the Updater and pass it your bot's token.
        self.updater = Updater("1084160074:AAGcfIVWRxXdNpzWLafBQKXV4dssd6zVmKo", use_context=True)

        dp = self.updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                FIRST: [CallbackQueryHandler(one, pattern='^' + 'room1' + '.+$'),
                        CallbackQueryHandler(two, pattern='^' + 'room2' + '.+$'),
                        CallbackQueryHandler(three, pattern='^' + 'room3' + '.+$'),
                        CallbackQueryHandler(start_over, pattern='^' + 'mods' + '$'),
                        CallbackQueryHandler(end, pattern='^' + 'exit' + '$'),
                        CallbackQueryHandler(rooms, pattern='^' + 'manual' + '$'), ],
                # CallbackQueryHandler(sensor, pattern='^' + 'status' + '$')],
                SECOND: [CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '.+$'),
                         CallbackQueryHandler(end, pattern='^' + str(TWO) + '$')],
                # THIRD: [CallbackQueryHandler]

            },
            fallbacks=[CommandHandler('start', start)]
        )

        dp.add_handler(conv_handler)

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        self.updater.start_polling()

    def stop_bot(self):
        self.updater.stop()
