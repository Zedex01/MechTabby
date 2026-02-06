#Pick Adapter Name

$AdapterName = "Ethernet"

$bytes = [byte[]]@(0x02)

#add 5 Random bytes
1..5 | ForEach-Object {
	$bytes += [byte](Get-Random -Minimum 0 -Maximum 256)
}

#Convert to MAC:
$NewMac = ($bytes | ForEach-Object { "{0:X2}" -f $_ }) -join ""

Write-Host "Setting MAC to $NewMac"
