@Echo off

cd /d %~dp0

IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST steg.spec ( del steg.spec )

pyinstaller --onefile --name steg main.py