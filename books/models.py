# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    publisher = models.CharField(u'Издательство', max_length=64, null='True', blank='True')
    pub_year = models.IntegerField(u'Год публикации')

    def __str__(self):
        return self.name + " " + self.author
