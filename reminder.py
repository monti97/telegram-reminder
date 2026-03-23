import os
import sys
import re
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

# ======================
# CONFIG
# ======================

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("ERRORE: TELEGRAM_TOKEN o CHAT_ID mancanti")
    sys.exit(1)

# ======================
# NOMI (MODIFICALI QUI)
# ======================

nomi = [
    "Stefano",
    "Chiara",
    "Wash",
    "Belloandre",
    "Daniele",
    "Drago"
]

# ======================
# ESCAPE MARKDOWNV2
# ======================

def escape_md(text):
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)

# ======================
# ROTAZIONE
# ======================

mese = datetime.now().month
nome = nomi[(mese - 1) % len(nomi)]
nome = escape_md(nome)

# ======================
# MESSAGGIO (SPOILER SICURO)
# ======================

messaggio = (
    "Ehi! È arrivato il momento di sganciare!\n"
    "Altrimenti Spotify stacca la spina!\n\n"
    f"E questo mese tocca a… ||{nome}||!\n\n"
    "Congratulazioni! 🎊 🥳 🎊"
)

print("Invio messaggio:")
print(messaggio)

# ======================
# INVIO
# ======================

try:
    bot = Bot(token=TOKEN)
    bot.send_message(
        chat_id=CHAT_ID,
        text=messaggio,
        parse_mode="MarkdownV2"
    )
    print("Messaggio inviato correttamente ✅")

except TelegramError as e:
    print("ERRORE TELEGRAM:", e)
    sys.exit(2)

except Exception as e:
    print("ERRORE GENERICO:", e)
    sys.exit(3)
