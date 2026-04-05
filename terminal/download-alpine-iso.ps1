$ErrorActionPreference = "Stop"

$isoName = "alpine-virt-3.20.9-x86.iso"
$isoUrl = "https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86/$isoName"
$destPath = Join-Path $PSScriptRoot $isoName

Write-Host "Downloading Alpine ISO..."
Write-Host "Source: $isoUrl"
Write-Host "Target: $destPath"

Invoke-WebRequest -Uri $isoUrl -OutFile $destPath

Write-Host "Download complete."
Write-Host "Now run: python -m http.server 8080"
