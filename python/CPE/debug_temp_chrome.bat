
::Kill Other instances
::taskkill /IM chrome.exe /F

:: If being ran from another drive, first change to c
c:

cd "C:\Program Files \Google\Chrome\Application"
::cd "C:\Program Files (x86)\Google\Chrome\Application"

:: Launch chrome in debug mode as this profile:
chrome.exe --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir="C:\.TempProfile"

::"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"