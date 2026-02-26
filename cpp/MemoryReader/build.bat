@echo off

cd /d %~dp0

::clean old build
IF EXIST MemReader.exe ( del MemReader.exe )

::Build
g++ -m64 main.cpp -o MemReader.exe -lcomctl32 -ldwmapi

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)