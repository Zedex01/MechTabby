
::Kill Other instances
taskkill /IM chrome.exe /F

cd "C:\Program Files\Google\Chrome\Application"

:: Launch chrome in debug mode as this profile:
chrome.exe --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir="C:\.TempProfile"

