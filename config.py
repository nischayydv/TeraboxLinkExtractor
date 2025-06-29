import os

class Config:
    # Set your Terabox ndus cookie
    TERA_COOKIE = os.getenv("TERA_COOKIE", "Yvi0JX1peHuimKDAHhsHkhS3X_0MerqG2AwZNwYb")

    # Telegram API credentials
    API_ID = int(os.getenv("API_ID", 24720215))  # Replace 123456 with your API ID
    API_HASH = os.getenv("API_HASH", "c0d3395590fecba19985f95d6300785e")

    # Telegram bot token
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8037389280:AAF-M7JAws6kG5G1cn2ZNnxdLKAhVPPLkUU")
