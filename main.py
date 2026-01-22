python
import os
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Получаем токен
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ ОШИБКА: BOT_TOKEN не установлен!")
    logger.info("💡 Установите переменную BOT_TOKEN в Railway:")
    logger.info("   1. Зайдите в проект на Railway")
    logger.info("   2. Вкладка 'Variables'")
    logger.info("   3. Добавьте BOT_TOKEN=ваш_токен")
    sys.exit(1)

# Инициализация бота
try:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    logger.info("✅ Бот инициализирован успешно!")
except Exception as e:
    logger.error(f"❌ Ошибка инициализации бота: {e}")
    sys.exit(1)

# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🤖 Бот работает на Railway 24/7!")

# Ответ на любое сообщение
@dp.message()
async def echo(message: Message):
    await message.answer(f"📝 Вы написали: {message.text}")

# Команда /status
@dp.message(Command("status"))
async def status_command(message: Message):
    await message.answer("✅ Бот работает в облаке Railway!")

# Запуск бота с обработкой ошибок
async def main():
    try:
        logger.info("=" * 50)
        logger.info("🚀 ЗАПУСК ТЕЛЕГРАМ БОТА")
        logger.info("📍 Хостинг: Railway.app")
        logger.info(f"🤖 Токен: {'Установлен' if BOT_TOKEN else 'НЕ УСТАНОВЛЕН!'}")
        logger.info("=" * 50)
        
        if not BOT_TOKEN:
            logger.error("❌ КРИТИЧЕСКАЯ ОШИБКА: BOT_TOKEN не найден!")
            return
        
        logger.info("🔄 Начинаю polling...")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Ошибка запуска бота: {e}")
    finally:
        logger.info("🛑 Бот остановлен")

# Точка входа
if __name__ == "__main__":
    # Для Railway важно использовать asyncio.run()
    asyncio.run(main())
