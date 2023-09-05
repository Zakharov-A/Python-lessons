import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)


TOKEN = "6361652657:AAHTs5OUJcFbbeMHK_n-x3qA8D3XeZKR-v0"
MSG = "Have you programmed today, {}?"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	user_full_name = message.from_user.full_name
	logging.info(f'{user_id} {user_full_name} {time.asctime()}')
	await message.reply(f"Привет, {user_full_name}!")

	for i in range(10):
		time.sleep(60)
		await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
	executor.start_polling(dp)
