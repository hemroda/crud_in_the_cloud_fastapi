# pull official base image
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

# install psycopg2 dependencies and Node.js
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev npm

# install Python dependencies
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock $APP_HOME
RUN pip install pipenv && \
    pipenv install --deploy --system

# copy package.json and package-lock.json
COPY package.json package-lock.json $APP_HOME/

# install Node.js dependencies
RUN npm install

# copy the rest of the project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R cruder:crudergroup $APP_HOME

# change to the cruder user
USER cruder

EXPOSE 8000

# run entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
