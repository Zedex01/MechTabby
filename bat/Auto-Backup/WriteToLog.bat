::Matthew Moran 2025 05 26
::File that writes to a log
::Usage: call WriteToLog.bat <content>

@echo off
::===Config====
set LOG_FILE=C:\Users\mmoran\Projects\Scripts\log.csv


:: Get current date and time (format: yyyy-MM-dd, HH:mm:ss)
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set DATE=%%i
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format HH:mm:ss"') do set TIME=%%i

::Combine and append to log:
echo %DATE%,%TIME%,%~1 >> %LOG_FILE% 


