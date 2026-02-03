
::Kill Other instances
taskkill /IM chrome.exe /F

cd "C:\Program Files\Google\Chrome\Application"
:: Launch chrome in debug mode as this profile:
chrome.exe --remote-debugging-port=9222 --headless --profile-directory="Profile 1"

::Note, there is a lock on profiles for normal mode, headless overrides this.