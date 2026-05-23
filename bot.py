from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import re

# =========================
# BOT TOKEN
# =========================

BOT_TOKEN = "8476597907:AAFLmCDvudAmDFWBIKebJvWZsxlTCsPr6Mg"

# =========================
# RESTRICTED WORDS
# =========================

RESTRICTED_WORDS = [

    # Contact Related
    "skype",
    "whatsapp",
    "email",
    "messenger",

    # Payment Related
    "pay",
    "payment",
    "paypal",
    "payoneer",
    "bank account",
    "money",
    "credit card",
    "transferwise",
    "stripe",

    # Marketplace Related
    "peopleperhour",
    "upwork",
    "freelancer",

    # Rating Related
    "positive feedback",
    "positive rating",
    "five star",
    "negative feedback",
]

# =========================
# DETECT FUNCTION
# =========================

async def detect_words(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # যদি message না থাকে
    if not update.message or not update.message.text:
        return

    # User Message ছোট হাতের করা
    text = update.message.text.lower()

    matched_words = []

    # সব restricted word check
    for word in RESTRICTED_WORDS:

        pattern = r'\b' + re.escape(word) + r'\b'

        matches = re.findall(pattern, text)

        if matches:

            for match in matches:

                formatted_word = f"• [{match}]"

                if formatted_word not in matched_words:
                    matched_words.append(formatted_word)

    # যদি restricted word detect হয়
    if matched_words:

        detected_text = "\n".join(matched_words)

        await update.message.reply_text(

            f"⚠️ Restricted word detected.\n"
            f"Please kindly fix your message.\n\n"
            f"Detected Words:\n"
            f"{detected_text}"
        )

# =========================
# APP START
# =========================

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, detect_words)
)

print("Bot Running...")

app.run_polling()