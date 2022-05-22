from django.contrib import admin
from .models import AnalysisReport, AnalysisReportLine


# class CustomerReportTemplateAdmin(admin.ModelAdmin):
    # search_fields = [
        # 'template_name',
    # ]
    # list_display = [
        # 'template_name',
        # 'customer_id'
    # ]
class AnalysisReportLineAdmin(admin.TabularInline):
    model = AnalysisReportLine
    fields = [
        'analysis_name',
        'value_text',
        'value',
        'lower_than',
        'greater_than',
    ]

class AnalysisReportAdmin(admin.ModelAdmin):
    list_display = [
        'analysis_report_name',
        'sample_result_name',
    ]
    list_filter = ['status']
    inlines = [AnalysisReportLineAdmin]

admin.site.register(AnalysisReport, AnalysisReportAdmin)
