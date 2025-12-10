$subnet = "192.168.1"

$used = @()

1..254 | ForEach-Object {
    $ip = "$subnet.$_"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet -TimeoutSeconds 1) {
        $used += $ip
    }
}

Write-Host "Used IPs:"
$used

Write-Host "'nFree IPs:"
1..254 | ForEach-Object {
    $ip = "$subnet.$_"
    if ($used -notcontains $ip) {
        Write-Host $ip
    }
}