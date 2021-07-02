FROM python:3.7

RUN mkdir -p /survey
WORKDIR /survey
ADD . .
RUN apt-get update && apt-get install -y gcc python3-dev locales locales-all gettext libmagic-dev && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8020