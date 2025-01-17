# CRUD-in-the-Cloud [FastAPI]

This is a FastAPI app that I use to learn FastAPI, and Python in general.

## Features

- Python
- FastAPI
- JavaScript
- Sqlalchemy
- PostgreSQL
- Pytest
- Docker

## Dev

```sh
git clone git@github.com:hemroda/crud_in_the_cloud_fastapi.git
```

### Setup Dev environment

Set environment variables

```sh
cp ./backend/.env.sample ./backend/.env
```

- Build the new image and spin up the containers:

```sh
docker-compose up -d --build
```

Got ot `http://127.0.0.1:8000`

### Database

- Access the DB

```sh
docker-compose exec db psql --username=pguser --dbname=crud_in_the_cloud_db
```

- List the databases

```sql
crud_in_the_cloud_db=# \l
```

- Connect to `crud_in_the_cloud_db` database

```sql
crud_in_the_cloud_db=# \c crud_in_the_cloud_db
```

```sql
crud_in_the_cloud_db=# \dt
```

#### Migrations - Alembic

```sh
alembic revision --autogenerate -m "the message you want"
```

```sh
alembic upgrade head
```

#### Access pgAdmin

Go to `http://localhost:8080/login`

Use the following logins:

    - user/email: admin@users.com

    - password: adminpassword

When creating the server:
    - General tab:

        - name: server

    - Connection tab:

        - Host name/address: db

        - Username: pguser

        - Password: pguserpassword

        ⚠️ The other fields do not change


### Install new packages

```sh
 docker-compose exec backend pipenv install name_of_the_package
```

⚠️⚠️ After adding a new package, you will need to rebuild the project ⚠️⚠️

```sh
 docker-compose up -d --build
```

## Specs

* Run all the specs in Docker

```sh
docker-compose exec backend pytest -v
```

* Run a specific test file in Docker
```sh
docker-compose exec backend pytest -v test/unit/service/*.py
```

## Gotchas

* Tailwind or styles not applied
If the class you try to use is not listed in `static/css/main.css`, you need to rebuild tailwind

```sh
docker-compose exec backend npm run build:tailwind
```

You might need to clear your browsers cache if it still is not working ¯\_(ツ)_/¯


### Documentation

Got to `http://127.0.0.1:8000/doc`


## Production

### Before creating the servers

* Copy `terraform.tfvars.sample` to `terraform.tfvars` and update the values.

```sh
cp terraform.tfvars.sample terraform.tfvars
```

### Deploying in Prod for updates

* SSH to the server.
* cd into `crud_in_the_cloud_fastapi` folder
* Pull the changes, run `git pull origin main`
* Run the following commands:

```sh
docker-compose -f docker-compose.prod.yml up -d --build
```

### Renew certificate

```sh
docker-compose -f docker-compose.prod.yml run --rm certbot sh -c "certbot renew"
```
