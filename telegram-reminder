import os
import sys
import re
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("ERRORE: variabili mancanti")
    sys.exit(1)

nomi = ["Stefano", "Chiara", "Wash", "Belloandre", "Daniele", "Drago"]

def escape_md(text):
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)

mese = datetime.now().month
nome = nomi[(mese - 1) % len(nomi)]
nome = escape_md(nome)

messaggio = (
    "Ehi! È arrivato il momento di sganciare!\n"
    "Altrimenti Spotify stacca la spina!\n\n"
    f"E questo mese tocca a… ||*{nome}*||!\n\n"
    "Congratulazioni! 🎊 🥳 🎊"
)

print(messaggio)

try:
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=messaggio, parse_mode="MarkdownV2")
    print("OK")
except TelegramError as e:
    print("ERRORE TELEGRAM:", e)
    sys.exit(2)
