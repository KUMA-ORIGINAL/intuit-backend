import requests
import time
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_telegram_message(text, retries=3, delay=2):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
    }
    last_exception = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, data=data, timeout=5)
            result = response.json()
            if result.get("ok"):
                logger.info(f"Telegram message sent successfully on attempt {attempt}")
                return True
            else:
                logger.error(f"Telegram API error on attempt {attempt}: {result}")
        except Exception as e:
            last_exception = e
            logger.error(f"Telegram send error on attempt {attempt}: {e}")
        time.sleep(delay)
    logger.critical(f"Telegram message NOT sent after {retries} attempts. Last exception: {last_exception}")
    return False
