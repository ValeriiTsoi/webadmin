FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Т.к. build-context теперь ./backend — здесь лежит requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код backend внутрь образа
COPY . /app

ENV DJANGO_SETTINGS_MODULE=webadmin.settings

# collectstatic — опционально (не требует БД); если не нужен — можно закомментить
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000
CMD ["gunicorn", "webadmin.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
