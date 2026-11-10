# Temporary Updater CE terminal session for Windows.
# Served at https://innioasis.app/run_windows_lite.ps1
#   irm https://innioasis.app/run_windows_lite.ps1 | iex
# This is not part of the window build.

$ErrorActionPreference = "Stop"
$Site = "https://innioasis.app"
# The archive is an extra file on 2.5.3, beside the Windows and Mac packages.
# A newer tag would offer those installed apps an update they should not get.
$Apis = @(
    "https://api.github.com/repos/y1-community/updater-ce-neo/releases/tags/2.5.3",
    "https://api.github.com/repos/y1-community/updater-ce-neo/releases/latest"
)
$Dest = Join-Path $env:LOCALAPPDATA "innioasis-updater\lite"
$Archive = Join-Path $env:TEMP "UpdaterCE-Lite.tar.gz"

Write-Host "Updater CE — temporary terminal session"
Write-Host "1/4  Looking for Python"

$Python = $null
foreach ($name in @("python", "python3", "py")) {
    $cmd = Get-Command $name -ErrorAction SilentlyContinue
    if ($cmd) { $Python = $cmd.Source; break }
}
if (-not $Python) {
    Write-Host "Python 3.8 or newer is required. Install it from https://www.python.org/downloads/ and run this again."
    exit 3
}

Write-Host "2/4  Fetching the release index"
$Url = "$Site/UpdaterCE-Lite.tar.gz"
foreach ($Api in $Apis) {
    try {
        $release = Invoke-RestMethod -Uri $Api -Headers @{ "User-Agent" = "UpdaterCE-lite" }
        $asset = $release.assets | Where-Object { $_.name -eq "UpdaterCE-Lite.tar.gz" } | Select-Object -First 1
        if ($asset) { $Url = $asset.browser_download_url; break }
    } catch {
        continue
    }
}

Write-Host "3/4  Downloading"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
Invoke-WebRequest -Uri $Url -OutFile $Archive -UseBasicParsing
tar -xzf $Archive -C $Dest

Write-Host "4/4  Opening the terminal session"
& $Python (Join-Path $Dest "lite.py") tui
exit $LASTEXITCODE
