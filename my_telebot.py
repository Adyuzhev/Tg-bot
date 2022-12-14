from deeppavlov import build_model, train_model
from aiogram import Bot, Dispatcher, executor, types
import logging
import json

import sqlite3 as sql

with open('token.json') as f:
    config = json.load(f)

TOKEN = config['token']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

question_writer = logging.getLogger('question_writer')
question_writer.setLevel(logging.DEBUG)
fh = logging.FileHandler('NewQuestions.csv')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)
question_writer.addHandler(fh)

#model = train_model('./tfidf_autofaq.json')

model = build_model('./tfidf_autofaq.json')


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.answer(f"Здравствуйте, {user_full_name}, здесь Вы можете задать интересующие вас вопросы о поступлении в магиратуру!")


@dp.message_handler(commands='help')
async def help_handler(message: types.Message):
    await message.answer("Задайте интересующий Вас вопрос")


@dp.message_handler()
async def model_handler(message: types.Message):
    result = model([message.text])
    question_writer.debug('"' + message.text + '","' +
                          result[0][0] + '","' + str(result[1][0]) + '"')

    con = sql.connect("questions.db")
    cur = con.cursor()
    cur.execute("insert into questions(question,answer,score) values (?,?,?)",
                (message.text, result[0][0], float(result[1][0])))
    con.commit()
    print('"' + message.text + '","' + result[0][0] + '"')
    print("saved")
    if result[1][0] < 0.04:
        await message.answer("Уточните вопрос")
    else:
        await message.answer(result[0][0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
