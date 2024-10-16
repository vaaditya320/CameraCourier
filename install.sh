#!/bin/bash

# Check for Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it first."
    exit 1
fi

# Check for pip installation
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install it first."
    exit 1
fi

# Create a virtual environment (optional but recommended)
echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip3 install opencv-python Pillow python-dotenv

# Notify the user
echo "All dependencies have been installed successfully!"
echo "Remember to activate the virtual environment using 'source venv/bin/activate' before running the application."
