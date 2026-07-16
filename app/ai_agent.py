from pathlib import Path

from app.config import PDD_DOC_PATH


def load_pdd_document() -> str:
    path = Path(PDD_DOC_PATH)
    if not path.exists():
        return "Документ ПДД не найден. Пожалуйста, настройте PDD_DOC_PATH и загрузите файл документа."
    return path.read_text(encoding="utf-8")


def answer_question(question: str) -> str:
    document = load_pdd_document()
    if "не найден" in document:
        return document

    # Простейший поиск по документу в качестве заглушки.
    normalized = question.lower()
    if "знак" in normalized or "знаки" in normalized:
        return "Я нашёл информацию по знакам. В ближайшее время ответ будет уточнён по документу ПДД."
    if "скорость" in normalized or "км/ч" in normalized:
        return "Скоростной режим зависит от типа дороги. Для точного ответа используйте ИИ-асистента по документу ПДД."
    if "парков" in normalized:
        return "Парковка разрешена, если нет запрещающих знаков и разметки. Уточню ответ по документу ПДД."
    if "перекрёст" in normalized:
        return "На перекрёстке действует правило правой руки, если нет знаков приоритета."
    if "пешеход" in normalized:
        return "Пешеходы имеют преимущество на переходах. Внимательно следите за зеброй."
    if "штраф" in normalized:
        return "Штрафы зависят от нарушения. Уточните конкретную ситуацию, и я помогу найти правила."

    return (
        "Я принимаю вопрос к ИИ-ассистенту. Скоро появится ответ на основе документа ПДД."
    )
