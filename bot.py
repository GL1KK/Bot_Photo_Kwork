from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import logging
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images") 

TOKEN=os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет напиши число от 1 до 10 и я отправлю тебе фото")

@dp.message(lambda message: message.text)
async def send_photo(message: Message):
    if message.text.isdigit():
        num = int(message.text)
        if 0 < num <= 10:
            photo_path = os.path.join(IMAGES_DIR, f"{num}.png")
            await message.answer_photo(types.FSInputFile(photo_path))
        else: 
            await message.answer("Дипазон от 1 до 10! Повторите попытку")
    else:
        await message.answer("Введите число!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())