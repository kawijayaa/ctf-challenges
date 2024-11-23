FROM python:3.8-slim

WORKDIR /app

COPY src /app

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y iputils-ping --fix-missing
RUN pip install -r requirements.txt
RUN adduser --system --no-create-home app

EXPOSE 8080

USER app
CMD ["python", "main.py"]
