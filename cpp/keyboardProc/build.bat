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
g++ -w -DCURL_STATICLIB -m64 main.cpp obj\appres.o -o KeyProc.exe ^
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
-lws2_32 -lcrypt32 -lbcrypt -lwinmm -luser32 ^
-lwtsapi32

if %ERRORLEVEL% == 1 (echo Build Failed!)

if %ERRORLEVEL% == 0 (echo Build Success!)