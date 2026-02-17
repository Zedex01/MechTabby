@echo off

cd /d %~dp0

::clean old build
IF EXIST KeyReader.exe ( del KeyReader.exe )
IF EXIST obj\appres.o ( del obj\appres.o )
IF EXIST fileout ( del fileout )

::Icon
IF NOT EXIST obj (mkdir obj)
windres res\app.rc -O coff obj\appres.o

::Build
g++ -m64 main.cpp obj\appres.o -o KeyReader.exe

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)