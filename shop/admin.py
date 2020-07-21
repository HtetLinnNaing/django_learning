from django.contrib import admin
from shop.models import inventory


# Register your models here.
class InventoryInline(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'category', 'label', 'item_quantity','item_price', 'unit_price']


admin.site.register(inventory, InventoryInline)
