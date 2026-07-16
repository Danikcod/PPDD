# PPDD - Telegram PDD Helper

Минимальный backend для Railway: FastAPI приложение с `/` и `/webhook`.

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Локальный запуск

1. Создайте файл `.env` на основе `.env.example`.
2. Положите `TELEGRAM_BOT_TOKEN` и `PDD_DOC_PATH`.
3. Запустите сервер:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Создание бота в BotFather

1. В Telegram найдите `@BotFather`.
2. Отправьте `/newbot`.
3. Придумайте имя и username бота.
4. Сохраните токен `TELEGRAM_BOT_TOKEN`.

## Настройка webhook

В Railway используйте `https://<your-service>.up.railway.app/webhook`.

Для теста локально можно пробросить порт через ngrok:

```bash
ngrok http 8000
```

и установить webhook через:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" \
  -d "url=https://<NGROK_URL>/webhook"
```

## Безопасность ключей

- `TELEGRAM_BOT_TOKEN` и `AI_API_KEY` должны храниться только в Railway как переменные окружения.
- не вставляй ключи в код и не отправляй их в открытые чаты.
- если ключ уже был опубликован, лучше сразу сгенерировать новый.

## Дубликат файла PDD

В проекте должен быть только один файл `pdd_document.txt`. Если ты случайно отправил документ дважды в чат, это не проблема, главное — в репозитории есть только один рабочий файл.

## Как работает бот

- `/start` — приветствие и выбор тем.
- Темы: `Знаки`, `Скорость`, `Парковка`, `Перекрёстки`, `Пешеходы`, `Штрафы`.
- Все остальные вопросы отправляются в ИИ-агент.

## Файлы

- `app/main.py` — FastAPI webhook.
- `app/bot_logic.py` — логика ответов на сообщения.
- `app/telegram_client.py` — отправка сообщений в Telegram.
- `app/ai_agent.py` — простой ИИ-парсер документа ПДД.
- `pdd_document.txt` — пример файла с правилами.
