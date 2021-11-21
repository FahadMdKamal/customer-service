from django.contrib import admin

# Register your models here.
from mods.nlu.models import NluEntities, NluImportFile, NluIntent, NluSync, NluUtterances, StaticDictionary

admin.site.register(NluEntities)
admin.site.register(NluImportFile)
admin.site.register(NluIntent)
admin.site.register(NluSync)
admin.site.register(NluUtterances)
admin.site.register(StaticDictionary)