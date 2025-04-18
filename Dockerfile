FROM python:3.12.4


# RUN apk update && \
#     apk add nano
RUN apt-get update && \
    apt-get install -y nano


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "sms.wsgi:application", "--bind", "0.0.0.0:8000"]

