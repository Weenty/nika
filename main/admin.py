from django import forms
from django.contrib import admin
from .models import *
from goods.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mptt.admin import MPTTModelAdmin
from django.utils.html import format_html

class ProductsAdminForm(forms.ModelForm):
    discription = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = products
        fields = '__all__'

@admin.register(package)
class PackageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.image.url))

    image_tag.short_description = 'image'
    list_display = ['name', 'cost', 'quantity']
    readonly_fields = ['image_tag']
    
@admin.register(image)
class ImageAdmin(PackageAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="100px" />'.format(obj.image.url))
    list_display = ['image_tag', 'image']


class ProductHasPackegeInline(admin.TabularInline):
    model = product_has_packages
    extra = 2

class ProductHasSectionAndCategoryInline(admin.TabularInline):
    model = product_has_section_and_category
    extra = 2

class ProductHasSectionAndCategoryAdmin(admin.ModelAdmin):
    inlines = (ProductHasSectionAndCategoryInline,ProductHasPackegeInline)

admin.site.register(products, ProductHasSectionAndCategoryAdmin)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
admin.site.register(users)
admin.site.register(section_and_caterogy, MPTTModelAdmin)
admin.site.register(basket)
admin.site.register(order)





