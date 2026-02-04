@echo off

cd /d %~dp0

::clean old build
IF EXIST payload.dll ( del payload.dll )
::IF EXIST main.exe ( del main.exe )

::build dll
g++ payload.cpp -shared -o payload.dll

::build Main
g++ shellInjector.cpp -o injector.exe