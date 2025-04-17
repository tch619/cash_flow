from django.db import models
from common.models import BaseModel
from django.utils import timezone


class EntryCashFlow(models.Model):
    created_at = models.DateField(default=timezone.now().date, verbose_name='Время создания')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='Тип')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, verbose_name='Подкатегория')
    sum = models.IntegerField(verbose_name='Сумма в рублях')
    comment = models.CharField(max_length=150, verbose_name='Комментарий', null=True, blank=True)

    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'


class Status(BaseModel):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(BaseModel):
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(BaseModel):
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='categories', verbose_name='Тип')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
