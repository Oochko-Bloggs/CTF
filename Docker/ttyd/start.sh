#!/bin/bash

# Get the username from QUERY_STRING
username=$(echo "$QUERY_STRING" | sed -n 's/.*username=\([^&]*\).*/\1/p')

# If no username passed, use default
if [ -z "$username" ]; then
    username="unknown_user"
fi

# Just print username and start bash
script log
echo "Welcome $username!"
exec bash
