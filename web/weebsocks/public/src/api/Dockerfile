FROM golang:1.23-alpine

WORKDIR /app
COPY . .

RUN go mod tidy
RUN go build -o api

EXPOSE 8080

CMD ./api
