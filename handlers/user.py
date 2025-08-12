from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from config.config import Config, load_config
from google import genai
from aiogram.utils.text_decorations import html, html_decoration

router = Router()
config : Config = load_config()
client = genai.Client(api_key=config.gemini.token)


def normalized_response(text,max_lenght = 4000) -> list:
    return [text[i:i + max_lenght] for i in range(0,len(text),max_lenght)]


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello I'm bot which is powered by Gemini 2.5 Flash""!\n"
                         "What do you want to learn today?"
                         )


@router.message(Command(commands='help'))
async def process_help(message: Message):
    await message.answer('Just send me a message with your question and wait a few seconds')


@router.message()
async def gemini_answer(message: Message):
    await message.reply('Generating response...')
    response = client.models.generate_content(
            model="gemini-2.5-flash", contents = message.text
        )
    slice_response = normalized_response(html.escape(response.text)) #html.escape is needed to change (<, > и &.") on safe symbols
    for chunk in slice_response:
        await message.answer(chunk)