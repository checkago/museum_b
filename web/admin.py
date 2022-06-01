from django.contrib import admin
from web.models import *
from django import forms
from ckeditor.widgets import CKEditorWidget


class SimphonyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = Simphony
        fields = '__all__'


class SimphonyAdmin(admin.ModelAdmin):
    form = SimphonyAdminForm
    list_display = ('title',)


admin.site.register(Simphony, SimphonyAdmin)
