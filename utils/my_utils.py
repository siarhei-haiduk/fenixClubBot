from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


async def print_state(message: Message, state: FSMContext):
    await message.answer(f'текущее состояние: {await state.get_state()}\nтекущее сообщение: {message.text}',
                         parse_mode='html')
