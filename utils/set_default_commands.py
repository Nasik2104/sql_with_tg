from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("get_user_by_id", "Пошут по айді"),
            types.BotCommand("get_user_by_name", "Пошук за ім'ям"),
            types.BotCommand("add_me", "Додати мене"),
            types.BotCommand("remove_me", "Видалити мене"),
            types.BotCommand("update", "Оновити дані")

        ]
    )
