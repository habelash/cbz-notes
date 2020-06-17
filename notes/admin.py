from django.contrib import admin
from .models import chemisrty, zoology, botany

# Register your models here.
admin.site.site_header = "Kishor Publications"
admin.site.register(chemisrty)
admin.site.register(botany)
admin.site.register(zoology)
