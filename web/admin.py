from django.contrib import admin
from .models import Contact,Gallery,Category,Product,Advertisement



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)
    


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('image',)
    


