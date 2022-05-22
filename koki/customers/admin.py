from django.contrib import admin
from .models import Customers

class CustomersAdmin(admin.ModelAdmin):
    search_fields = [
        'customer_code',
        'customer_name'
    ]
    list_display = [
        'customer_code',
        'customer_name'
    ]

admin.site.register(Customers, CustomersAdmin)
