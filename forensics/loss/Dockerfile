FROM node:20-alpine

WORKDIR /app

COPY src/server .
COPY src/git git/

RUN npm install

CMD ["node", "index.js"]
