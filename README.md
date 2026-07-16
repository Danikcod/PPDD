# PPDD - Telegram PDD Helper

Минимальный backend для Railway: FastAPI приложение с `/` и `/webhook`.

Запуск локально:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

В Railway используется `Procfile` с командой запуска.
