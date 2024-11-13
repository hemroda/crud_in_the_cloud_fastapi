
# CRUD-in-the-Cloud [FastAPI]

This is a FastAPI app that I use to learn FastAPI, and Python in general.

## Features

- Python
- FastAPI
- JavaScript
- PostgreSQL
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

## Specs

* Run all the specs in Docker

```sh
docker-compose exec backend pytest -v
```

* Run a specific test file in Docker
```sh
docker-compose exec backend pytest -v test/unit/service/*.py
```

### Documentation

Got to `http://127.0.0.1:8000/doc`


## Production

* To run the server
```sh
fastapi run main.py
```

* Copy `terraform.tfvars.sample` to `terraform.tfvars` and update the values.

```sh
cp terraform.tfvars.sample terraform.tfvars
```
