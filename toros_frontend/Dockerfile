FROM node:18-alpine

ENV NEXT_TELEMETRY_DISABLED 1

WORKDIR /app

# Copy lock files if file exists
COPY package.json yarn.lock* .

RUN yarn install

COPY src ./src
COPY public ./public
COPY next.config.js .
COPY tsconfig.json .

CMD yarn dev