from django.contrib import admin
from .models import chemisrty, zoology, botany, sem1, sem2, sem3, sem4, sem5, sem6

# Register your models here.
admin.site.site_header = "Kishor Publications"
admin.site.register(chemisrty)
admin.site.register(botany)
admin.site.register(zoology)
admin.site.register(sem1)
admin.site.register(sem2)
admin.site.register(sem3)
admin.site.register(sem4)
admin.site.register(sem5)
admin.site.register(sem6)
