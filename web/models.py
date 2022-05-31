from django.db import models


class Book(models.Model):
    date = models.DateField(verbose_name='Дата проиведения')
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='books', blank=True, verbose_name='Изображение')
    file = models.FileField(upload_to='books_files', blank=True, verbose_name='Файл книги')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.title


class Simphony(models.Model):
    date = models.DateField(verbose_name='Дата симфонии')
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='books', blank=True, verbose_name='Изображение')
    file = models.FileField(upload_to='books_files', blank=True, verbose_name='Файл книги')

    class Meta:
        verbose_name = 'Симфония'
        verbose_name_plural = 'Симфонии'

    def __str__(self):
        return self.title


class Foto(models.Model):
    date = models.DateField(verbose_name='Дата фотографии')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    image = models.ImageField(upload_to='gallery', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name


class Women(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    image = models.ImageField(upload_to='womens', verbose_name='Музы')

    class Meta:
        verbose_name = 'Муза'
        verbose_name_plural = 'Музы'

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.CharField(max_length=250, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.author


class Voice(models.Model):
    author = models.CharField(max_length=250, verbose_name='Автор')
    audio = models.FileField(upload_to='voices', verbose_name='Аудио (100 голосов)')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.author

