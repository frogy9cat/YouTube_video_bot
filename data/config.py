import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili

# ADMINS=['486178287']
# BOT_TOKEN='5389210352:AAG5wIuNTE4EreKdsPrLNrDv_uVjdF6jBoQ'
# ip='localhost'
