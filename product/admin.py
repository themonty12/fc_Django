from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock')

    def price_format(self, obj):
        price = intcomma(obj.price)
        return f'{price} 원'


    def styled_stock(self, obj):
        stock = obj.stock
        if stock <= 50:
            stock = intcomma(stock)
            return format_html(f'<b><sapn style="color:red">{ stock } 개</span></b>')    
        return f'{intcomma(stock)} 개'

    def changelist_view(self, request, extra_context=None):
        # 원하는 동작 (제목 바꾸기)
        extra_context = { 'title' : '상품 목록' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        product = Product.objects.get(pk=object_id)
        extra_context = { 'title' : f'{ product.name } 수정하기' }
        return super().changeform_view(request, object_id, form_url, extra_context)

    styled_stock.short_description = '재고'
    price_format.short_description = '가격'

admin.site.register(Product, ProductAdmin)