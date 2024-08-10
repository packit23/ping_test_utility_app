# Define variables
$plinkPath = "C:\path\to\plink.exe"  # Update path to plink.exe
$hostname = "router_or_switch_hostname_or_ip"
$username = "your_username"
$password = "your_password"
$outputFile = "arp_table.txt"
$pythonScriptPath = "C:\path\to\ping_script.py"  # Update path to your Python script

# Run plink to connect to the Cisco device and fetch ARP table
$command = "show arp"
& $plinkPath -ssh -l $username -pw $password $hostname $command | Out-File $outputFile

# Check if the ARP table file was created successfully
if (Test-Path $outputFile) {
    # Run the Python script
    & python $pythonScriptPath
} else {
    Write-Output "Failed to create ARP table file."
}
