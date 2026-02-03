@Echo off

cd /d %~dp0

IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST gcp.spec ( del gcp.spec )

pyinstaller --onefile --name gcp main.py