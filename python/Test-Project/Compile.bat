REM For a single script compilation, 
REM 	simply run 'pyinstaller --onefile <python_file>.py'

cd "%~dp0"
pyinstaller --onefile --noconsole src/Test.py
pause
