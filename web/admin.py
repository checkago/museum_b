from django.contrib import admin
from web.models import *
from django import forms
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


class SimphonyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        verbose_name = 'Текст'
        model = Simphony
        fields = '__all__'


class SimphonyAdmin(admin.ModelAdmin):
    form = SimphonyAdminForm
    list_display = ('title',)


class WomenAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        verbose_name = 'Текст'
        model = Women
        fields = '__all__'


class WomenAdmin(admin.ModelAdmin):
    form = WomenAdminForm
    list_display = ('name',)


class BookAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        verbose_name = 'Текст'
        model = Book
        fields = '__all__'


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ('title',)


admin.site.register(Book, BookAdmin)
admin.site.register(Simphony, SimphonyAdmin)
admin.site.register(Women, WomenAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Voice)
admin.site.register(Quote)
admin.site.register(Foto)
