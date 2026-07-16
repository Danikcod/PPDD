from app.faq_data import DEFAULT_REPLY, FAQ_ANSWERS, TOPIC_BUTTONS
from app.telegram_utils import build_keyboard
from app.ai_agent import answer_question


def build_response(text: str) -> tuple[str, dict]:
    if text == "/start":
        reply = (
            "Привет! Я бот-ПДД помощник. Выберите тему из клавиатуры ниже или напишите свой вопрос о правилах дорожного движения."
        )
        return reply, build_keyboard(TOPIC_BUTTONS)

    if text in FAQ_ANSWERS:
        answer, example = FAQ_ANSWERS[text]
        reply = f"*{text}*\n{answer}\n\n_{example}_"
        return reply, build_keyboard(TOPIC_BUTTONS)

    # Если есть AI-ассистент, то обрабатываем все остальные вопросы через него.
    ai_answer = answer_question(text)
    return ai_answer, build_keyboard(TOPIC_BUTTONS)
