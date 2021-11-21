from mods.content.models import ContentMedia


def media_url(id):
    data = ContentMedia.objects.filter(id=id).values('id','public_url').first()
    return data["public_url"]