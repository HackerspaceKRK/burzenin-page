#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Error: Two arguments are required."
  echo "Usage: $0 <callsign> <name>"
  exit 1
fi

# Assign the arguments to variables
CALLSIGN=$1
NAME=$2
CALLSIGN_UPPER=$(echo "$CALLSIGN" | tr '[:lower:]' '[:upper:]')

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$0")

# Define the path to the _authors and _data directories
AUTHORS_DIR=$(realpath "$SCRIPT_DIR/../_authors")
DATA_DIR=$(realpath "$SCRIPT_DIR/../_data")

# Perform the sed command with the provided callsign
sed "s/changeme/$CALLSIGN/g" "$SCRIPT_DIR/author_template.md" > "$AUTHORS_DIR/$CALLSIGN.md"
echo "File has been processed and saved as $AUTHORS_DIR/$CALLSIGN.md"

# Define the snippet to be added
SNIPPET=$(cat <<EOF

## begin $CALLSIGN
$CALLSIGN:
  name              : $NAME
  avatar            : "/assets/images/zjazd.png"
  callsign          : $CALLSIGN_UPPER
  constructor       : yes

## end $CALLSIGN
EOF
)

# Append the snippet to the end of _data/authors.yml
echo "$SNIPPET" >> "$DATA_DIR/authors.yml"
echo "Snippet has been added to $DATA_DIR/authors.yml"