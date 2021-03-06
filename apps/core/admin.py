from django.contrib import admin
from apps.core.models import (Taxonomy,
                              TaxonomyType,
                              Apps,
                              Profile,
                              LoggedInUserInfo,
                              PasswordStore,
                              UserAllowOrigin,
                              Channels,
                              WorkGroups
                              )


admin.site.site_header = "Univa Admin Panel"
admin.site.site_title = "Univa Admin Portal"
admin.site.index_title = "Welcome to Univa Portal"

# admin.site.register(Taxonomy)
admin.site.register(TaxonomyType)
admin.site.register(LoggedInUserInfo)
admin.site.register(PasswordStore)
admin.site.register(Channels)


@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    list_display = ('app_code', 'status',)
    prepopulated_fields = {"slug": ("app_code","app_domain")}


@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ("name", 'app', 'taxonomy_type', 'parent')
    list_filter = ('app', 'taxonomy_type',)
    prepopulated_fields = {"slug": ("taxonomy_type","name")}
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile',)


@admin.register(UserAllowOrigin)
class UserAllowOriginAdmin(admin.ModelAdmin):
    list_display = ('user', 'principal', 'allowed',
                    'origin_type', 'origin_sig')
    list_filter = ('user', 'origin_type', 'allowed')


@admin.register(WorkGroups)
class WorkGroups(admin.ModelAdmin):
    pass
