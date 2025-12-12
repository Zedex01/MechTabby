@echo off
cd /D "%~dp0"

REM Build using gcc
gcc -o main main.c

pause
