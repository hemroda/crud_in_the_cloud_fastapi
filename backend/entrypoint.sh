#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "$(date) - Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT..."

    timeout=30
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
        timeout=$((timeout - 1))
        if [ $timeout -le 0 ]; then
            echo "$(date) - PostgreSQL did not start in time!"
            exit 1
        fi
    done

    echo "$(date) - PostgreSQL started successfully!"
fi

echo "$(date) - Running Alembic migrations..."
if ! alembic upgrade head; then
    echo "$(date) - Alembic migration failed!"
    exit 1
fi
echo "$(date) - Alembic migrations applied successfully!"

echo "$(date) - Starting the application..."
exec "$@"
