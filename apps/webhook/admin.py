from django.contrib import admin
from .models import Page, Ticket

admin.site.site_header = "Social Attend Admin Panel"
admin.site.site_title = "Social Attend Admin Portal"
admin.site.index_title = "Welcome to Social Attend Portal"

class PageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','source','page_id')
admin.site.register(Page, PageAdmin)

class TicketAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('message_type','platform','source','case_id','received_at')
admin.site.register(Ticket, TicketAdmin)