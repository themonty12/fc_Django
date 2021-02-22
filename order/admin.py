from django.contrib import admin
from django.utils.html import format_html
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status')

    def styled_status(self, obj):
        if obj.status == "환불":
            return format_html(f'<sapn style="color:red">{ obj.status }</span>')
        elif obj.status == "결제완료":
            return format_html(f'<sapn style="color:green">{ obj.status }</span>')
        return obj.status

    styled_status.short_description = '상태'

admin.site.register(Order, OrderAdmin)