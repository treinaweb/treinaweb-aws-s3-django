from django.contrib import admin
from restapi.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo, PhotoAdmin)
