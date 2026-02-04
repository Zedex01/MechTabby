
::Kill Other instances
::taskkill /IM chrome.exe /F

cd "C:\Program Files\Google\Chrome\Application"
:: Launch chrome in debug mode as this profile:
chrome.exe --remote-debugging-port=9222 --remote-allow-origins=* --profile-directory="Profile 2"

::Note, there is a lock on profiles for normal mode, headless overrides this.