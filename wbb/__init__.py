from pyrogram import Client

from Python_ARQ import ARQ
import time
import logging
from .config import BOT_TOKEN, API_ID, API_HASH, SUDO_USERS, OWNER, ARQ_API_ENDPOINT

f = open("error.log", "w")
f.write("PEAK OF LOG FILE")

LOG_FORMAT = (
    '''
    [%(asctime)s.%(msecs)03d] %(filename)s:%(lineno)s
    %(levelname)s: %(message)s''')

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt="%m-%d %H:%M",
    filename="error.log",
    filemode="w",
)

console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter(LOG_FORMAT)
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

log = logging.getLogger()

SUDO_USERS = SUDO_USERS
SUDO_USERS.append(OWNER)

MOD_LOAD = []
MOD_NOLOAD = []

bot_start_time = time.time()
app = Client("wbb", bot_token=API_HASH, api_id=API_ID, api_hash=API_HASH)
arq = ARQ(ARQ_API_ENDPOINT)
