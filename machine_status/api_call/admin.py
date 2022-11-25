from django.contrib import admin
from .models import Status
admin.site.register(Status)
class useradmin(admin.ModelAdmin):
    list_display = ('S_id','status')
