from aiogram import types, Bot, Dispatcher, filters, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio
import sys
import logging
import config

dp = Dispatcher()
TOKEN = config.token


@dp.message(filters.CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"К Вашим услугам, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("К Вашим услугам!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
