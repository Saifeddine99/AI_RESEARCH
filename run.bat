@echo off
echo Starting AI Research Project...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.x from https://www.python.org/downloads/
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install requirements
pip install -r requirements.txt

:: Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    echo API_KEY=your_gemini_api_key_here > .env
    echo Please edit .env file and add your Gemini API key
)

:: Run the application
streamlit run app.py

pause 