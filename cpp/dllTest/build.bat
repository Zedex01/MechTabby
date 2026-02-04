@echo off

cd /d %~dp0

::clean old build
IF EXIST myLibrary.dll ( del myLibrary.dll )
IF EXIST main.exe ( del main.exe )

::build dll
g++ myLibrary.cpp -shared -o myLibrary.dll

::build Main
g++ main.cpp -o main.exe