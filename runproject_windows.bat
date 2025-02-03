@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate



echo Initializing database and running the main program...
python src/main.py

echo.
echo Current directory: %cd%
echo Virtual environment activated: %VIRTUAL_ENV%

pause