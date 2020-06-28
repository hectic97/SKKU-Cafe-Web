from django.contrib import admin

# Register your models here.
from .models import evaluation,facilityreview,moodreview

admin.site.register(evaluation)
admin.site.register(facilityreview)
admin.site.register(moodreview)