from django.contrib import admin
from .models import Contact,Gallery,Category,Product



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)
    prepopulated_fields = {'slug':('title',)}