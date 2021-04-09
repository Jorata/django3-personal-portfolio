from django.db import models


class BlogProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.title
