$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $RepoRoot '.venv\Scripts\python.exe'

if (-not (Test-Path $Python)) {
    throw 'Virtual environment not found. Run scripts\setup.ps1 first.'
}

Set-Location $RepoRoot
& $Python -m pymodaq_plugins_oxygen_plasma.app.main
