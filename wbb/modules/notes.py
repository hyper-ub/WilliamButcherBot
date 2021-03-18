from pyrogram import filters

from wbb import app
import database.notes as db


@app.on_message(filters.command("save") & ~filters.edited & ~filters.private)
async def save_note(_, message):
    if len(message.command) < 2 or not message.reply_to_message:
        await message.reply_text("Usage:\nReply to a text or sticker with /save [NOTE_NAME] to save it.")
    elif not message.reply_to_message.text and not message.reply_to_message.sticker:
        await message.reply_text("__**You can only save text or stickers in notes.**__")
    else:
        name = message.text.split(None, 1)[1]
        _type = "text" if message.reply_to_message.text else "sticker"
        note = {
            "type": _type,
            "data": message.reply_to_message.text.markdown if _type == "text" else message.reply_to_message.sticker.file_id
        }
        await db.save_note(message.chat.id, name, note)
        await message.reply_text(f"__**Saved note {name}.**__")


@app.on_message(filters.command("notes") & ~filters.edited & ~filters.private)
async def get_notes(_, message):
    _notes = await db.get_note_names(message.chat.id)

    if not _notes:
        await message.reply_text("Nothing to see here")
    else:
        await message.reply_text("\n".join(_notes))


@app.on_message(filters.command("get") & ~filters.edited & ~filters.private)
async def get_note(_, message):
    if len(message.command) < 2:
        await message.reply_text("**Usage**\n__/get [NOTE_NAME]__")
    else:
        name = message.text.split(None, 1)[1]
        _note = await db.get_note(message.chat.id, name)
        if not _note:
            await message.reply_text("**There are no notes in this chat matching your query.**")
        else:
            if _note["type"] == "text":
                await message.reply_text(_note["data"])
            else:
                await message.reply_sticker(_note["sticker"])
