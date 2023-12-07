from django.shortcuts import render, redirect, get_object_or_404
# import News_app.tasks as task
from News_app.tasks.news_tasks import news_task
# from News_app.parser import parser_main_page
from News_app.models import Games, News, Board
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#
# def main(request):
#     board = Board.objects.all()
#     sorted_board = board.order_by('news_id').distinct()
#     context = {
#         'board': sorted_board
#     }
#     return render(request, 'News_app/index.jinja2', context=context)


class MainView(ListView):
    """Функция отображения Скидок"""
    model = Board
    template_name = "News_app/index.jinja2"
    paginate_by = 6
    context_object_name = "board"

    # def get_context_data(self, **kwargs):
    #
    #     # отправка всех объектов
    #     context = super().get_context_data(**kwargs)
    #
    #     return Board.objects.all()
    #
    # def get_queryset(self):
    #
    #     return Board.objects.order_by('news_id')


def parser_news(request):
    news_task.delay()
    # parser_main_page()

    return redirect("News_app:main")


class NewsDetailsView(DetailView):
    template_name = 'News_app/news_detail.jinja2'
    # queryset = News.objects.values()
    context_object_name = 'news'
    model = News

    def get_object(self, queryset=None):
        board = Board.objects.get(id=self.kwargs.get('pk'))
        # News.objects.filter(news_id=board.news_id).values()
        return get_object_or_404(News, pk=News.objects.filter(news_id=board.news_id))
#     def get_context_data(self, **kwargs):
#
#         # отправка всех объектов
#         context = super().get_context_data(**kwargs)
#         board = Board.objects.get(id=self.kwargs.get('pk'))
#         context['news'] = News.objects.filter(news_id=board.news_id).values()
#         return context
#
#     def get_queryset(self):
#         board = Board.objects.get(id=self.kwargs.get('pk'))
#         return News.objects.filter(news_id=board.news_id).values()
# #
def news_detailed(request, news_id):
    """
    Функция принимает news_id
    """
    board = Board.objects.get(id=news_id)
    # print('BOARD   ', board)
    # print(News.objects.filter(news_id=board.news_id))
    # print(News.objects.filter(news_id=board.news_id))
    # news = News.objects.get(news_id=board.news_id)
    context = {
        'news': News.objects.filter(news_id=board.news_id)
    }
    return render(request, 'News_app/news_detail.jinja2', context=context)
