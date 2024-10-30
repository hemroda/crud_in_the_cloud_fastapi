
# CRUD-in-the-Cloud [FastAPI]

This is a FastAPI app that I use to learn FastAPI, and Python in general.

## Features

- Python

## Dev

```sh
git clone git@github.com:hemroda/crud_in_the_cloud_fastapi.git
```

### Setup Dev environment

Set environment variables

```sh
cp ./backend/.env.dev.sample ./backend/.env
```

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

* Create your virtual environment
```sh
python -m venv .venv
```

* Activate your virtual environment
```sh
source .venv/bin/activate
```

* Install the project dependencies
```sh
pip install -r requirements.txt
```

* To run the server
```sh
uvicorn main:app --reload
```

Or

```sh
fastapi dev main.py
```

Got ot `http://127.0.0.1:8000`

- Build the new image and spin up the containers:

```sh
docker-compose up -d --build
```

### Documentation

Got to `http://127.0.0.1:8000/doc`


## Production

* To run the server
```sh
fastapi run main.py
```
