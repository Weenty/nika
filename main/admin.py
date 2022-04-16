from django import forms
from django.contrib import admin
from .models import users
from goods.models import section, caterogy, products, package, image
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CatalogyAdminForm(forms.ModelForm):
    discription = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = products
        fields = '__all__'

admin.site.register(users)
admin.site.register(section)
admin.site.register(caterogy)
admin.site.register(package)
admin.site.register(image)

@admin.register(products)
class CatalogyAdmin(admin.ModelAdmin):
    form = CatalogyAdminForm

