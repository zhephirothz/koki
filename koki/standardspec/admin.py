from django.contrib import admin
from .models import StandardSpecLine, StandardSpec


class StandardSpecLineInline(admin.TabularInline):
    model = StandardSpecLine
    fields = [
        'name',
        'value_text',
    ]
    extra = 5


class StandardSpecAdmin(admin.ModelAdmin):
    inlines = [StandardSpecLineInline]
    list_display = [
        'spec_name',
        'remark',
    ]

admin.site.register(StandardSpec, StandardSpecAdmin)
