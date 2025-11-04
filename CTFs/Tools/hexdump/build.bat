@Echo off

cd /d %~dp0

IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST hexdump.spec ( del hexdump.spec )

pyinstaller --onefile --name hexdump main.py