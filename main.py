from aiogram import types, Bot, Dispatcher, filters, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio
import sys
import logging
import config
import json

dp = Dispatcher()
TOKEN = config.token


@dp.message(filters.Command("start"))
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"К Вашим услугам, {html.bold(message.from_user.full_name)}!")


@dp.message(filters.Command("new"))
async def new_word_handler(message: types.Message) -> None:
    f = 0
    text = message.text
    text = text[5:]
    f = open('word_dict.json', 'r+', encoding='utf-8')
    data = json.load(f)
    for i in data['words']:
        if text in i['word']:
            f = 1
            break
    if f:
        await message.answer("Такое слово уже есть в словаре")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
