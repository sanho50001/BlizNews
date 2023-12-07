import requests
from bs4 import BeautifulSoup
from News_app.models import Games, News, Board
import time
import urllib3
import re


def parser_main_page(url='https://www.wowhead.com/ru'):
    """Парсер начальной страницы wowhead"""
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print('Начат процесс парсера | Запуск парсера по гл.странице')
    result = requests.get(url=url, verify=False)
    time.sleep(1)
    soup = BeautifulSoup(result.text, 'lxml')
    products = soup.find_all('div', class_='news-list-card')
    for product in products:
        time.sleep(1)
        parser_main_page_info(product)


def parser_main_page_info(product):
    """Парсер начальной страницы wowhead"""
    games = Games()

    news_id = product.get('id')
    game_type = product.find(class_='news-list-card-type fa fa-thumb-tack').text
    title = product.find('h3', class_='heading-size-2')
    title_url = product.findNext().get('href') \
        if 'www.wowhead.com' in str(product.findNext().get('href')) \
        else ('https://www.wowhead.com' + str(product.findNext().get('href'))
              if not product.findNext().get('href') == None
              else 'Пусто')
    time.sleep(1)
    title_text = title.text
    news_image_url = product.findNext().get('style')[22:-1]
    description_text = product.find('div', class_='news-list-card-content-body').text
    time.sleep(1)

    parse_data = parser_page(url=title_url)

    game_name = game_type.strip()

    time.sleep(1)
    if Games.objects.filter(name_game=game_name).exists() != True:
        games.name_game = game_name
        games.save()
    name_game = Games.objects.get(name_game=game_name)
    if news_id in Board.objects.filter(news_id=news_id):
        return print('Конец парсера | Найдено сходство')
    else:
        board = Board(
            game=name_game,
            news_id=news_id,
            text_first=title_text,
            text_second=description_text,
            board_image_url=news_image_url
        )
        board.save()

    if news_id in News.objects.filter(news_id=news_id):
        return print('Конец парсера | Найдено сходство')
    else:
        news = News(
            game=name_game,
            news_id=news_id,
            title=title_text,
            text=parse_data,
            news_image_url=news_image_url,
            original_news=title_url
        )
        news.save()

    print('Конец парсера | Завершение')
    return


def parser_page(url):
    """Парсер страницы wowhead"""
    # stopwords = {'<div class="quote-box"'
    #              ' data-type="blizzard">'
    #              ' <div class="quote-header"> </div> <div class="quote-body">',
    #              '<br>', '</br>',
    #              '<i>', '</i>',
    #              '<ul>', '</ul>',
    #              '<li>', '</li>',
    #              '<tr>', '</tr>',
    #              'h', '<h>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<h7>', '<h8>', '<h9>',
    #              'h', '</h>', '</h1>', '</h2>', '</h3>', '</h4>', '</h5>', '</h6>', '</h7>', '</h8>', '</h9>',
    #              'a', 'href', 'https', 'www', 'wowhead', 'com', 'client', 'Wowhead',
    #              'Client',  'br', 'li', 'ul', 'i'
    #              }
    stopwords = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    result = requests.get(url=url)
    soup = BeautifulSoup(result.text, 'lxml')
    products = soup.find_all('div', class_='news-post-content')
    texted = ''
    for product in products:
        time.sleep(1)
        text = product.findNext('noscript')
        for t in text:
            time.sleep(1)

            texted += str(t)
            # texted += str(list(str(word) for word in re.split("\W+", str(t)) if str(word.lower()) not in stopwords))
    cleartext = re.sub(stopwords, '', texted)
    print('Парсер страницы закончен. Переход к следующей')
    return cleartext
