FROM node:16-alpine as builder

WORKDIR /app

# copy all files
COPY . .

# clean install dependencies
RUN npm ci

# build application
RUN npm run build

# Nginx config
FROM nginx

COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
