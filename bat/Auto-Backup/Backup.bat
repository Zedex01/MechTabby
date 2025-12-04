::Needs to be a universal file that I can add to a lot of projects easily
@echo off

::NOTE: ONCE THE FILES HAS BEEN CHANGED IT NEEDS TO RUN AS ADMIN TO ENABLE SYNCING WITH G DRIVE!!

::Creates a local enviornment, ie, Env variables created only apply in the script instance
::setlocal enabledelayedexpansion

::set PROJECT_NAME=TestProject
set PROJECT_NAME=%1
::echo ==========%PROJECT_NAME%=============

::=== Config ===
set PROJECT_PATH=C:\Users\mmoran\Projects\%PROJECT_NAME%
set BACKUP_PATH="G:\My Drive\Project-Repo-Backups\%PROJECT_NAME%"
set WriteToLog=C:\Users\mmoran\Projects\Scripts\WriteToLog.bat
set ERROR_FILE=%TEMP%\git_error.log

::==Init Var==
set OUTPUT=

::Strip Quotes
set BUNDLE_DIR=%BACKUP_PATH:"=%


::======================= Check for old backups =========================================
set LATEST_BUNDLE=
set LATEST_BUNDLE_HASH=
set HAS_BUNDLES=0
set FOUND_HASH=0

cd /d "%PROJECT_PATH%"

:: Check if current directory is a git repo
git rev-parse --is-inside-work-tree >nul 2>&1

if errorlevel 1 (
	powershell -Command "Write-Host 'Backup Failed: Not a git repository' -ForegroundColor Red"
	set OUTPUT="Backup Failed: Not a git repository"
	::call %WriteToLog% %CONTENT%
	goto :END
)

::Find if any old backups:
echo Checking for old backups of %PROJECT_NAME%...
::call %WriteToLog% Checking for old backups of %PROJECT_NAME%...

::Find most recent backup
for /f %%F in ('dir /b /a-d /o-d "%BUNDLE_DIR%\*.bundle"') do (
    set LATEST_BUNDLE=%%F
    goto :FoundBundle
)
goto :MakeBackup

:FoundBundle
::echo locating hash of backup for %PROJECT_NAME%...
::Get Hash from most recent commit
for /f "tokens=1" %%i in ('git bundle list-heads "%BUNDLE_DIR%\%LATEST_BUNDLE%"') do (
    set "LATEST_BUNDLE_HASH=%%i"
    goto :GetHeadHash
)
echo hash not found.
goto :MakeBackup

:GetHeadHash


::Get Hash of current Head
set CURRENT_HEAD_HASH=
for /f %%H in ('git rev-parse HEAD') do set CURRENT_HEAD_HASH=%%H

::Compare Local to most recent bundle hash
if %CURRENT_HEAD_HASH% == %LATEST_BUNDLE_HASH% (
	::echo HASHES MATCH: Backup already up to date
	powershell -Command "Write-Host 'Backup already up to date: %LATEST_BUNDLE%' -ForegroundColor Green"
	set OUTPUT="Backup already up to date: %LATEST_BUNDLE%"
	goto :END
	
) else (
	echo HASHES DO NOT MATCH:
	goto :MakeBackup
)


:MakeBackup
echo Making Backup of: %PROJECT_NAME%...
::call %WriteToLog% Making Backup of: %PROJECT_NAME%...
::Get current date and time
for /f %%i in ('pwsh -NoProfile -Command "Get-Date -Format yyyy-MM-dd"')do set DATE=%%i

set BUNDLE_FILE=%BUNDLE_DIR%\%PROJECT_NAME%-backup-%DATE%.bundle

REM echo checking for backupfolder...
REM echo %BACKUP_PATH%
::Make sure backupfolder exists
if not exist %BACKUP_PATH% (
	mkdir %BACKUP_PATH%
)

REM CREATING BUNDLE...
REM echo BUNDLE: %BUNDLE_FILE%
::Create the git bundle with all history
REM %ERROR_FILE%
git bundle create "%BUNDLE_FILE%" --all 2>&1 
echo %ERRORLEVEL%
::set GIT_ERROR=
::set /p GIT_ERROR=<%ERROR_FILE%

:: check if any errors arrose
if errorlevel 1 (
	echo %ERRORLEVEL%
	powershell -Command "Write-Host 'Backup Failed: %GIT_ERROR%' -ForegroundColor Red"
	set OUTPUT="Backup Failed: %GIT_ERROR%"
) else (
	::set CONTENT= "Backup Complete: %BUNDLE_FILE%"
	powershell -Command "Write-Host 'Backup Complete: %BUNDLE_FILE%' -ForegroundColor Green"
	set OUTPUT="Backup Complete: %BUNDLE_FILE%"
)

:END
::Write Output to log
call %WriteToLog% %OUTPUT%
