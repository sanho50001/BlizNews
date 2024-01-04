FROM python:3.10

#WORKDIR /app

ENV HOME=/app
ENV APP_HOME=/app/web
WORKDIR $HOME
COPY ./requirements.txt requirements.txt
#
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/static
#
#
#RUN mkdir $APP_HOME/media
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "BlizNews.wsgi:application", "--bind", "0.0.0.0:8000"]

ADD . /app/



#CMD ["python", "manage.py", "createsuperuser", "admin", "admin"]