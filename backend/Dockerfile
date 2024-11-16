# Build stage for Tailwind CSS
FROM node:20-alpine AS css-builder
WORKDIR /app
# Copy package files
COPY package.json package-lock.json ./
# Install dependencies (ignore optional deps)
RUN npm install --no-optional
# Copy source files needed for build
COPY static ./static
COPY tailwind.config.js ./
# Build CSS
RUN npm run build:css

# Main Python application stage
FROM python:3.12.7-alpine3.19

# create the cruder user
RUN addgroup -S crudergroup && adduser -S cruder -G crudergroup

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV HOME=/usr/src
ENV APP_HOME=/usr/src/backend

# set work directory
WORKDIR $APP_HOME

# create the appropriate directories
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --deploy --system

# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . .

# Copy the compiled CSS from the build stage
COPY --from=css-builder /app/static/css/main.css ./static/css/

# chown all the files to the app user
RUN chown -R cruder:crudergroup $APP_HOME

# change to the cruder user
USER cruder

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
