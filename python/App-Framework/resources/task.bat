@echo off
setlocal enabledelayedexpansion

for /L %%i in (0,1,100) do (
    echo %%i%%%
    TIMEOUT /T 0.2 /NOBREAK > nul
)