from django.db import models


class Dog(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.PositiveSmallIntegerField('Возраст')

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return self.name
