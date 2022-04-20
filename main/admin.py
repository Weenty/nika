from django import forms
from django.contrib import admin
from .models import users
from goods.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mptt.admin import MPTTModelAdmin

class ProductsAdminForm(forms.ModelForm):
    discription = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = products
        fields = '__all__'
admin.site.register(product_has_packages)
admin.site.register(product_has_section_and_category)
admin.site.register(users)
admin.site.register(section_and_caterogy, MPTTModelAdmin)
admin.site.register(package)
admin.site.register(image)

class ProductHasSectionAndCategoryInline(admin.TabularInline):
    model = product_has_section_and_category
    extra = 2

class ProductHasSectionAndCategoryAdmin(admin.ModelAdmin):
    inlines = (ProductHasSectionAndCategoryInline,)

admin.site.register(products, ProductHasSectionAndCategoryAdmin)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm