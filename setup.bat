@echo off
echo [LIFE OS] Checking Python...
python --version
if errorlevel 1 goto NoPython

echo [LIFE OS] Creating virtual environment...
python -m venv venv

echo [LIFE OS] Activating venv...
call venv\Scripts\activate.bat

echo [LIFE OS] Installing dependencies...
pip install -r requirements.txt
pip install playwright
playwright install chromium

echo.
echo [LIFE OS] Setup Complete! 
echo.
echo To run the app:
echo 1. Keep this terminal open (venv is active)
echo 2. Run: npm run dev
echo.
pause
exit /b

:NoPython
echo [ERROR] Python not found. Please install Python 3.10 or higher.
pause
