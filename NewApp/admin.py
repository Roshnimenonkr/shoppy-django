from django.contrib import admin
from .models import Category,Product,relatedimage,contact
# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display=('title','slug','category_image','is_active','description','is_featured')
    list_editable=('slug','is_featured','is_active')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category,category_admin)

class relatedimg_admin(admin.StackedInline):
    model=relatedimage



class product_admin(admin.ModelAdmin):
    list_display=('title','slug','product_image','short_description','detail_description','is_active','is_featured')
    list_editable=('slug','is_featured','is_active')
    search_fields=('title','short_description','detail_description')
    prepopulated_fields={'slug':('title',)}
    list_filter=('is_active','is_featured','category','price')
    inlines=[relatedimg_admin]
admin.site.register(Product,product_admin)

admin.site.register(contact)