param (
    [string]$ReleaseArchivePattern = "./package_name-*-py3-none-any.whl"
)

if (-not $ReleaseArchivePattern) {
    Write-Host "usage: .\test-dist.ps1 package_name-YY.MM.MICRO-py3-none-any.whl"
    exit 1
}

# Set ErrorActionPreference to Stop to treat all errors as terminating
$ErrorActionPreference = "Stop"

try {
    $ReleaseArchive = Get-ChildItem -Path $ReleaseArchivePattern | Select-Object -First 1

    if (-not $ReleaseArchive) {
        Write-Host "No matching release archive found for pattern: $ReleaseArchivePattern"
        exit 1
    }

    Write-Host "Release archive: $ReleaseArchive"

    Write-Host "Removing any old artefacts"
    if (Test-Path -Path test_venv) {
        Remove-Item -Recurse -Force test_venv
    }

    Write-Host "Creating test virtual environment"
    python -m venv test_venv

    Write-Host "Entering test virtual environment"
    & .\test_venv\Scripts\Activate.ps1

    Write-Host "Upgrading pip"
    pip install --upgrade pip

    Write-Host "Installing $ReleaseArchive"
    pip install $ReleaseArchive.FullName

    Write-Host "Running tests"
    python -m unittest discover -s ..

    Write-Host "Exiting test virtual environment"
    deactivate

    Write-Host "Removing test virtual environment"
    Remove-Item -Recurse -Force test_venv
} catch {
    Write-Host "An error occurred: $_"
    exit 1
}
