from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Gp, Record, Filling

# 全站禁止删除功能
admin.site.disable_action('delete_selected')

class GpAdmin(admin.ModelAdmin):
    list_display = ('gp_code', 'zn_code', 'sc_date', 'jc_date', 'specification', 'company')
    search_fields = ('gp_code', 'zn_code')

    list_display_links = ('gp_code', 'zn_code')
    # list_editable = ('gp_code', 'zn_code')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('gp_code', 'time', 'client', 'tel', 'address')
    search_fields = ('gp_code', 'time', 'client', 'tel')
    # list_display_links = ('gp_code',)


admin.site.register(Gp, GpAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Filling)

