@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Running tests...
pytest --tb=short --disable-warnings

pause
