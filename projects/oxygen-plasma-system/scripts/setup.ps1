$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw 'Python was not found in PATH.'
}

if (-not (Test-Path '.venv')) {
    python -m venv .venv
}

$Python = Join-Path $RepoRoot '.venv\Scripts\python.exe'
& $Python -m pip install --upgrade pip
& $Python -m pip install -e '.[dev]'
& $Python -m pytest
Write-Host 'Environment ready. GUI v1 tests passed.' -ForegroundColor Green
