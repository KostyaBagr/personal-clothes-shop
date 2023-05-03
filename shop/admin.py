from django.contrib import admin
from django.contrib.admindocs import urls
# Register your models here.
from .models import Category, Product, ProductVariant, ClothingSize, ProductPhotos
from django.utils.safestring import mark_safe
import admin_thumbnails


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductPhotosAdmin(admin.ModelAdmin):
  pass

@admin_thumbnails.thumbnail('image')
class ProductPhotosInline(admin.TabularInline):
    model = ProductPhotos
    extra=1
    readonly_fields = ('id',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug',  'price', 'available', 'created', 'uploaded','preview']
    list_filter = ['name','available', 'created', 'uploaded','sizes']
    list_display_links = ('name','id')
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ProductPhotosInline,ProductVariantInline]


    def preview(self, obj):
        return mark_safe(f"<img src='{obj.image.url}'style='max-height: 80px; max-width:50px;'>")

class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_size', 'product_quantity', 'id']


admin.site.register(ClothingSize)
admin.site.register(ProductVariant,ProductVariantsAdmin)
admin.site.register(ProductPhotos, ProductPhotosAdmin)
admin.site.register(Product, ProductAdmin)