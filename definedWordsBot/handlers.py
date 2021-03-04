from main import bot, dp
from aiogram.types import Message

from config import forbidden_words_list, groups_id, bot_username
from functions import if_element_in_text, forbidden_words_warning, question_forward


@dp.message_handler(lambda msg: if_element_in_text(msg.text, forbidden_words_list) or bot_username in msg.text,
                    content_types=['text'],
                    chat_id=groups_id["main_group_id"])
async def message_checker(message: Message):
    text = message.text
    if if_element_in_text(text, forbidden_words_list):
        await forbidden_words_warning(message)

    if bot_username in text:
        await question_forward(message)


@dp.message_handler(content_types=['text'], chat_id=groups_id["question_group_id"], is_reply=True)
async def answer_for_forwarded_question(message: Message):
    arguments = {'username_who_asked': message.reply_to_message.forward_from.username,
                 'answer': message.text}

    await bot.send_message(chat_id=groups_id["main_group_id"],
                           text="@%(username_who_asked)s, поступил ответ на ваш вопрос: %(answer)s."
                                % arguments)