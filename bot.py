
import time
import telegram
from telegram.ext import Updater, CommandHandler
import random

TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo seu token do BotFather
CHAT_ID = "7633969366"    # ID do usuário Gerivaldo

# Lógica simulada para Bac Bo com 90% de chance (exemplo)
def gerar_aposta():
    chance = random.randint(1, 100)
    if chance <= 90:
        return "APOSTA SUGERIDA: Player ✅ (alta chance)"
    else:
        return "APOSTA SUGERIDA: Banker ⚠️ (chance menor)"

def enviar_mensagem(context):
    mensagem = gerar_aposta()
    context.bot.send_message(chat_id=CHAT_ID, text=mensagem)

def iniciar_bot():
    updater = Updater(token=TOKEN, use_context=True)
    job = updater.job_queue
    job.run_repeating(enviar_mensagem, interval=60, first=5)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    iniciar_bot()
