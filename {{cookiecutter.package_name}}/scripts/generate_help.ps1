param (
    [string]$MakefilePath = "Makefile"
)

if (Test-Path $MakefilePath) {
    Get-Content $MakefilePath | Select-String '^#\shelp:' | ForEach-Object {
        $_.Line -replace '# help: ', '' -replace '# help:', ''
    }
} else {
    Write-Error "Makefile not found at path: $MakefilePath"
}
