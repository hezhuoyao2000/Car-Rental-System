#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Initializing database and running the main program..."
python3 src/main.py

echo "Current directory: $(pwd)"
echo "Virtual environment activated: $VIRTUAL_ENV"

echo "Press any key to exit..."
read -n 1 -s
