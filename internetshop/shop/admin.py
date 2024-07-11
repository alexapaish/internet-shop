from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Review, ReviewAdmin)