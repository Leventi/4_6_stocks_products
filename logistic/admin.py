from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    fields = ['stock', 'product', 'quantity', 'price']
    list_display = ('stock', 'product', 'quantity', 'price')
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ('title', 'description')
    inlines = [StockProductInline]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    fields = ['address']
    list_display = ('address', )
    inlines = [StockProductInline]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('stock', 'product', 'quantity', 'price')

