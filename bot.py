import time
import telebot

# Wklej tutaj token od @BotFather
TOKEN = "8963049868:AAF6BXRhFsYoPk61BsRQqhqnYOIzVbpp8rk"
bot = telebot.TeleBot(TOKEN)

# Twój adres lokalny (ten sam, przez który wchodzisz z telefonu na Wi-Fi)
APP_LINK = "http://127.0.0.1:5500/index.html"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    
    # 1. Wysyłamy wiadomość z linkiem
    msg = bot.send_message(
        chat_id, 
        f"🟢 **SYSTEM OPERACYJNY AKTYWNY**\n\nKliknij poniższy link, aby uzyskać dostęp do terminala:\n{APP_LINK}\n\n⚠️ *Ta wiadomość ulegnie samozniszczeniu za 10 sekund ze względów bezpieczeństwa.*",
        parse_mode="Markdown"
    )
    
    # 2. Odliczamy 10 sekund w tle
    time.sleep(10)
    
    # 3. Usuwamy wiadomość
    try:
        bot.delete_message(chat_id, msg.message_id)
    except Exception as e:
        print("Nie udało się usunąć wiadomości:", e)

print("Bot Telegrama został uruchomiony...")
bot.infinity_polling()