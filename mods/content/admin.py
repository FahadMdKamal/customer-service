from django.contrib import admin

from mods.content.models.flow import Flow
from .models import Content, ContentText, ContentData, ContentMedia, ConverseContentType, ContentTaxonomy, ContentCustomFields, ContentVars
from .models.flow_node import FlowNode
from .models.node_config import NodeConfig
from .models.node_contents import NodeContent

admin.site.register(Content)
admin.site.register(ContentText)
admin.site.register(ContentData)
admin.site.register(ContentMedia)
admin.site.register(ConverseContentType)
admin.site.register(ContentTaxonomy)
admin.site.register(ContentCustomFields)
admin.site.register(ContentVars)
admin.site.register(Flow)
admin.site.register(FlowNode)
admin.site.register(NodeConfig)
admin.site.register(NodeContent)
