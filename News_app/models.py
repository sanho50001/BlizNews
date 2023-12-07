from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Games(models.Model):
    """Модель Игр"""
    name_game = models.CharField(max_length=500, verbose_name=_('name game'))

    class Meta:
        verbose_name = _('Games')
        verbose_name_plural = _('Games')

    def __str__(self):
        return str(self.name_game)


def file_news_directory_path(instance: 'News', filename: str) -> str:
    """Фукнция директории превью пользователя
    возвращает айди профиля и имя файла

    """
    return 'news/news_{pk}/file_news/{filename}'.format(
        pk=instance.pk,
        filename=filename
    )


class News(models.Model):
    """Модель Новостей"""
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='game_news')
    title = models.CharField(max_length=500, blank=True, verbose_name=_('title'))
    text = models.TextField(max_length=500, blank=True, verbose_name=_('text'))
    news_id = models.CharField(max_length=500, blank=True, unique=True,  verbose_name=_('news_id'))
    file_news = models.FileField(null=True, blank=True, upload_to=file_news_directory_path, verbose_name=_('file news'))
    news_image_url = models.CharField(max_length=500, blank=True, verbose_name=_('news image url'))
    created = models.DateField(
        auto_now_add=True, verbose_name=_("data created")
    )
    original_news = models.CharField(max_length=500, blank=True, verbose_name=_('original news'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return str(self.id) + ' News ' + str(self.game)


def file_newsimages_directory_path(instance: 'NewsImages', filename: str) -> str:
    """Фукнция директории превью пользователя
    возвращает айди профиля и имя файла

    """
    return 'news/news_{pk}/file_news/{filename}'.format(
        pk=instance.news.pk,
        filename=filename,
    )


class NewsImages(models.Model):
    """Модель Фото новостей"""
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    file_news_images = models.FileField(
        null=True,
        blank=True,
        upload_to=file_news_directory_path,
        verbose_name=_('file news image')
    )
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    def get_absolute_url(self):
        return reverse('main_app:newsview', args=[self.id])


def file_board_directory_path(instance: 'Board', filename: str) -> str:
    """Фукнция директории превью пользователя
    возвращает айди профиля и имя файла

    """
    return 'board/board_{pk}/file_board/{filename}'.format(
        pk=instance.pk,
        filename=filename
    )


class Board(models.Model):
    """Модель борда"""
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='game_board')
    news_id = models.CharField(max_length=500, blank=True, unique=True, verbose_name=_('news_id'))
    text_first = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('first text'))
    text_second = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('second text'))
    file_board = models.FileField(null=True, blank=True,
                                  upload_to=file_board_directory_path, verbose_name=_('file board'))
    board_image_url = models.CharField(max_length=500, blank=True, verbose_name=_('board image url'))
    created = models.DateField(
        auto_now_add=True, verbose_name=_("data created")
    )

    class Meta:
        verbose_name = _('board')
        verbose_name_plural = _('board')

    def __str__(self):
        return str(self.id) + ' Board ' + str(self.game)
    #
    # def save(self, *args, **kwargs):
    #     obj = Board.objects.filter(news_id=self.news_id)
    #     for count, _ in enumerate(obj):
    #         if count > 1:
    #             obj.first().delete()
    #         else:
    #             super().save()
