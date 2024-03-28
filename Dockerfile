FROM python:3.12.2

WORKDIR /app

COPY . /app

CMD ["python", "practik.py"]