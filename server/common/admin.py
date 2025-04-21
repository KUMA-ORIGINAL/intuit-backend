import logging

from django.conf import settings
from django.urls import path, reverse
from django.shortcuts import redirect
from django.contrib import messages

from modeltranslation.admin import TabbedTranslationAdmin
from modeltranslation.translator import translator as model_translator

from .utils import translate_text

logger = logging.getLogger(__name__)


class AutoTranslateAdmin(TabbedTranslationAdmin):
    change_form_template = "admin/translate_button_change_form.html"  # подключаем шаблон

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/translate/',
                 self.admin_site.admin_view(self.translate_view),
                 name=f'{self.model._meta.app_label}_{self.model._meta.model_name}_translate'),
        ]
        return custom_urls + urls

    def translate_view(self, request, object_id):
        obj = self.model.objects.get(pk=object_id)

        default_lang = settings.LANGUAGE_CODE.split('-')[0]
        other_langs = [lang[0] for lang in settings.LANGUAGES if lang[0] != default_lang]

        opts = model_translator.get_options_for_model(self.model)
        for field in opts.fields:
            default_value = getattr(obj, f"{field}_{default_lang}", "")
            if default_value:
                for lang in other_langs:
                    field_name = f"{field}_{lang}"
                    logger.warning(f"field_name {field_name}")
                    value = getattr(obj, field_name, None)
                    logger.warning(f"Значение {value}")
                    if not value or not str(value).strip():
                        translated = translate_text(default_value, target_lang=lang, source_lang=default_lang)
                        logger.warning(f"Перевод {translated}")
                        setattr(obj, field_name, translated)

        obj.save()
        messages.success(request, "Перевод выполнен.")
        return redirect(f"../")

    def render_change_form(self, request, context, *args, **kwargs):
        obj = context.get("original")
        if obj:
            app_label = self.model._meta.app_label
            model_name = self.model._meta.model_name
            translate_url = reverse(f"admin:{app_label}_{model_name}_translate", args=[obj.pk])
            context["translate_url"] = translate_url
        return super().render_change_form(request, context, *args, **kwargs)