@echo off

cd /d %~dp0

::clean old build
IF EXIST KeyProc.exe ( del KeyProc.exe )
IF EXIST obj\appres.o ( del obj\appres.o )
IF EXIST data\out.json ( del data\out.json )

::Icon
IF NOT EXIST obj (mkdir obj)
windres res\app.rc -O coff obj\appres.o

::build
g++ -m64 main.cpp obj\appres.o -o KeyProc.exe

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)