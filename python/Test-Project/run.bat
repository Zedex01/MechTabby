@Echo off
REM goto directory containing .bat file
cd "%~dp0" 
echo "%~dp0"
"C:/SDKs/Python/Python313/python.exe" src/Test.py
pause