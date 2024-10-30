# pull official base image
FROM python:3.12.7-alpine3.19

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock /usr/src/backend/

RUN pip install pipenv && \
    pipenv install --deploy --system

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/backend/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/backend/entrypoint.sh"]

# copy project
COPY . .

EXPOSE 8000

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]

# CMD ["fastapi", "run", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]