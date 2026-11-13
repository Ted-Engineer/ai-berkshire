@echo off
setlocal
set "ROOT=%~dp0.."
set "DEST=%USERPROFILE%\.qoder\skills"

where python3 >nul 2>&1
if %errorlevel%==0 (set "PY=python3") else (set "PY=python")
%PY% "%ROOT%\scripts\sync-codex-skills.py"

if not exist "%DEST%" mkdir "%DEST%"
for /d %%D in ("%ROOT%\codex-skills\*") do (
  if exist "%DEST%\%%~nxD" rmdir /s /q "%DEST%\%%~nxD"
  xcopy /e /i /y "%%D" "%DEST%\%%~nxD" >nul
)
echo Installed Qoder skills to %DEST%
echo Open a new Qoder chat session (or restart Qoder) to pick up the skills.
