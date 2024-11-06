from django.utils import translation
from django.conf import settings


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Попробуем получить язык из заголовка HTTP_ACCEPT_LANGUAGE
        lang = request.META.get('HTTP_ACCEPT_LANGUAGE')

        if lang and lang in dict(settings.LANGUAGES):
            translation.activate(lang)
        else:
            # Используем язык по умолчанию, если язык из заголовка не поддерживается
            translation.activate(settings.LANGUAGE_CODE)

        # Передаем запрос дальше в приложение
        response = self.get_response(request)

        return response