# ==============================================================================
# WAR-SHARK-v1 - Windows PowerShell Installation Script
# Author: Ian Carter Kulani
# Version: 1.0.0
# ==============================================================================

#Requires -RunAsAdministrator

# Configuration
$WARSHARK_VERSION = "1.0.0"
$INSTALL_DIR = "$env:ProgramFiles\WAR-SHARK"
$CONFIG_DIR = "$env:USERPROFILE\.war_shark"
$VENV_DIR = "$INSTALL_DIR\venv"
$LOG_FILE = "$INSTALL_DIR\install.log"

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

function Write-Banner {
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                                                                              ║" -ForegroundColor Cyan
    Write-Host "║   🦈 WAR-SHARK-v1 - Ultimate Cybersecurity Command & Control Platform       ║" -ForegroundColor Cyan
    Write-Host "║                                                                              ║" -ForegroundColor Cyan
    Write-Host "║   Author: Ian Carter Kulani                                                  ║" -ForegroundColor Cyan
    Write-Host "║   Version: 1.0.0                                                             ║" -ForegroundColor Cyan
    Write-Host "║                                                                              ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Log {
    param(
        [string]$Level,
        [string]$Message
    )
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    
    $color = switch ($Level) {
        "INFO" { "Blue" }
        "SUCCESS" { "Green" }
        "WARNING" { "Yellow" }
        "ERROR" { "Red" }
        default { "White" }
    }
    
    Write-Host "[$timestamp] [$Level] $Message" -ForegroundColor $color
    
    # Also write to log file
    if (Test-Path (Split-Path $LOG_FILE)) {
        "[$timestamp] [$Level] $Message" | Out-File -FilePath $LOG_FILE -Append -Encoding UTF8
    }
}

function Test-Prerequisites {
    Write-Log "INFO" "Checking prerequisites..."
    
    # Check Python
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        $python = Get-Command python3 -ErrorAction SilentlyContinue
    }
    
    if (-not $python) {
        Write-Log "ERROR" "Python not found. Please install Python 3.8+"
        Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
        exit 1
    }
    
    $pythonVersion = & $python.Source --version 2>&1
    Write-Log "SUCCESS" "Found $pythonVersion"
    
    # Check pip
    $pip = & $python.Source -m pip --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Log "WARNING" "pip not found. Installing..."
        & $python.Source -m ensurepip --upgrade
    }
    Write-Log "SUCCESS" "pip is available"
    
    # Check git
    $git = Get-Command git -ErrorAction SilentlyContinue
    if (-not $git) {
        Write-Log "WARNING" "Git not found. Some features may not work."
    } else {
        Write-Log "SUCCESS" "Git is available"
    }
}

function Install-SystemDependencies {
    Write-Log "INFO" "Installing system dependencies..."
    
    # Check if winget is available
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    
    if ($winget) {
        # Install common tools via winget
        $tools = @(
            "Python.Python.3.11",
            "Git.Git",
            "Insecure.Nmap",
            "curl.curl"
        )
        
        foreach ($tool in $tools) {
            Write-Log "INFO" "Installing $tool..."
            winget install --id $tool --accept-source-agreements --accept-package-agreements --silent 2>$null
        }
    } else {
        Write-Log "WARNING" "winget not available. Please install tools manually."
    }
    
    Write-Log "SUCCESS" "System dependencies processed"
}

function New-Directories {
    Write-Log "INFO" "Creating directories..."
    
    $directories = @(
        $INSTALL_DIR,
        $CONFIG_DIR,
        "$CONFIG_DIR\payloads",
        "$CONFIG_DIR\workspaces",
        "$CONFIG_DIR\scans",
        "$CONFIG_DIR\phishing_pages",
        "$CONFIG_DIR\phishing_templates",
        "$CONFIG_DIR\captured_credentials",
        "$CONFIG_DIR\ssh_keys",
        "$CONFIG_DIR\traffic_logs",
        "$CONFIG_DIR\nikto_results",
        "$CONFIG_DIR\web_templates",
        "$CONFIG_DIR\sessions",
        "$CONFIG_DIR\spear_phishing",
        "$CONFIG_DIR\email_templates",
        "$CONFIG_DIR\dos_logs",
        "$CONFIG_DIR\agents",
        "$CONFIG_DIR\c2_logs",
        "$CONFIG_DIR\modules",
        "$CONFIG_DIR\network_monitor",
        "$CONFIG_DIR\keylog_exfil",
        "$CONFIG_DIR\deployments",
        "$CONFIG_DIR\domain_hosting",
        "$CONFIG_DIR\docker_scans",
        "$CONFIG_DIR\cracking",
        "$CONFIG_DIR\wordlists",
        "$CONFIG_DIR\reverse_engineering",
        "$CONFIG_DIR\metasploit",
        "$CONFIG_DIR\post_exploitation",
        "$CONFIG_DIR\exploit_db"
    )
    
    foreach ($dir in $directories) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    
    Write-Log "SUCCESS" "Directories created"
}

function New-VirtualEnvironment {
    Write-Log "INFO" "Setting up virtual environment..."
    
    if (-not (Test-Path $VENV_DIR)) {
        python -m venv $VENV_DIR
    }
    
    # Activate virtual environment
    & "$VENV_DIR\Scripts\Activate.ps1"
    
    # Upgrade pip
    python -m pip install --upgrade pip setuptools wheel
    
    Write-Log "SUCCESS" "Virtual environment ready"
}

function Install-PythonDependencies {
    Write-Log "INFO" "Installing Python dependencies..."
    
    # Activate virtual environment
    & "$VENV_DIR\Scripts\Activate.ps1"
    
    # Install from requirements
    $requirementsFile = "$INSTALL_DIR\requirements.txt"
    if (Test-Path $requirementsFile) {
        pip install -r $requirementsFile
    } else {
        Write-Log "WARNING" "requirements.txt not found"
    }
    
    Write-Log "SUCCESS" "Python dependencies installed"
}

function New-Configuration {
    Write-Log "INFO" "Creating default configuration..."
    
    $config = @{
        version = "1.0.0"
        auto_start = $false
        auto_block_enabled = $false
        auto_block_threshold = 5
        scan_timeout = 30
        report_format = "both"
        generate_graphics = $true
        keylogger = @{
            enabled = $false
            hotkey = "f10"
            log_file = "$CONFIG_DIR\keylog.txt"
            c2_server = ""
            upload_interval = 30
        }
        web = @{
            enabled = $false
            port = 5000
            host = "0.0.0.0"
        }
        monitoring = @{
            enabled = $true
            port_scan_threshold = 10
            syn_flood_threshold = 100
            http_flood_threshold = 200
        }
        traffic_generation = @{
            enabled = $true
            max_duration = 300
            max_packet_rate = 1000
            allow_floods = $false
        }
        social_engineering = @{
            enabled = $true
            default_port = 8080
            capture_credentials = $true
        }
    }
    
    $config | ConvertTo-Json -Depth 10 | Out-File -FilePath "$CONFIG_DIR\config.json" -Encoding UTF8
    
    Write-Log "SUCCESS" "Default configuration created"
}

function New-Launcher {
    Write-Log "INFO" "Creating launcher script..."
    
    $launcherContent = @"
@echo off
call "$VENV_DIR\Scripts\activate.bat"
cd /d "$INSTALL_DIR"
python war_shark.py %*
"@
    
    $launcherContent | Out-File -FilePath "$INSTALL_DIR\war-shark.bat" -Encoding ASCII
    
    # Add to PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    if ($currentPath -notlike "*$INSTALL_DIR*") {
        [Environment]::SetEnvironmentVariable("Path", "$currentPath;$INSTALL_DIR", "Machine")
    }
    
    Write-Log "SUCCESS" "Launcher created"
}

function New-Shortcut {
    Write-Log "INFO" "Creating desktop shortcut..."
    
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\WAR-SHARK.lnk")
    $Shortcut.TargetPath = "$INSTALL_DIR\war-shark.bat"
    $Shortcut.WorkingDirectory = $INSTALL_DIR
    $Shortcut.Description = "WAR-SHARK Cybersecurity Platform"
    $Shortcut.Save()
    
    Write-Log "SUCCESS" "Desktop shortcut created"
}

function Show-PostInstall {
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║                                                                              ║" -ForegroundColor Green
    Write-Host "║   ✅ WAR-SHARK Installation Complete!                                        ║" -ForegroundColor Green
    Write-Host "║                                                                              ║" -ForegroundColor Green
    Write-Host "╚══════════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
    Write-Host ""
    Write-Host "📁 Installation Directory: $INSTALL_DIR" -ForegroundColor Cyan
    Write-Host "📁 Configuration Directory: $CONFIG_DIR" -ForegroundColor Cyan
    Write-Host "📁 Log File: $LOG_FILE" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🚀 To run WAR-SHARK:" -ForegroundColor Yellow
    Write-Host "   war-shark.bat" -ForegroundColor White
    Write-Host ""
    Write-Host "🔧 To activate virtual environment:" -ForegroundColor Yellow
    Write-Host "   & '$VENV_DIR\Scripts\Activate.ps1'" -ForegroundColor White
    Write-Host ""
    Write-Host "⚠️  WARNING: For authorized security testing only!" -ForegroundColor Red
    Write-Host ""
}

# ==============================================================================
# MAIN INSTALLATION
# ==============================================================================

function Main {
    # Initialize log
    if (-not (Test-Path $INSTALL_DIR)) {
        New-Item -ItemType Directory -Path $INSTALL_DIR -Force | Out-Null
    }
    "" | Out-File -FilePath $LOG_FILE -Encoding UTF8
    
    Write-Banner
    
    # Check prerequisites
    Test-Prerequisites
    
    # Install system dependencies
    Install-SystemDependencies
    
    # Create directories
    New-Directories
    
    # Setup virtual environment
    New-VirtualEnvironment
    
    # Install Python dependencies
    Install-PythonDependencies
    
    # Create configuration
    New-Configuration
    
    # Create launcher
    New-Launcher
    
    # Create shortcut
    New-Shortcut
    
    # Post-installation
    Show-PostInstall
}

# Run main
Main
