from django.contrib import admin
from .models import *


# class StatusAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Status


class BookInline(admin.TabularInline):
    model = BookRazdel


class BookAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]

    class Meta:
        model = Customer


class TripInOrderInline(admin.TabularInline):
    model = TripInOrder


class OrderAdmin(admin.ModelAdmin):

    inlines = [
        TripInOrderInline,
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)
# admin.site.register(Status,StatusAdmin)

# Register your models here.
