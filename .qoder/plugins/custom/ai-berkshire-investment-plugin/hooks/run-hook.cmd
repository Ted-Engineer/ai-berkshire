: << 'CMDBLOCK'
@echo off
REM Cross-platform polyglot wrapper for hook scripts.
REM On Windows: cmd.exe runs the batch portion, which finds and calls bash.
REM On Unix: the shell interprets this as a script (: is a no-op in bash).
REM
REM Usage: run-hook.cmd <script-name> [args...]

if "%~1"=="" (
    echo run-hook.cmd: missing script name >&2
    exit /b 1
)

set "HOOK_DIR=%~dp0"

REM Try Git for Windows bash in standard locations
for %%B in (
    "%PROGRAMFILES%\Git\bin\bash.exe"
    "%PROGRAMFILES(X86)%\Git\bin\bash.exe"
    "%LOCALAPPDATA%\Programs\Git\bin\bash.exe"
) do (
    if exist %%B (
        %%B "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
        exit /b %ERRORLEVEL%
    )
)

echo run-hook.cmd: bash not found >&2
exit /b 1
CMDBLOCK

# Unix portion (bash executes this; cmd.exe never reaches here)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_NAME="${1:?Usage: run-hook.cmd <script-name> [args...]}"
shift
exec bash "${SCRIPT_DIR}/${SCRIPT_NAME}" "$@"
