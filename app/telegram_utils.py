from typing import Any, Dict

TELEGRAM_API_URL = "https://api.telegram.org"


def build_message(chat_id: int, text: str, reply_markup: Dict[str, Any] = None) -> Dict[str, Any]:
    message = {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "MarkdownV2",
    }
    if reply_markup is not None:
        message["reply_markup"] = reply_markup
    return message


def build_keyboard(buttons: list) -> Dict[str, Any]:
    return {
        "keyboard": [[{"text": button}] for button in buttons],
        "resize_keyboard": True,
        "one_time_keyboard": False,
    }
