@echo off

cd /d %~dp0

::clean old build
IF EXIST main.exe ( del main.exe )

echo Building...
::build Main
g++ -m64 main.cpp -o main.exe

echo Build Success!
echo ===============================

