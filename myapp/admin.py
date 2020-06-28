from django.contrib import admin

# Register your models here.
from .models import building,menuinfo,detailaboutcafe

admin.site.register(building)
admin.site.register(menuinfo)
admin.site.register(detailaboutcafe)