from django.urls import path
from .views import (
    # main,
    MainView,
    parser_news,
    # NewsDetailsView,
    news_detailed,
)

app_name = "News_app"

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('parser/', parser_news, name='parser'),

    path("main/<int:news_id>/", news_detailed, name="news_detail"),
    # path("main/<int:pk>/", NewsDetailsView.as_view(), name="news_detail"),
]
