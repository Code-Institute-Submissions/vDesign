from django.contrib import admin
from .models import PowerPointProject


# Register your models here.
class PowerPointProjectAdmin(admin.ModelAdmin):
    
    list_display = (
        'client',
        'project_name',
        'project_description',
        'requirements',
        'quote',
    )

admin.site.register(PowerPointProject, PowerPointProjectAdmin)

