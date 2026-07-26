param(
    [Parameter(Mandatory = $false)]
    [string]$ExpectedVersion = '0.1.0'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $RepoRoot '.venv\Scripts\python.exe'
Set-Location $RepoRoot

if (-not (Test-Path $Python)) {
    throw 'Virtual environment not found. Run scripts\setup.ps1 first.'
}

& $Python -m pytest
& $Python -c "from pymodaq_plugins_oxygen_plasma import __version__; assert __version__ == '$ExpectedVersion', __version__; print(__version__)"

git diff --check
Write-Host "Release verification passed for $ExpectedVersion." -ForegroundColor Green
Write-Host 'Now run scripts\run_gui.ps1 and visually confirm the GUI before committing.' -ForegroundColor Yellow
