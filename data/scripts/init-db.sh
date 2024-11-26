#!/bin/bash
set -e

echo "Starting database initialization for DATA..."
echo "Database name: $POSTGRES_DB"
echo "User: $POSTGRES_USER"

# Check if dump file exists
if [ ! -f "/docker-entrypoint-initdb.d/data.dump" ]; then
    echo "ERROR: Dump file not found!"
    exit 1
fi

# Attempt to restore the dump file
pg_restore \
    -v \
    --no-owner \
    --no-privileges \
    -U $POSTGRES_USER \
    -d $POSTGRES_DB \
    /docker-entrypoint-initdb.d/data.dump || {
    echo "ERROR: Failed to restore database dump"
    exit 1
}

echo "Database initialization completed successfully"

