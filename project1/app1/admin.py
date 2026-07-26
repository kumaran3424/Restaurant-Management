from django.contrib import admin

# Register your models here.
from app1.models import*
admin.site.register(chef)
admin.site.register(category)
admin.site.register(menuitem)
admin.site.register(dinning_table)