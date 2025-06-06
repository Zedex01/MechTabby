@echo off
setlocal enabledelayedexpansion

set PROJECT_NAME=pico_numpad
set BUILD_DIR=build

echo ================================
echo Starting build for %PROJECT_NAME%
echo ================================

REM Change to build directory
echo.
echo [1/3] Changing to build directory...
cd %BUILD_DIR% || (
    echo ERROR: Failed to change to build directory.
    exit /b 1
)

REM Run CMake
echo.
echo [2/3] Running CMake...
cmake .. -G "Ninja"
if errorlevel 1 (
    echo ERROR: CMake configuration failed.
    exit /b 1
)

REM Run Ninja build
echo.
echo [3/3] Building project with Ninja...
ninja
if errorlevel 1 (
    echo ERROR: Build failed.
    exit /b 1
)

REM Check if UF2 file exists
echo.
if exist "%PROJECT_NAME%.uf2" (
    echo ✅ Build succeeded! UF2 file generated: %PROJECT_NAME%.uf2
) else (
    echo ⚠️ Build finished, but UF2 file was not found!
    exit /b 1
)

echo.
echo Done.
exit /b 0
