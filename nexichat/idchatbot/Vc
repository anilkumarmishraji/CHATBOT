from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped


@Client.on_message(filters.command("start_vc") & filters.group)
async def start_vc(client, message):
    await pytgcalls.start()
    await message.reply("Voice chat started successfully.")

@Client.on_message(filters.command("play") & filters.group)
async def play_audio(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        await message.reply("Reply to an audio file or voice message to play it.")
        return
    file_path = await message.reply_to_message.download()
    await pytgcalls.join_group_call(
        message.chat.id,
        AudioPiped(file_path)
    )
    await message.reply("Playing audio in VC.")

@Client.on_message(filters.command("stop_vc") & filters.group)
async def stop_vc(client, message):
    await pytgcalls.leave_group_call(message.chat.id)
    await message.reply("Voice chat stopped.")
