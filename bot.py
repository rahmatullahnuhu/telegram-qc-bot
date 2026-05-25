from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
import os

# ==============================
# BOT TOKEN
# ==============================
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==============================
# RESTRICTED WORDS
# ==============================
RESTRICTED_WORDS = [

    # Communication Related
    "skype",
    "whatsapp",
    "telegram",
    "messenger",
    "discord",
    "zoom",
    "google meet",
    "meet",
    "gmail",
    "email",
    "yahoo mail",
    "contact me",
    "call me",
    "phone number",
    "mobile number",
    "number",
    "outside fiverr",
    "private chat",
    "direct contact",
    "personal contact",
    "reach me",
    "talk privately",
    "outside platform",
    "business deal outside",
    "send your details",

    # Payment Related
    "pay",
    "payment",
    "paypal",
    "payoneer",
    "wise",
    "transferwise",
    "bank account",
    "credit card",
    "debit card",
    "money",
    "money transfer",
    "crypto",
    "bitcoin",
    "invoice",
    "send money",

    # Marketplace Related
    "upwork",
    "freelancer",
    "peopleperhour",
    "guru",
    "legiit",
    "marketplace",
    "other platform",
]

# ==============================
# START COMMAND
# ==============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ QC Warning Bot is Active & Monitoring Messages."
    )

# ==============================
# MESSAGE CHECKER
# ==============================
async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    # Convert message to lowercase
    message_text = update.message.text.lower()

    # Detect restricted words
    detected_words = []

    for word in RESTRICTED_WORDS:
        if word.lower() in message_text:
            detected_words.append(word)

    # Remove duplicate words
    detected_words = list(set(detected_words))

    # If restricted word found
    if detected_words:

        detected_text = "\n".join(
            [f"• [{word}]" for word in detected_words]
        )

        warning_message = (
            "⚠️ Restricted word detected.\n"
            "Please kindly fix your message.\n\n"
            "Detected Words:\n"
            f"{detected_text}"
        )

        await update.message.reply_text(warning_message)

# ==============================
# MAIN FUNCTION
# ==============================
def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Message Handler
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, check_message)
    )

    print("✅ QC Warning Bot Running...")

    app.run_polling()

# ==============================
# RUN BOT
# ==============================
if __name__ == "__main__":
    main()
