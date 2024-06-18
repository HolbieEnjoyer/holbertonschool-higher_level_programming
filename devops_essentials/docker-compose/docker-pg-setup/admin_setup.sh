#!/bin/bash

# Replace with your pgAdmin credentials
PGADMIN_EMAIL="admin@example.com"
PGADMIN_PASSWORD="admin"

# Step 1: Authenticate and obtain login token
echo "Logging in to pgAdmin..."
LOGIN_RESPONSE=$(curl --silent --request POST \
                     --url http://localhost:8080/login \
                     --header 'Content-Type: application/json' \
                     --data "{\"email\":\"$PGADMIN_EMAIL\",\"password\":\"$PGADMIN_PASSWORD\"}")

TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r .access_token)
if [ -z "$TOKEN" ]; then
  echo "Failed to obtain authentication token. Exiting."
  exit 1
fi

echo "Login successful. Token: $TOKEN"

# Step 2: Retrieve list of servers
echo "Fetching list of servers..."
SERVERS_RESPONSE=$(curl --silent --request GET \
                        --url http://localhost:8080/servers \
                        --header "Authorization: Bearer $TOKEN")

echo "Current servers:"
echo "$SERVERS_RESPONSE"

# Step 3: Add a new server (adjust parameters as necessary)
echo "Adding new server..."
ADD_SERVER_RESPONSE=$(curl --silent --request POST \
                            --url http://localhost:8080/servers \
                            --header 'Content-Type: application/json' \
                            --header "Authorization: Bearer $TOKEN" \
                            --data '{
                              "name": "My PostgreSQL Server",
                              "host": "db",  // Replace with your PostgreSQL service name
                              "port": 5432,
                              "username": "myuser",
                              "password": "mypassword",
                              "database": "mydatabase",
                              "ssl_mode": "prefer"
                            }')

echo "Server added:"
echo "$ADD_SERVER_RESPONSE"

echo "Setup complete."
