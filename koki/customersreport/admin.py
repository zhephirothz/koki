from django.contrib import admin
from .models import CustomerReportTemplate


class CustomerReportTemplateAdmin(admin.ModelAdmin):
    search_fields = [
        'template_name',
    ]
    list_display = [
        'template_name',
        'customer_id'
    ]

admin.site.register(CustomerReportTemplate, CustomerReportTemplateAdmin)
