@Echo off
:: Goto Current .Bat file
cd /d %~dp0/src/

::Delete old build
IF EXIST build ( rmdir build /s /q )
IF EXIST dist ( rmdir dist /s /q )
IF EXIST AutoZipper.spec ( del AutoZipper.spec )

::Check for arguments
IF "%1" == "" (
    echo Building without console...
    pyinstaller main.py --name AutoZipper --onefile --noconsole --add-data "../resources;resources"
    echo done!
    exit
)
IF "%1" == "-c" (
    echo Building with console...
    pyinstaller main.py --name AutoZipper --onefile --add-data "../resources;resources"
    echo done!
    exit
)
IF "%1" == "-clean" (
    echo Cleanup Done!
    exit
)


