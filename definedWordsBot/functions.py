from main import bot

from config import groups_id


async def forbidden_words_warning(message):                 # функция, которая предупреждает пользователя о том, что
    arguments = {'chat_name': message.chat.title,           # нельзя писать запрещенные слова и отправляет уведомление
                 'username': message.from_user.username,    # в группу "Отчет"
                 'text': message.text}

    await bot.send_message(message.chat.id,
                           text="Пожалуйста, давай не будем употреблять эти слова.",
                           reply_to_message_id=message.message_id)

    await bot.send_message(chat_id=groups_id["report_group_id"],
                           text="Название беседы: %(chat_name)s.\nПользователь: @%(username)s.\nНарушение: '%(text)s'."
                                % arguments)


async def question_forward(message):                                        # функция, которая пересылает сообщение
    await bot.forward_message(chat_id=groups_id["question_group_id"],       # в беседу "Вопросы"
                              from_chat_id=groups_id["main_group_id"],
                              message_id=message.message_id)


def if_element_in_text(text, elements):   # функция, которая ищет вхождение элементов массива в текст
    text = text.lower()
    for el in elements:
        if el in text:
            return True
    return False
