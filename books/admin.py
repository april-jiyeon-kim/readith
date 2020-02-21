from django.contrib import admin
from . import models

@admin.register(models.Genre)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name",)

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """ Book Admin Definition """

    fieldsets = (
        (
            "Book Info",
            {"fields": ("title", "description", "author", "published_date", "pages", "genres")},
        ),
    )

    list_display = (
        "title",
        "description",
        "author",
        "published_date",
        "pages",
    )


    search_fields = ("^title", "^description", "author")
