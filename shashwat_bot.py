import telebot
from telebot import types

# BotFather से मिला हुआ API Token डालें
API_KEY = '8179484671:AAGF2Wr4FVmmpIK9R3ejdXSum1Asdom_mLA'  # <-- यहाँ अपना BotFather वाला API token डालें
bot = telebot.TeleBot(API_KEY)

# /start command
@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 
        "🙏 नमस्ते! मैं Shashwat का Educational Bot हूँ।\n"
        "आपको यहाँ मिलेगा:\n📘 Books, 📄 Notes, 📑 Papers, 🧪 Test, 🗣️ English Speaking, और बहुत कुछ!\n\n"
        "⬇ नीचे Menu से अपना विकल्प चुनें या Commands इस्तेमाल करें।"
    )
    main_menu(message)

# Menu with buttons
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b1 = types.KeyboardButton("📚 PDF Resources")
    b2 = types.KeyboardButton("🧪 Test & Quiz")
    b3 = types.KeyboardButton("🗣️ English Speaking")
    b4 = types.KeyboardButton("🌐 Visit Website")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, "👇 Menu से चुनें:", reply_markup=markup)

# Button responses
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    if message.text == "📚 PDF Resources":
        bot.send_message(message.chat.id,
            "📥 Direct Download Links:\n\n"
            "🔹 UP Board Class 6 to 12 Book:https://boardexam.netlify.app/up_board/up_board_all_page\n"
            "🔹 CBSE Class 6 to 12 Notes: https://boardexam.netlify.app/cbsc_bord/cbsc_board_all_page\n"
            "🔹 All IMPORTANT PAGE: https://boardexam.netlify.app/all-link-site\n"
            "🔹 Graduation COURSE : https://boardexam.netlify.app/graduation/graduation\n"
            "➕ और भी: https://yourwebsite.com/downloads"
        )

    elif message.text == "🧪 Test & Quiz":
        bot.send_message(message.chat.id,
            "🧪 टेस्ट लिंक:\n\n"
            "✅ JEE MCQ: https://boardexam.netlify.app/jee&neet/jee_test\n"
            "✅ NEET Quiz: https://boardexam.netlify.app/jee&neet/neet_test\n"
            "✅ ITI Practice Test: https://boardexam.netlify.app/iti/iti_page\n"
            "✅ Merchant Navy: https://boardexam.netlify.app/marchant_navi/navi.%20all%20topic.html"
        )

    elif message.text == "🗣️ English Speaking":
        bot.send_message(message.chat.id,
            "🗣️ Spoken English Content:\n\n"
            "📖 Grammar Guide: https://boardexam.netlify.app/english_speacking.html/english-main\n"
            "🎧 Speaking Practice: https://boardexam.netlify.app/english_speacking.html/english-main\n"
            "📥 PDF Course: https://boardexam.netlify.app/english_speacking.html/english-main"
        )

    elif message.text == "🌐 Visit Website":
        bot.send_message(message.chat.id, "🌐 Visit करें: https://boardexam.netlify.app/")

    else:
        bot.send_message(message.chat.id, "कृपया Menu से कोई विकल्प चुनें।")

# Run the bot
print("🤖 Bot चालू हो चुका है...")
bot.polling()
