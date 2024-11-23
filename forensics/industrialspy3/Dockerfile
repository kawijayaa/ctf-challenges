FROM python:3.8-alpine

RUN apk add --no-cache \
    socat

WORKDIR /app

COPY src/nc.py .

CMD ["socat", "TCP-LISTEN:8080,fork,reuseaddr", "EXEC:python3 nc.py"]
