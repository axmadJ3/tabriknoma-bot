from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram import Router


register_router = Router()


@register_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Ру"), 
                   KeyboardButton(text="Uz")
                   ]], resize_keyboard=True)

    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!.\nTilni tanlang👇", reply_markup=keyboard)


