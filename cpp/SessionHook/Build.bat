@echo off
 
cd /d %~dp0

::clean old build
IF EXIST SessionHook.exe ( del SessionHook.exe )

::build
g++ -m64 main.cpp -o SessionHook.exe -lwtsapi32


if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)