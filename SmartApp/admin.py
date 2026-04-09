from django.contrib import admin
from .models import IncidentReport

# This line tells Django to show the table in the Admin UI
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    
    list_display = ('category', 'description', 'created_at')
    list_filter = ('category', 'created_at')