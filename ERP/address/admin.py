from django.contrib import admin

from .models import District, Municipality, Elderate, City, Street, Building


# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        'apskr_id',
        'apskr_no',
        'apskr_name',
    )

    list_filter = ()


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = (
        'sav_id',
        'sav_name',
        'apskr_name'

    )
    list_filter = ()


class ElderateAdmin(admin.ModelAdmin):
    list_display = (
        'sen_id',
        'sen_name',
        'sav_name'

    )
    list_filter = ()


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'gyv_id',
        'gyv_name',
        'sen_name'

    )
    list_filter = ()


class StreetAdmin(admin.ModelAdmin):
    list_display = (
        'active',
        'str_id',
        'str_name',
        'gyv_name'

    )
    list_filter = ()


class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'active',
        'AOB_KODAS',
        'NR',
        'KORPUSO_NR',
        'PASTO_KODAS'
    )

    # list_filter = ('active', 'AOB_KODAS', 'NR', 'KORPUSO_NR', 'PASTO_KODAS')
    # # list_filter parodo filtravimo laukus
    # fieldsets = (
    #     (None, {'fields': ('AOB_KODAS', 'NR', 'KORPUSO_NR', 'PASTO_KODAS', 'active')}),
    # )


#
#     klasė parodo kaip atrodys modelis admin puslapyje

admin.site.register(District, DistrictAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Elderate, ElderateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(Building, BuildingAdmin)
