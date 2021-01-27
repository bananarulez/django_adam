from django.contrib import admin

# Register your models here.
from .models import Cvut, CvutImages


class PostImageAdmin(admin.StackedInline):
    model = CvutImages


@admin.register(Cvut)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Cvut


@admin.register(CvutImages)
class PostImageAdmin(admin.ModelAdmin):
    pass