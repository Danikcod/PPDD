from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok", "service": "PPDD bot backend"}


@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    # placeholder: process incoming Telegram update
    return {"received": True, "update": payload}
