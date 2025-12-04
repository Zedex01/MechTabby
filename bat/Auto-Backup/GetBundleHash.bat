::DoNotSetLocal

@echo off
cd /d C:\Users\mmoran\Projects\Scripts
::set BUNDLE_DIR=%1
::===
set BUNDLE_DIR="G:\My Drive\Project-Repo-Backups\TestProject"
::===
::Strip Quotes
set BUNDLE_DIR=%BUNDLE_DIR:"=%

echo BUNDLE_DIR: %BUNDLE_DIR%

::Reset Variables
set LATEST_BUNDLE=
set LATEST_BUNDLE_HASH=

::Find most recent bundle

for /f %%F in ('dir /b /a-d /o-d "%BUNDLE_DIR%\*.bundle"') do (
	echo %%F
    set LATEST_BUNDLE=%%F
    goto :found
)
:found

if not defined LATEST_BUNDLE (
	echo No bundles found!
	pause
	exit /b 1001 ::Returns with error code 1001, no other bundles
)

::Get Hash from most recent commit
for /f "tokens=1" %%i in ('git bundle list-heads "%BUNDLE_DIR%\%LATEST_BUNDLE%"') do (
    set "LATEST_BUNDLE_HASH=%%i"
    goto :afterLoop
)
:afterLoop

if not defined LATEST_BUNDLE_HASH (
	echo Unable to get bundle HASH!
	exit /b 1002 ::Returns with error code 1002, no Hash found
)

echo BND_HASH: %LATEST_BUNDLE_HASH%

pause