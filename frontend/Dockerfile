FROM node:20-alpine

# create the cruder user
RUN addgroup -S crudergroup && adduser -S cruder -G crudergroup

# set environment variables
ENV HOME=/usr/src
ENV APP_HOME=/usr/src/frontend

# set work directory
WORKDIR $APP_HOME

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
