from django import forms
from django.contrib import admin
from .models import users, section, caterogy, catalogy, package, image
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CatalogyAdminForm(forms.ModelForm):
    discription = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = catalogy
        fields = '__all__'

admin.site.register(users)
admin.site.register(section)
admin.site.register(caterogy)
admin.site.register(package)
admin.site.register(image)

@admin.register(catalogy)
class CatalogyAdmin(admin.ModelAdmin):
    form = CatalogyAdminForm

