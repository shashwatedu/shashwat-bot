import telebot
from telebot import types
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot token (in a real application, store this securely)
API_KEY = '8179484671:AAGF2Wr4FVmmpIK9R3ejdXSum1Asdom_mLA'
bot = telebot.TeleBot(API_KEY)

# Resource URLs (organized for easy maintenance)
RESOURCES = {
    "pdf": {
        "UP Board": "https://boardexam.netlify.app/up_board/up_board_all_page",
        "CBSE Notes": "https://boardexam.netlify.app/cbsc_bord/cbsc_board_all_page",
        "Important Pages": "https://boardexam.netlify.app/all-link-site",
        "Graduation": "https://boardexam.netlify.app/graduation/graduation"
    },
    "tests": {
        "JEE MCQ": "https://boardexam.netlify.app/jee&neet/jee_test",
        "NEET Quiz": "https://boardexam.netlify.app/jee&neet/neet_test",
        "ITI Practice": "https://boardexam.netlify.app/iti/iti_page",
        "Merchant Navy": "https://boardexam.netlify.app/marchant_navi/navi.all%20topic.html"
    },
    "english": {
        "Grammar Guide": "https://boardexam.netlify.app/english_speacking.html/english-main",
        "Speaking Practice": "https://boardexam.netlify.app/english_speacking.html/english-main",
        "PDF Course": "https://boardexam.netlify.app/english_speacking.html/english-main"
    },
    "website": "https://boardexam.netlify.app/"
}

# Helper function to create keyboard markup
def create_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        types.KeyboardButton("📚 PDF Resources"),
        types.KeyboardButton("🧪 Tests & Quizzes"),
        types.KeyboardButton("🗣️ English Speaking"),
        types.KeyboardButton("🌐 Visit Website"),
        types.KeyboardButton("ℹ️ About Bot"),
        types.KeyboardButton("🆘 Help")
    ]
    markup.add(*buttons)
    return markup

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        welcome_msg = (
            "🙏 नमस्ते {name}! मैं Shashwat का Educational Bot हूँ।\n\n"
            "📚 मैं आपको निम्नलिखित सुविधाएँ प्रदान करता हूँ:\n"
            "- सभी कक्षाओं की 📘 पुस्तकें और 📄 नोट्स\n"
            "- परीक्षा 📑 पेपर्स और 🧪 प्रैक्टिस टेस्ट\n"
            "- 🗣️ अंग्रेजी बोलने का प्रशिक्षण\n"
            "- और भी बहुत कुछ!\n\n"
            "👇 नीचे दिए गए मेनू से अपना विकल्प चुनें"
        ).format(name=message.from_user.first_name)
        
        bot.send_message(
            message.chat.id,
            welcome_msg,
            reply_markup=create_menu_keyboard()
        )
        logger.info(f"Sent welcome message to {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in send_welcome: {e}")
        bot.reply_to(message, "⚠️ कुछ त्रुटि हुई। कृपया पुनः प्रयास करें।")

# Help command handler
@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda msg: msg.text == "🆘 Help")
def send_help(message):
    help_text = (
        "🆘 सहायता केंद्र:\n\n"
        "📌 मैं आपको निम्नलिखित सेवाएँ प्रदान करता हूँ:\n"
        "- शैक्षिक संसाधन डाउनलोड\n"
        "- ऑनलाइन टेस्ट और क्विज\n"
        "- अंग्रेजी सीखने के संसाधन\n\n"
        "🔹 उपयोग करने के लिए मेनू बटन का प्रयोग करें या निम्न कमांड टाइप करें:\n"
        "/start - बॉट पुनः आरंभ करें\n"
        "/help - सहायता देखें\n"
        "/about - बॉट के बारे में जानकारी\n\n"
        "समस्या होने पर संपर्क करें: support@example.com"
    )
    bot.send_message(message.chat.id, help_text)

# About command handler
@bot.message_handler(commands=['about'])
@bot.message_handler(func=lambda msg: msg.text == "ℹ️ About Bot")
def send_about(message):
    about_text = (
        "ℹ️ बॉट के बारे में:\n\n"
        "📚 Shashwat Educational Bot\n"
        "संस्करण: 2.0\n"
        "अंतिम अपडेट: 30 मई 2024\n\n"
        "यह बॉट छात्रों को निःशुल्क शैक्षिक संसाधन प्रदान करता है।\n\n"
        "विकसितकर्ता: Shashwat\n"
        "संपर्क: contact@example.com"
    )
    bot.send_message(message.chat.id, about_text)

# PDF Resources handler
@bot.message_handler(func=lambda msg: msg.text == "📚 PDF Resources")
def send_pdf_resources(message):
    try:
        response = "📚 PDF संसाधन:\n\n"
        for name, url in RESOURCES["pdf"].items():
            response += f"🔹 {name}: {url}\n"
        
        response += "\n⬆️ उपरोक्त लिंक पर क्लिक करके संसाधन डाउनलोड करें।"
        
        # Add inline buttons for quick access
        markup = types.InlineKeyboardMarkup()
        for name, url in RESOURCES["pdf"].items():
            markup.add(types.InlineKeyboardButton(text=name, url=url))
        
        bot.send_message(
            message.chat.id,
            response,
            reply_markup=markup,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error in send_pdf_resources: {e}")
        bot.reply_to(message, "⚠️ PDF संसाधन लोड करने में त्रुटि। कृपया बाद में पुनः प्रयास करें।")

# Tests handler
@bot.message_handler(func=lambda msg: msg.text == "🧪 Tests & Quizzes")
def send_tests(message):
    try:
        response = "🧪 परीक्षण और क्विज़:\n\n"
        for name, url in RESOURCES["tests"].items():
            response += f"✅ {name}: {url}\n"
        
        # Add inline buttons
        markup = types.InlineKeyboardMarkup()
        for name, url in RESOURCES["tests"].items():
            markup.add(types.InlineKeyboardButton(text=name, url=url))
        
        bot.send_message(
            message.chat.id,
            response,
            reply_markup=markup,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error in send_tests: {e}")
        bot.reply_to(message, "⚠️ टेस्ट लोड करने में त्रुटि। कृपया बाद में पुनः प्रयास करें।")

# English Speaking handler
@bot.message_handler(func=lambda msg: msg.text == "🗣️ English Speaking")
def send_english_resources(message):
    try:
        response = "🗣️ अंग्रेजी सीखने के संसाधन:\n\n"
        for name, url in RESOURCES["english"].items():
            response += f"📌 {name}: {url}\n"
        
        # Add inline buttons
        markup = types.InlineKeyboardMarkup()
        for name, url in RESOURCES["english"].items():
            markup.add(types.InlineKeyboardButton(text=name, url=url))
        
        bot.send_message(
            message.chat.id,
            response,
            reply_markup=markup,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error in send_english_resources: {e}")
        bot.reply_to(message, "⚠️ अंग्रेजी संसाधन लोड करने में त्रुटि।")

# Website handler
@bot.message_handler(func=lambda msg: msg.text == "🌐 Visit Website")
def send_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🌐 वेबसाइट खोलें", url=RESOURCES["website"]))
    bot.send_message(
        message.chat.id,
        "हमारी वेबसाइट पर जाएँ:",
        reply_markup=markup
    )

# Default handler for unknown messages
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(
        message,
        "❌ मैं इस कमांड को नहीं समझ पाया।\n\n"
        "कृपया मेनू से कोई विकल्प चुनें या /help टाइप करें।",
        reply_markup=create_menu_keyboard()
    )

# Error handler
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    try:
        bot.answer_callback_query(call.id, "Processing your request...")
    except Exception as e:
        logger.error(f"Error in callback: {e}")

# Start the bot
if __name__ == "__main__":
    logger.info("🤖 बॉट सक्रिय हो रहा है...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
