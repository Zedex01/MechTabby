@Echo off
:: Goto Current .Bat file
cd /d %~dp0

::Delete old build
IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST WorkTracker.spec ( del WorkTracker.spec )

::Check for arguments
IF "%1" == "" (
    echo Building without console...
    pyinstaller --name WorkTracker --onedir --noconsole --add-data "data;data" --paths src main.py
    
    REM Copy over Config and DB files
    xcopy "data" "dist\WorkTracker\data" /E /I /Y
    exit
)
IF "%1" == "-c" (
    echo Building with console...
    pyinstaller --name WorkTracker --onedir --add-data "data;data" --paths src main.py
    
    REM Copy over Config and DB files
    xcopy "data" "dist\WorkTracker\data" /E /I /Y
    exit
)
IF "%1" == "-clean" (
    echo Cleanup Done!
    exit
)


