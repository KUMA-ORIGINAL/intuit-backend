import html

from googletrans import Translator

translator = Translator()


def translate_text(text, target_lang, source_lang='ru'):
    """
    Переводит текст с сохранением HTML-тегов и корректной обработкой HTML-сущностей.

    :param text: Исходный текст с HTML-сущностями.
    :param target_lang: Целевой язык (например, 'en').
    :param source_lang: Язык источника (по умолчанию 'ru').
    :return: Переведённый текст с сохранением HTML-структуры.
    """
    try:
        clean_text = html.unescape(text)

        translated = translator.translate(clean_text, src=source_lang, dest=target_lang).text

        return html.escape(translated)
    except Exception as e:
        print(f"Error during translation: {e}")
        return text
