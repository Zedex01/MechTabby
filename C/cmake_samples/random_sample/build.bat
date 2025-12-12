
@echo off
cd /D "%~dp0"

REM Build using gcc
gcc -o main main.c random.c -lm

REM Can also compile each line individually:
REM gcc -c main.c
REM gcc -c random.c
REM gcc -o main main.o random.o -lm

pause