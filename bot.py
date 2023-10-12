from pyrogram import Client, filters, enums
from gradio_client import Client as GClient
import os, shutil

from utils.read_params import read_secrets, read_gradio_host, read_voices

gradio = GClient(read_gradio_host())

secrets = read_secrets()
app = Client(
    "my_bot",
    api_id=secrets["API_ID"], api_hash=secrets["API_HASH"],
    bot_token=secrets["TOKEN"]
)

available_voices = read_voices()
@app.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
    await message.reply(
        "Привет!\nЯ RVC Urfu бот, "
        "переозвучиваю голосовые сообщения разными голосами\n"
        "\n"
        "Для выбора голоса введи\n"
        "`/voice <название>`\n"
        "Доступные голоса: " + ", ".join(available_voices),
    )

active_voice = ""
@app.on_message(filters.command(["voice"], prefixes=["/", "!"]))
async def voice_cmd(client, message):
    v = message.text.split()[1]
    if v in available_voices:
        global active_voice
        active_voice = available_voices[v]
        await message.reply("Выбран голос: " + active_voice)
    else:
        await message.reply("Такого голоса нет")

@app.on_message(filters.voice)
async def on_voice(client, message):
    print(active_voice)
    
    await app.download_media(message)
    await message.reply("Переозвучиваю...")
    await app.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    
    gradio.predict(active_voice, 0,0, api_name="/infer_change_voice")
    gradio.predict(0, os.path.abspath(".\\downloads"), os.path.abspath(".\\out"), [], 0, "rmvpe", "", "", 0,0,0,0,0, "ogg", api_name="/infer_convert_batch")
    
    await message.reply_voice(os.path.abspath(".\\out") + "\\" + os.listdir(".\\out")[0])
    await app.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    
    shutil.rmtree(os.path.abspath(".\\downloads"))
    shutil.rmtree(os.path.abspath(".\\out"))
app.run()