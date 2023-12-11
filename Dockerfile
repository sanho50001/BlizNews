FROM python:3.10

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app/
CMD #!/bin/bash
set -e
DB_NAME=${1:-BlizNewsUser}
DB_USER=${2:-BlizNewsDB}
DB_USER_PASS=${3:-1}
sudo su postgres
createdb  $DB_NAME;
psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_USER_PASS';"
psql -c "grant all privileges on database $DB_NAME to $DB_USER;"
echo "Postgres User '$DB_USER' and database '$DB_NAME' created."
CMD ["python", "manage.py", "runserver", "127.0.0.0:8000"]
CMD ["python", "manage.py", "createsuperuser", "admin", "admin"]