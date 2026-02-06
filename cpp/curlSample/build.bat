@echo off

cd /d %~dp0

::clean old build
IF EXIST main.exe ( del main.exe )

echo Building...

::build Main
g++ -w -DCURL_STATICLIB -m64 ^
main.cpp -o main.exe ^
-L .\dep\curl\lib ^
-I .\dep\curl\include ^
-lcurl ^
-lssl -lcrypto ^
-lnghttp2 -lnghttp3 -lngtcp2 -lngtcp2_crypto_libressl ^
-lssh2 ^
-lpsl ^
-lwldap32 ^
-lsecur32 ^
-liphlpapi ^
-lnormaliz ^
-lz -lbrotlidec -lbrotlicommon -lzstd ^
-lws2_32 -lcrypt32 -lbcrypt -lwinmm -luser32

::Check for errors
if %ERRORLEVEL% == 0 (echo Build Success!)
echo =======================