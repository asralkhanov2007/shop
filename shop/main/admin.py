from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Colors)


class ProductImageAdmin(admin.StackedInline):
	model =  ProductImages

#Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}



# Product
@admin.register(Product)
class ProAdmin(admin.ModelAdmin):
	inlines = [ProductImageAdmin]
	list_display = ['name', 'category', 'instock']
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Product

@admin.register(ProductImages)
class PrImAdmin(admin.ModelAdmin):
	pass