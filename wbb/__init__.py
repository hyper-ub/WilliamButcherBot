from pyrogram import Client

from Python_ARQ import ARQ
import time
import logging
from sample_config import (
    bot_token,
    api_id,
    api_hash,
    OWNER_ID,
    sudo_users_id as SUDO_USER_ID,
    ARQ_API_BASE_URL as ARQ_API
)

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

SUDOERS = SUDO_USER_ID
SUDOERS.append(OWNER_ID)
MOD_LOAD = []
MOD_NOLOAD = []
bot_start_time = time.time()
app = Client("wbb", bot_token=bot_token, api_id=api_id, api_hash=api_hash)
arq = ARQ(ARQ_API)
