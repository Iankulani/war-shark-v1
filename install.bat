@echo off
REM ==============================================================================
REM WAR-SHARK-v1 - Windows Installation Script
REM Author: Ian Carter Kulani
REM Version: 1.0.0
REM ==============================================================================

setlocal EnableDelayedExpansion

REM Configuration
set WARSHARK_VERSION=1.0.0
set INSTALL_DIR=%ProgramFiles%\WAR-SHARK
set CONFIG_DIR=%USERPROFILE%\.war_shark
set VENV_DIR=%INSTALL_DIR%\venv
set LOG_FILE=%INSTALL_DIR%\install.log

REM Colors (Windows 10+)
set RED=[91m
set GREEN=[92m
set YELLOW=[93m
set BLUE=[94m
set CYAN=[96m
set WHITE=[97m
set NC=[0m

REM ==============================================================================
REM UTILITY FUNCTIONS
REM ==============================================================================

:print_banner
echo.
echo %CYAN%╔══════════════════════════════════════════════════════════════════════════════╗%NC%
echo %CYAN%║                                                                              ║%NC%
echo %CYAN%║   🦈 WAR-SHARK-v1 - Ultimate Cybersecurity Command ^& Control Platform       ║%NC%
echo %CYAN%║                                                                              ║%NC%
echo %CYAN%║   Author: Ian Carter Kulani                                                  ║%NC%
echo %CYAN%║   Version: 1.0.0                                                             ║%NC%
echo %CYAN%║                                                                              ║%NC%
echo %CYAN%╚══════════════════════════════════════════════════════════════════════════════╝%NC%
echo.
goto :eof

:log
set LEVEL=%~1
set MESSAGE=%~2
set TIMESTAMP=%date% %time%

if "%LEVEL%"=="INFO" set COLOR=%BLUE%
if "%LEVEL%"=="SUCCESS" set COLOR=%GREEN%
if "%LEVEL%"=="WARNING" set COLOR=%YELLOW%
if "%LEVEL%"=="ERROR" set COLOR=%RED%

echo %COLOR%[%TIMESTAMP%] [%LEVEL%] %MESSAGE%%NC%
echo [%TIMESTAMP%] [%LEVEL%] %MESSAGE% >> "%LOG_FILE%" 2>nul
goto :eof

:check_admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    call :log ERROR "This script must be run as Administrator"
    echo Please right-click and select "Run as Administrator"
    pause
    exit /b 1
)
goto :eof

:check_python
call :log INFO "Checking Python installation..."

python --version >nul 2>&1
if %errorLevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorLevel% neq 0 (
        call :log ERROR "Python not found. Please install Python 3.8+"
        echo Download from: https://www.python.org/downloads/
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=python3
    )
) else (
    set PYTHON_CMD=python
)

for /f "tokens=2" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VERSION=%%i
call :log SUCCESS "Python %PYTHON_VERSION% found"
goto :eof

:check_pip
call :log INFO "Checking pip installation..."

%PYTHON_CMD% -m pip --version >nul 2>&1
if %errorLevel% neq 0 (
    call :log WARNING "pip not found. Installing..."
    %PYTHON_CMD% -m ensurepip --upgrade
    if %errorLevel% neq 0 (
        call :log ERROR "Failed to install pip"
        pause
        exit /b 1
    )
)
call :log SUCCESS "pip available"
goto :eof

:install_dependencies
call :log INFO "Installing Python dependencies..."

%PYTHON_CMD% -m pip install --upgrade pip setuptools wheel

if exist "%INSTALL_DIR%\requirements.txt" (
    %PYTHON_CMD% -m pip install -r "%INSTALL_DIR%\requirements.txt"
) else (
    call :log WARNING "requirements.txt not found"
)

call :log SUCCESS "Python dependencies installed"
goto :eof

:create_directories
call :log INFO "Creating directories..."

mkdir "%INSTALL_DIR%" 2>nul
mkdir "%CONFIG_DIR%" 2>nul
mkdir "%CONFIG_DIR%\payloads" 2>nul
mkdir "%CONFIG_DIR%\workspaces" 2>nul
mkdir "%CONFIG_DIR%\scans" 2>nul
mkdir "%CONFIG_DIR%\phishing_pages" 2>nul
mkdir "%CONFIG_DIR%\phishing_templates" 2>nul
mkdir "%CONFIG_DIR%\captured_credentials" 2>nul
mkdir "%CONFIG_DIR%\ssh_keys" 2>nul
mkdir "%CONFIG_DIR%\traffic_logs" 2>nul
mkdir "%CONFIG_DIR%\nikto_results" 2>nul
mkdir "%CONFIG_DIR%\web_templates" 2>nul
mkdir "%CONFIG_DIR%\sessions" 2>nul
mkdir "%CONFIG_DIR%\spear_phishing" 2>nul
mkdir "%CONFIG_DIR%\email_templates" 2>nul
mkdir "%CONFIG_DIR%\dos_logs" 2>nul
mkdir "%CONFIG_DIR%\agents" 2>nul
mkdir "%CONFIG_DIR%\c2_logs" 2>nul
mkdir "%CONFIG_DIR%\modules" 2>nul
mkdir "%CONFIG_DIR%\network_monitor" 2>nul
mkdir "%CONFIG_DIR%\keylog_exfil" 2>nul
mkdir "%CONFIG_DIR%\deployments" 2>nul
mkdir "%CONFIG_DIR%\domain_hosting" 2>nul
mkdir "%CONFIG_DIR%\docker_scans" 2>nul
mkdir "%CONFIG_DIR%\cracking" 2>nul
mkdir "%CONFIG_DIR%\wordlists" 2>nul
mkdir "%CONFIG_DIR%\reverse_engineering" 2>nul
mkdir "%CONFIG_DIR%\metasploit" 2>nul
mkdir "%CONFIG_DIR%\post_exploitation" 2>nul
mkdir "%CONFIG_DIR%\exploit_db" 2>nul

call :log SUCCESS "Directories created"
goto :eof

:setup_virtualenv
call :log INFO "Setting up virtual environment..."

if not exist "%VENV_DIR%" (
    %PYTHON_CMD% -m venv "%VENV_DIR%"
)

call "%VENV_DIR%\Scripts\activate.bat"

python -m pip install --upgrade pip setuptools wheel

if exist "%INSTALL_DIR%\requirements.txt" (
    pip install -r "%INSTALL_DIR%\requirements.txt"
)

call :log SUCCESS "Virtual environment ready"
goto :eof

:create_config
call :log INFO "Creating default configuration..."

(
echo {
echo     "version": "1.0.0",
echo     "auto_start": false,
echo     "auto_block_enabled": false,
echo     "auto_block_threshold": 5,
echo     "scan_timeout": 30,
echo     "report_format": "both",
echo     "generate_graphics": true,
echo     "keylogger": {
echo         "enabled": false,
echo         "hotkey": "f10",
echo         "log_file": "%%USERPROFILE%%\\.war_shark\\keylog.txt",
echo         "c2_server": "",
echo         "upload_interval": 30
echo     },
echo     "web": {
echo         "enabled": false,
echo         "port": 5000,
echo         "host": "0.0.0.0"
echo     },
echo     "monitoring": {
echo         "enabled": true,
echo         "port_scan_threshold": 10,
echo         "syn_flood_threshold": 100,
echo         "http_flood_threshold": 200
echo     },
echo     "traffic_generation": {
echo         "enabled": true,
echo         "max_duration": 300,
echo         "max_packet_rate": 1000,
echo         "allow_floods": false
echo     },
echo     "social_engineering": {
echo         "enabled": true,
echo         "default_port": 8080,
echo         "capture_credentials": true
echo     }
echo }
) > "%CONFIG_DIR%\config.json"

call :log SUCCESS "Default configuration created"
goto :eof

:create_launcher
call :log INFO "Creating launcher script..."

(
echo @echo off
echo call "%VENV_DIR%\Scripts\activate.bat"
echo cd /d "%INSTALL_DIR%"
echo python war_shark.py %%*
) > "%INSTALL_DIR%\war-shark.bat"

REM Add to PATH
setx PATH "%PATH%;%INSTALL_DIR%" /M >nul 2>&1

call :log SUCCESS "Launcher created"
goto :eof

:post_install
echo.
echo %GREEN%╔══════════════════════════════════════════════════════════════════════════════╗%NC%
echo %GREEN%║                                                                              ║%NC%
echo %GREEN%║   ✅ WAR-SHARK Installation Complete!                                        ║%NC%
echo %GREEN%║                                                                              ║%NC%
echo %GREEN%╚══════════════════════════════════════════════════════════════════════════════╝%NC%
echo.
echo %CYAN%📁 Installation Directory:%NC% %INSTALL_DIR%
echo %CYAN%📁 Configuration Directory:%NC% %CONFIG_DIR%
echo %CYAN%📁 Log File:%NC% %LOG_FILE%
echo.
echo %YELLOW%🚀 To run WAR-SHARK:%NC%
echo    %WHITE%war-shark.bat%NC%
echo.
echo %YELLOW%🔧 To activate virtual environment:%NC%
echo    %WHITE%call %VENV_DIR%\Scripts\activate.bat%NC%
echo.
echo %RED%⚠️  WARNING: For authorized security testing only!%NC%
echo.
goto :eof

REM ==============================================================================
REM MAIN INSTALLATION
REM ==============================================================================

:main
REM Initialize log
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%" 2>nul
echo. > "%LOG_FILE%" 2>nul

call :print_banner

REM Check admin
call :check_admin

REM Check Python
call :check_python
call :check_pip

REM Create directories
call :create_directories

REM Setup virtual environment
call :setup_virtualenv

REM Install dependencies
call :install_dependencies

REM Create configuration
call :create_config

REM Create launcher
call :create_launcher

REM Post-installation
call :post_install

pause
exit /b 0
