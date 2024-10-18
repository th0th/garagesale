FROM python:3.12-slim-bookworm

WORKDIR /app

COPY garagesale garagesale
COPY market market
COPY media media
COPY static static
COPY templates templates
COPY db.sqlite3 .
COPY manage.py .
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
