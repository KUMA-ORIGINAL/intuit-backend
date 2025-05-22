import logging
import httpx
from django.conf import settings

logger = logging.getLogger(__name__)

def send_telegram_message(text: str) -> None:
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)

    if not token or not chat_id:
        logger.warning("Telegram token или chat_id не сконфигурированы.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        response = httpx.post(url, data=payload, timeout=5)
        if response.status_code != 200:
            logger.error(
                "Ошибка при отправке Telegram-сообщения: %s | Ответ: %s",
                response.status_code,
                response.text,
            )
    except httpx.RequestError as exc:
        logger.exception("Сетевая ошибка при отправке в Telegram: %s", exc)
    except Exception as e:
        logger.exception("Неизвестная ошибка при отправке Telegram-сообщения: %s", e)
