from django.contrib import admin
from .models import Car, Cart, HomeInfo
# Register your models here.

admin.site.register(Car)
admin.site.register(HomeInfo)
admin.site.register(Cart)