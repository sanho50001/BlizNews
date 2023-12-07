from django.contrib import admin
from News_app.models import Games, News, Board
from django import forms


class GamesAdminForm(forms.ModelForm):
    """Форма для модели Games"""
    class Meta:
        model = Games
        fields = "__all__"


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    """Админ панель модель Games"""

    list_display = [
        "name_game"
    ]
    form = GamesAdminForm


class NewsAdminForm(forms.ModelForm):
    """Форма для модели News"""
    class Meta:
        model = News
        fields = "__all__"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Админ панель модель News"""

    list_display = [
        'id',
        "game",
        "news_id"
    ]
    form = NewsAdminForm


class BoardAdminForm(forms.ModelForm):
    """Форма для модели Board"""
    class Meta:
        model = Board
        fields = "__all__"


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """Админ панель модель Board"""

    list_display = [
        'id',
        "game",
        "news_id"
    ]
    form = BoardAdminForm

