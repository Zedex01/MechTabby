@Echo off

cd /d %~dp0

IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST b64.spec ( del b64.spec )

pyinstaller --onefile --name b64 main.py