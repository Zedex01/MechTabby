@echo off

cd /d %~dp0

::clean old build
IF EXIST race.exe ( del race.exe )

::build
g++ -m64 main.cpp -o race.exe

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)