FROM node:18-alpine

WORKDIR /app

RUN apk update
RUN apk add --no-cache zlib-dev udev nss ca-certificates
RUN apk add --no-cache chromium

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 9999

CMD ["npm", "start"]
