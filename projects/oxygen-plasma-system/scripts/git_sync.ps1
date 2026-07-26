param(
    [Parameter(Mandatory = $true)]
    [string]$CommitMessage,

    [Parameter(Mandatory = $true)]
    [string]$TagName
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if (-not (git remote get-url origin 2>$null)) {
    throw 'Remote origin is not configured.'
}

& "$PSScriptRoot\verify_release.ps1"

git switch main
git pull --rebase origin main
git add --all

if (git diff --cached --quiet) {
    throw 'No staged change exists; refusing to create an empty release commit.'
}

git commit -m $CommitMessage
git tag -a $TagName -m $TagName
git push origin main
git push origin $TagName

git fetch origin
$Local = git rev-parse HEAD
$Remote = git rev-parse origin/main
if ($Local -ne $Remote) {
    throw "Push verification failed. Local=$Local Remote=$Remote"
}

Write-Host "Synchronization verified: $Local" -ForegroundColor Green
