import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from routers import register_routers


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(register_routers())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
