from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, Scope

class ScopeInlineForset(BaseInlineFormSet):
    def clean(self):
        self.all_bouls = []
        for form in self.forms:
            clean_data = form.cleaned_data
            self.all_bouls.append(clean_data['is_main'])
        if self.all_bouls.count(True) == 0:
            raise ValidationError('Укажите основной раздел')
        elif self.all_bouls.count(True) >= 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineForset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline]
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']