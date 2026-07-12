# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# Mandatory Variables
API_ID = int(os.getenv("API_ID", "1234567"))
API_HASH = os.getenv("API_HASH", "default_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "default_bot_token")
OWNER_ID = os.getenv("OWNER_ID", "123456789")  # String အနေနဲ့ ထားပါ

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

# Chats (အားလုံးကို String အနေနဲ့ ထားပြီးမှ လိုအပ်ရင် int() နဲ့ ပြောင်းပါ)
AUTH_CHAT = os.getenv("AUTH_CHAT", "-100123456789")  # String အနေနဲ့ ထားပါ
LOGS_CHAT = os.getenv("LOGS_CHAT", "-1001234567891")  # String အနေနဲ့ ထားပါ
POST_CHAT = os.getenv("POST_CHAT", "-1001234567891")  # String အနေနဲ့ ထားပါ

# Admin Credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "adminadmin")

# Site Configs
SITE_SECRET = os.getenv("SITE_SECRET", "defaultsecretkey")
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")

SITE_NAME = os.getenv("SITE_NAME", "reelnn")
POST_CHAT_LINK = os.getenv("POST_CHAT_LINK", "https://t.me/reelnnUpdates")
ENABLE_REGISTRATION = os.getenv("ENABLE_REGISTRATION", "False").lower() in ("true", "1", "yes")

SIGNUP_IMAGE = os.getenv("SIGNUP_IMAGE", "https://i.ibb.co/dJ2t5bsF/anime-AI-1.jpg")
SIGNUP_MESSAGE = os.getenv("SIGNUP_MESSAGE", """
**Heyaa** 🙋🏻‍♀️\n
**Welcome to DocKeeper!** 🎬 
Your ultimate destination for entertainment!
To get started and access our media library,
please register your account.

👉 Use the /register command to sign up for the site.
""")

# Optional Variables
MULTI_TOKENS = {
    # 1: os.getenv("MULTI_BOT_TOKEN_1"),
    # 2: os.getenv("MULTI_BOT_TOKEN_2"),
    # Add more if needed
}

DELETE_AFTER_MINUTES = int(os.getenv("DELETE_AFTER_MINUTES", "10"))
POST_UPDATES = os.getenv("POST_UPDATES", "True").lower() in ("true", "1", "yes")
USE_CAPTION = os.getenv("USE_CAPTION", "False").lower() in ("true", "1", "yes")

# Port configuration
PORT = int(os.getenv("PORT", "10000"))

# Derived and Protected Variables (Don't Touch)
# ဒီနေရာမှာ int() နဲ့ ပြောင်းပါ
SUDO_USERS = [int(x) for x in str(OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in str(AUTH_CHAT).split()]
