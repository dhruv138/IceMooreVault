@echo off
REM Double-click this file in File Explorer to update the vault.
cd /d "%~dp0.."
where py >NUL 2>NUL
if %errorlevel%==0 (
  py -3 scripts\update_all.py
) else (
  python scripts\update_all.py
)
echo.
pause
