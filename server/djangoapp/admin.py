from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'car_make', 'dealer_id', 'year']
    list_display = ('name', 'car_make', 'type', 'year')

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
