from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    book = models.ForeignKey("books.Book", related_name="books", on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.book} - {self.room}"
