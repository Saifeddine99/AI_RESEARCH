#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to handle Windows-specific commands
run_windows() {
    echo "Detected Windows OS"
    
    # Check if Python is installed
    python --version >/dev/null 2>&1 || {
        echo "Python is not installed. Please install Python 3.x from https://www.python.org/downloads/"
        exit 1
    }

    # Create and activate virtual environment
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python -m venv venv
    fi
    
    # Activate virtual environment
    source venv/Scripts/activate || {
        echo "Failed to activate virtual environment"
        exit 1
    }

    # Install requirements
    pip install -r requirements.txt

    # Run the application
    streamlit run app.py
}

# Function to handle Unix-based systems (macOS and Linux)
run_unix() {
    echo "Detected Unix-based OS (macOS/Linux)"
    
    # Check if Python is installed
    if ! command_exists python3; then
        echo "Python 3 is not installed. Please install Python 3.x"
        exit 1
    }

    # Create and activate virtual environment
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate || {
        echo "Failed to activate virtual environment"
        exit 1
    }

    # Install requirements
    pip install -r requirements.txt

    # Run the application
    streamlit run app.py
}

# Check if .env file exists, if not create it
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    echo "API_KEY=your_gemini_api_key_here" > .env
    echo "Please edit .env file and add your Gemini API key"
fi

# Detect OS and run appropriate function
case "$(uname -s)" in
    CYGWIN*|MINGW*|MSYS*)
        # Windows
        run_windows
        ;;
    Darwin)
        # macOS
        run_unix
        ;;
    Linux)
        # Linux
        run_unix
        ;;
    *)
        echo "Unsupported operating system"
        exit 1
        ;;
esac 