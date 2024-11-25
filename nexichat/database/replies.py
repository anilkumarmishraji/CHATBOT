from nexichat.database import chatai
from nexichat import db

abuse_words_db = db.abuse_words_db.words
replies_cache = []
abuse_cache = []

async def load_abuse_cache():
    global abuse_cache
    abuse_cache = [entry['word'] for entry in await abuse_words_db.find().to_list(length=None)]

async def load_replies_cache():
    global replies_cache
    replies_cache = await chatai.find().to_list(length=None)
    await load_abuse_cache()
