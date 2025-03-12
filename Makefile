install:
	pip install -r requirements.txt

test: install
	pytest --tb=short --disable-warnings

build: test
	pyinstaller --onefile --icon=icon.ico Lab2.py
