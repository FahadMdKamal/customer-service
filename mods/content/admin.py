from django.contrib import admin

# Register your models here.

from .models import Content, ContentText, ContentData, ContentMedia, ConverseContentType, ContentTaxonomy, \
    ContentCustomFields, ContentVars

# Register your models here.

admin.site.register(Content)
admin.site.register(ContentText)
admin.site.register(ContentData)
admin.site.register(ContentMedia)
admin.site.register(ConverseContentType)
admin.site.register(ContentTaxonomy)
admin.site.register(ContentCustomFields)
admin.site.register(ContentVars)