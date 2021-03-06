from django.contrib import admin
from .models import Page, Ticket


class PageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','source','page_id')
admin.site.register(Page, PageAdmin)

class TicketAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('message_type','platform','source','case_id','received_at')
admin.site.register(Ticket, TicketAdmin)