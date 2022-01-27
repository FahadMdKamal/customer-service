from django.contrib import admin
from apps.core.models import (Taxonomy,
                              TaxonomyType,
                              App,
                              Profile,
                              Organization,
                              LoggedInUserInfo,
                              PasswordStore,
                              UserAllowOrigin,
                              ChannelTypes,
                              MavrikApps,
                              MaverikChannels)


admin.site.site_header = "Univa Admin Panel"
admin.site.site_title = "Univa Admin Portal"
admin.site.index_title = "Welcome to Univa Portal"

admin.site.register(Taxonomy)
admin.site.register(TaxonomyType)
admin.site.register(LoggedInUserInfo)
admin.site.register(PasswordStore)
admin.site.register(ChannelTypes)
admin.site.register(MavrikApps)
admin.site.register(MaverikChannels)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'organization')
    list_filter = ('organization',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(UserAllowOrigin)
class UserAllowOriginAdmin(admin.ModelAdmin):
    list_display = ('user', 'principal', 'allowed',
                    'origin_type', 'origin_sig')
    list_filter = ('user', 'origin_type', 'allowed')
