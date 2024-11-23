FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

RUN addgroup -g 1001 compfest16
RUN adduser -u 1001 -G compfest16 -D compfest16
RUN mkdir /app/uploads
RUN chown -R compfest16:compfest16 /app/uploads

RUN echo "bro this is not an IDOR challenge :v" > /app/uploads/1
RUN chown root:root /app/uploads/1
RUN chmod 0444 /app/uploads/1

RUN crontab /app/cleanup

EXPOSE 3000
CMD crond && su compfest16 -c 'npm start'
