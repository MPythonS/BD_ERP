from django.contrib import admin

from .models import ListTest


# Register your models here.
class ListTestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'updated'
    )
    list_filter = ()


admin.site.register(ListTest, ListTestAdmin)
