# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BAAf70YAt6-qUh6CLOTLbEgJYDjKRcOBpqkSAJYEUgLpou47rpQhlfgh5-BvKR6JUbWIrSWhsoZQe41CLlKTW_hw4gSH4kcXAnEpIOEvIJGkLtb23BAkyIcmPQrm2FoCoMIdWlhdusWXUSgyp7JK7WCqOcj4efjYFvbz7dM_Hn8fF1GJFRn1AddvJlkD1hgG7kdZ2lJA9tvfEJ32eUx4rr5GSEXg6o1Cn8b0lP9_JL0bSg1v_dShBhYI0xZ4d79n9RrVLYJxvk-H6m2xGReaKdlpMN8VOuIDSuxeoe3qLls1ar-K_HeTj7VV5r2YxqKFD1cciOY-BmeDYLwbkGKMfD9Kz13QAAAAFl-M36AA")
