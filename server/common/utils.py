# from bs4 import BeautifulSoup, NavigableString
# from django.conf import settings
# from openai import OpenAI
#
# client = OpenAI(api_key=settings.OPENAI_API_KEY)
#
#
# def translate_text(text, source_lang, target_lang):
#     if target_lang == 'en':
#         target_lang = 'английский'
#     elif target_lang == 'ky':
#         target_lang = 'кыргызский'
#     prompt = (
#         f"Переведи следующий текст с {source_lang} на {target_lang}. "
#         f"Сохрани пунктуацию и структуру. Переводи точно и без лишних примечаний:\n\n{text}"
#     )
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "Ты профессиональный переводчик. Переводи чётко и точно."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"[ERROR] Ошибка перевода: {e}")
#         return text
#
#
# def translate_html_content(html_text, source_lang, target_lang):
#     """
#     Переводит только текст внутри HTML-тегов, сохраняя структуру HTML.
#     """
#     soup = BeautifulSoup(html_text, 'html.parser')
#     text_nodes = [node for node in soup.descendants if isinstance(node, NavigableString) and node.strip()]
#
#     for node in text_nodes:
#         original_text = str(node)
#         translated = translate_text(original_text, source_lang, target_lang)
#         node.replace_with(translated)
#
#     return str(soup)
