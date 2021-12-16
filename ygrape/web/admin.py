from django.contrib import admin
from web.models import sensor, controller, data, alarm

# Register your models here.


admin.site.register([sensor, controller, data, alarm])
