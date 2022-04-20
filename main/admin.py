from django import forms
from django.contrib import admin
from .models import users
<<<<<<< HEAD
from goods.models import *
=======
from mptt.admin import DraggableMPTTAdmin
from goods.models import section_and_caterogy, products, package, image
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
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
<<<<<<< HEAD
admin.site.register(section_and_caterogy, MPTTModelAdmin)
=======
admin.site.register(section_and_caterogy)
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
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