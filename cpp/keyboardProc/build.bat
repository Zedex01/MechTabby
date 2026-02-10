@echo off

cd /d %~dp0

::clean old build
IF EXIST main.exe ( del main.exe )
IF EXIST data\out.json ( del data\out.json )

::build
g++ -m64 main.cpp -o main.exe

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)