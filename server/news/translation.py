from modeltranslation.translator import register, TranslationOptions
from .models import Post, Category, Image, File


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(File)
class ImageTranslationOptions(TranslationOptions):
    fields = ('title',)
