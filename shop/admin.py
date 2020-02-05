from django.contrib import admin
from .models import CustomUser, SubKind, Image, Kind, Advert

admin.site.register(CustomUser)
admin.site.register(SubKind)
admin.site.register(Image)
admin.site.register(Kind)
admin.site.register(Advert)
