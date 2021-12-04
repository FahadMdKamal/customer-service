from django.contrib import admin
from apps.core.models import Taxonomy, TaxonomyType, App


admin.site.site_header = "Univa Admin Panel"
admin.site.site_title = "Univa Admin Portal"
admin.site.index_title = "Welcome to Univa Portal"

admin.site.register(Taxonomy)
admin.site.register(TaxonomyType)
admin.site.register(App)
