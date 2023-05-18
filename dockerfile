FROM python:3.11 as builder

WORKDIR /app

COPY . .
RUN apt-get update && \
    python -m pip install -r requirements.txt

CMD ["python", "./main.py"]

