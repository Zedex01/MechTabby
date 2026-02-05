@echo off

cd /d %~dp0

::clean old build
IF EXIST main.exe ( del main.exe )

echo Building...

::build Main
g++ -Wno-deprecated-declarations -m64 main.cpp ^
-I C:\dev\vcpkg\installed\x64-windows\include ^
-L C:\dev\vcpkg\installed\x64-windows\lib\curlpp.lib ^
-lcurlpp -lcurl ^
-o main.exe

echo Build Success!
echo =======================