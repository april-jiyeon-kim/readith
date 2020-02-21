from django.db import models
from core import models as core_models

class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Genre(AbstractItem):

    """ Genre Object Definition """

    class Meta:
        verbose_name_plural = "Genres"


class Book(core_models.TimeStampedModel):

    """ Book Model Definition """

    title = models.CharField(max_length=140)
    description = models.TextField()
    author = models.CharField(max_length=140)
    published_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="books", blank=True)

    
    def __str__(self):
        return self.title