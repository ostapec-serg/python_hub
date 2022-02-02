from django.db import models


class Job(models.Model):
    id_story = models.IntegerField('Story identificator', default=0, unique=True)
    by = models.CharField('Author', max_length=200)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    text = models.TextField(default='No content')
    time = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    url = models.URLField(default='No content')


class Ask(models.Model):
    id_story = models.IntegerField('Story identificator', default=0, unique=True)
    by = models.CharField('Author', max_length=200)
    score = models.IntegerField(default=0)
    descendants = models.IntegerField(default=0)
    kids = models.TextField(default='No content')
    title = models.CharField(max_length=300)
    text = models.TextField(default='No content')
    time = models.CharField(max_length=30)
    type = models.CharField(max_length=20)


class New(models.Model):
    id_story = models.IntegerField('Story identificator', default=0, unique=True)
    by = models.CharField('Author', max_length=200)
    score = models.IntegerField(default=0)
    descendants = models.IntegerField(default=0)
    kids = models.TextField(default='No content')
    title = models.CharField(max_length=300)
    text = models.TextField(default='No content')
    time = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    url = models.URLField(default='No content')


class Show(models.Model):
    id_story = models.IntegerField('Story identificator', default=0, unique=True)
    by = models.CharField('Author', max_length=200)
    score = models.IntegerField(default=0)
    descendants = models.IntegerField(default=0)
    kids = models.TextField(default='No content')
    title = models.CharField(max_length=300)
    text = models.TextField(default='No content')
    time = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    url = models.URLField(default='No content')
