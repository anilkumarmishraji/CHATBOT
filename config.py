from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "27345751"
# -------------------------------------------------------------
API_HASH = "2f4074e9f5a56e99fd9ba562f2314523"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7282582221"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/anilkumarmishraji/CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "HINDII_CHATTING"
UPDATE_CHNL = "RAJA_NETWORKS"
OWNER_USERNAME = "ll_Raja_babu_ll"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
