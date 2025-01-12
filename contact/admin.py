from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'show','id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'show','first_name', 'last_name',
    list_display_links = 'phone','id',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name',
    ordering = '-id',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'name',