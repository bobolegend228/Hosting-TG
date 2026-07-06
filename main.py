import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен берётся из переменной окружения (безопасно)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_TOKEN = 1234567890:...AAF8664380576:AAHr0j1QKuecFw9LFHsKCIQzXtR9IhkwyBY...
GAME_URL   = https://Bobokvas228.github.io/detective-cards/
# Ссылка на твою игру на GitHub Pages
GAME_URL = os.environ.get("GAME_URL", "https://твой_ник.github.io/detective-cards/")

WELCOME_TEXT = """
🕵️ *Добро пожаловать в Карточный детектив\!*

В старинной усадьбе совершено убийство\. Среди гостей — преступник\. Только вы можете его разоблачить\.

🔍 Ищите улики
🗣️ Допрашивайте подозреваемых  
👁️ Вызывайте свидетелей
⚖️ Предъявляйте обвинение

Каждое дело уникально — новые подозреваемые, новые улики, новый преступник\.

Нажмите кнопку ниже, чтобы начать расследование\:
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start — приветствие + кнопка запуска игры"""
    keyboard = [
        [InlineKeyboardButton(
            text="🕵️ Начать расследование",
            web_app=WebAppInfo(url=GAME_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=WELCOME_TEXT,
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )

async def post_init(application: Application):
    """Устанавливает Menu Button (кнопка слева от поля ввода) при старте"""
    await application.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="🕵️ Играть",
            web_app=WebAppInfo(url=GAME_URL)
        )
    )

def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
