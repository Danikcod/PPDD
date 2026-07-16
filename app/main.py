from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.bot_logic import build_response
from app.telegram_client import send_message


app = FastAPI()


class WebhookUpdate(BaseModel):
    update_id: int
    message: dict | None = None
    callback_query: dict | None = None


@app.get("/")
async def root():
    return {"status": "ok", "service": "PPDD bot backend"}


@app.post("/webhook")
async def webhook(update: WebhookUpdate):
    if not update.message:
        raise HTTPException(status_code=400, detail="No message payload")

    chat_id = update.message.get("chat", {}).get("id")
    text = update.message.get("text", "").strip()

    if not chat_id or not text:
        raise HTTPException(status_code=400, detail="Message must contain chat id and text")

    reply_text, reply_markup = build_response(text)
    result = await send_message(chat_id, reply_text, reply_markup)
    return {"ok": True, "telegram_response": result}
