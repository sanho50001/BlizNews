import time
# from celery import shared_task
from BlizNews.celery import app
from News_app.parser import parser_main_page

# @shared_task
# def news_task(task_id=1):
#     parser_main_page()
#     time.sleep(int(task_id) * 2)
#     return True


@app.task
def news_task(task_id=1):
    # try:
    #     while True:
    #         print('Начат процесс таска ')
    #         parser_main_page()
    #         print('Отправка в сон')
    #         time.sleep(int(task_id) * 100)
    # except False:
    #     news_task()
    while True:
        print('Начат процесс таска ')
        parser_main_page()
        print('Отправка в сон')
        time.sleep(int(task_id) * 100)
