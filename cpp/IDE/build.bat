@echo off
 
cd /d %~dp0

::clean old build
IF EXIST IDE.exe ( del IDE.exe )
IF EXIST obj\appres.o ( del obj\appres.o )

::Icon
IF NOT EXIST obj (mkdir obj)
windres res\app.rc -O coff obj\appres.o

::build
g++ -m64 -mwindows -municode  -Ires main.cpp obj\appres.o -o IDE.exe ^
-lcomctl32 -ldwmapi

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)