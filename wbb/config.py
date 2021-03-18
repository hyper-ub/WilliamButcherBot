from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER = int(getenv(("OWNER_ID")))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LOG_GROUP = int(getenv("LOG_GROUP"))
FERNET_ENCRYPTION_KEY = getenv("FERNET_ENCRYPTION_KEY")
CAPTCHA_DELAY = int(getenv("CAPTCHA_DELAY"))
MONGODB_URI = getenv("MONGODB_URI")
ARQ_API_ENDPOINT = getenv("ARQ_API_ENDPOINT")
