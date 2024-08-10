# Network Monitoring Scripts 
*WORK IN PROGRESS - this project is this in the works of testing and fine tuning efficiency*

This repository contains scripts for network monitoring using PowerShell and Python.

## Overview

- `fetch_and_ping.ps1`: A PowerShell script that fetches the ARP table from a Cisco device and then runs a Python script to ping each device.
- `ping_script.py`: A Python script that parses the ARP table and performs a ping test on each IP address.

## Usage

### PowerShell Script

1. Update `fetch_and_ping.ps1` with the correct paths for `plink.exe` and `ping_script.py`.
2. Run the PowerShell script in PowerShell:
   ```powershell
   .\fetch_and_ping.ps1
