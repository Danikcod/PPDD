import httpx

from app.config import TELEGRAM_BOT_TOKEN

TELEGRAM_API_BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


async def send_message(chat_id: int, text: str, reply_markup: dict | None = None) -> dict:
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "MarkdownV2",
        "disable_web_page_preview": True,
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{TELEGRAM_API_BASE}/sendMessage", json=payload, timeout=30.0)
        response.raise_for_status()
        return response.json()
