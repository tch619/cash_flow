from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
