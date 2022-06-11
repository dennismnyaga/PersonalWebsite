from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from . models import *


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Djangonister ,MyModelAdmin)
admin.site.register(Pythonister, MyModelAdmin)
# admin.site.register(Djangonister)
admin.site.register(Portfolio)