@echo off

cd /d %~dp0
@echo on
::clean old build
IF EXIST payload.dll ( del payload.dll )
IF EXIST injector.exe ( del injector.exe )

::build dll
g++ -m64 payload.cpp -shared -o payload.dll

::build Main
g++ -m64 injectorDll.cpp -o injector.exe
