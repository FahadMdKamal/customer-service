 
def upload_handler(request) -> str:
    uploaded_file = request.FILES['file']
    with open('media/' + uploaded_file.name, 'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)

    return str({"media_url": f"media/ + {uploaded_file.name}" })
