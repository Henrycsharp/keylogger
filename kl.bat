@echo off
:: Check if English (US) keyboard is installed

:: Get the current keyboard layout
for /f "tokens=3 delims= " %%a in ('reg query "HKCU\Keyboard Layout\Preload" /v 1 2^>nul') do set "currentLayout=%%a"

:: Check if the layout is English (US)
if "%currentLayout%"=="00000409" (
    echo English (US) keyboard layout is installed.
) else (
    echo English (US) keyboard layout is not installed.
)
pause
