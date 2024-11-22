FROM node:18-alpine

WORKDIR /app

COPY src/web .
RUN npm install

RUN apk add nginx
COPY src/nginx.conf /etc/nginx/nginx.conf
RUN nginx -t

EXPOSE 80

CMD nginx && node app.js
