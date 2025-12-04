@echo off

setlocal enabledelayedexpansion

set BACKUP_FILE=C:\Users\mmoran\Projects\Scripts\Backup.bat
set PROJECT_LIST=C:\Users\mmoran\Projects\Scripts\ProjectList.txt
set WriteToLog=C:\Users\mmoran\Projects\Scripts\WriteToLog.bat

for /f "usebackq delims=" %%P in (%PROJECT_LIST%) do (
	echo Project: %%P
	call %BACKUP_FILE% %%P
)

call %WriteToLog% "Finished All Backups"

::Forceablly close task
::SCHTASKS /End /TN "Backup Repos"
