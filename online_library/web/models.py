from django.db import models

class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length = FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length = LAST_NAME_MAX_LENGTH,
    )

    image_url = models.URLField(
        verbose_name = 'Image URL',
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name
''' 
•	Book
o	title - Character field with max length of 30 characters
o	description - Text field
o	image - URL field
o	type - Character field with max length of 30 characters
'''
class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH,)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=TYPE_MAX_LENGTH,)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title