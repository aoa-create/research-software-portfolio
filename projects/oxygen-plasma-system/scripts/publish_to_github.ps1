param(
    [Parameter(Mandatory = $false)]
    [string]$Repository = 'aoa-create/oxygen-plasma-system',

    [Parameter(Mandatory = $false)]
    [ValidateSet('private', 'public')]
    [string]$Visibility = 'private'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git was not found in PATH.'
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw 'GitHub CLI (gh) was not found. Install it with: winget install --id GitHub.cli'
}

$Login = gh api user --jq .login
$ExpectedOwner = ($Repository -split '/')[0]
if ($Login -ne $ExpectedOwner) {
    throw "Authenticated GitHub account '$Login' does not match repository owner '$ExpectedOwner'."
}

$TargetUrl = "https://github.com/$Repository.git"
$Existing = gh repo view $Repository --json nameWithOwner 2>$null
$OriginUrl = git remote get-url origin 2>$null

if (-not $Existing) {
    if ($OriginUrl) {
        git remote remove origin
    }
    if ($Visibility -eq 'private') {
        gh repo create $Repository --private --source . --remote origin --push
    }
    else {
        gh repo create $Repository --public --source . --remote origin --push
    }
}
else {
    if ($OriginUrl) {
        git remote set-url origin $TargetUrl
    }
    else {
        git remote add origin $TargetUrl
    }
    git pull --rebase origin main
    git push -u origin main
}

git push origin --tags
git fetch origin
$Local = git rev-parse HEAD
$Remote = git rev-parse origin/main
if ($Local -ne $Remote) {
    throw "GitHub verification failed. Local=$Local Remote=$Remote"
}

Write-Host "GitHub publication verified: https://github.com/$Repository" -ForegroundColor Green
Write-Host "Commit: $Local" -ForegroundColor Green
