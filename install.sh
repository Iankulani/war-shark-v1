#!/bin/bash
# ==============================================================================
# WAR-SHARK-v1 - Linux/macOS Installation Script
# Author: Ian Carter Kulani
# Version: 1.0.0
# ==============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Configuration
WARSHARK_VERSION="1.0.0"
INSTALL_DIR="/opt/war-shark"
VENV_DIR="${INSTALL_DIR}/venv"
CONFIG_DIR="${HOME}/.war_shark"
LOG_FILE="${INSTALL_DIR}/install.log"

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

print_banner() {
    echo -e "${CYAN}"
    cat << "EOF"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🦈 WAR-SHARK-v1 - Ultimate Cybersecurity Command & Control Platform       ║
║                                                                              ║
║   Author: Ian Carter Kulani                                                  ║
║   Version: 1.0.0                                                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case $level in
        "INFO") color="${BLUE}" ;;
        "SUCCESS") color="${GREEN}" ;;
        "WARNING") color="${YELLOW}" ;;
        "ERROR") color="${RED}" ;;
        *) color="${NC}" ;;
    esac
    
    echo -e "${color}[${timestamp}] [${level}] ${message}${NC}"
    echo "[${timestamp}] [${level}] ${message}" >> "${LOG_FILE}" 2>/dev/null || true
}

check_root() {
    if [[ $EUID -ne 0 ]]; then
        log "ERROR" "This script must be run as root (use sudo)"
        exit 1
    fi
}

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
            PKG_MANAGER="apt-get"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
            PKG_MANAGER="yum"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
            PKG_MANAGER="pacman"
        elif [ -f /etc/alpine-release ]; then
            OS="alpine"
            PKG_MANAGER="apk"
        else
            OS="linux"
            PKG_MANAGER="apt-get"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG_MANAGER="brew"
    else
        OS="unknown"
        PKG_MANAGER="unknown"
    fi
    
    log "INFO" "Detected OS: ${OS}"
}

check_python() {
    log "INFO" "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
        
        if [[ $PYTHON_MAJOR -ge 3 ]] && [[ $PYTHON_MINOR -ge 8 ]]; then
            log "SUCCESS" "Python ${PYTHON_VERSION} found"
            PYTHON_CMD="python3"
        else
            log "ERROR" "Python 3.8+ required. Found: ${PYTHON_VERSION}"
            exit 1
        fi
    else
        log "ERROR" "Python 3 not found. Please install Python 3.8+"
        exit 1
    fi
}

check_pip() {
    log "INFO" "Checking pip installation..."
    
    if command -v pip3 &> /dev/null; then
        log "SUCCESS" "pip3 found"
        PIP_CMD="pip3"
    elif python3 -m pip --version &> /dev/null; then
        log "SUCCESS" "pip module found"
        PIP_CMD="python3 -m pip"
    else
        log "WARNING" "pip not found. Installing..."
        install_pip
    fi
}

install_pip() {
    log "INFO" "Installing pip..."
    
    if command -v curl &> /dev/null; then
        curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
        python3 /tmp/get-pip.py
        rm /tmp/get-pip.py
    elif command -v wget &> /dev/null; then
        wget -q https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
        python3 /tmp/get-pip.py
        rm /tmp/get-pip.py
    else
        log "ERROR" "Cannot download pip. Please install curl or wget"
        exit 1
    fi
    
    PIP_CMD="python3 -m pip"
    log "SUCCESS" "pip installed"
}

# ==============================================================================
# SYSTEM DEPENDENCIES
# ==============================================================================

install_system_deps() {
    log "INFO" "Installing system dependencies..."
    
    case $OS in
        "debian")
            apt-get update -qq
            apt-get install -y -qq \
                build-essential \
                libssl-dev \
                libffi-dev \
                python3-dev \
                python3-pip \
                python3-venv \
                git \
                curl \
                wget \
                nmap \
                netcat-openbsd \
                dnsutils \
                traceroute \
                whois \
                tcpdump \
                libpcap-dev \
                libxml2-dev \
                libxslt1-dev \
                zlib1g-dev \
                libjpeg-dev \
                libpng-dev \
                libfreetype6-dev \
                libpq-dev \
                default-libmysqlclient-dev \
                pkg-config \
                cmake \
                libgl1-mesa-glx \
                libglib2.0-0 \
                libsm6 \
                libxext6 \
                libxrender-dev \
                chromium-browser \
                chromium-chromedriver \
                2>/dev/null || true
            ;;
        "redhat")
            yum install -y \
                gcc \
                gcc-c++ \
                make \
                openssl-devel \
                libffi-devel \
                python3-devel \
                python3-pip \
                git \
                curl \
                wget \
                nmap \
                nc \
                bind-utils \
                traceroute \
                whois \
                tcpdump \
                libpcap-devel \
                libxml2-devel \
                libxslt-devel \
                zlib-devel \
                libjpeg-devel \
                libpng-devel \
                freetype-devel \
                2>/dev/null || true
            ;;
        "arch")
            pacman -Sy --noconfirm \
                base-devel \
                openssl \
                libffi \
                python \
                python-pip \
                git \
                curl \
                wget \
                nmap \
                gnu-netcat \
                bind-tools \
                traceroute \
                whois \
                tcpdump \
                libpcap \
                libxml2 \
                libxslt \
                zlib \
                libjpeg-turbo \
                libpng \
                freetype2 \
                2>/dev/null || true
            ;;
        "macos")
            if ! command -v brew &> /dev/null; then
                log "INFO" "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install \
                openssl \
                libffi \
                python3 \
                git \
                curl \
                wget \
                nmap \
                netcat \
                bind \
                traceroute \
                whois \
                tcpdump \
                libpcap \
                2>/dev/null || true
            ;;
        *)
            log "WARNING" "Unknown OS. Skipping system dependencies."
            ;;
    esac
    
    log "SUCCESS" "System dependencies installed"
}

install_python_deps() {
    log "INFO" "Installing Python dependencies..."
    
    # Upgrade pip
    ${PIP_CMD} install --upgrade pip setuptools wheel
    
    # Install from requirements
    if [ -f "${INSTALL_DIR}/requirements.txt" ]; then
        ${PIP_CMD} install -r "${INSTALL_DIR}/requirements.txt"
    else
        log "WARNING" "requirements.txt not found"
    fi
    
    log "SUCCESS" "Python dependencies installed"
}

# ==============================================================================
# DIRECTORY SETUP
# ==============================================================================

create_directories() {
    log "INFO" "Creating directories..."
    
    mkdir -p "${INSTALL_DIR}"
    mkdir -p "${CONFIG_DIR}"
    mkdir -p "${CONFIG_DIR}/payloads"
    mkdir -p "${CONFIG_DIR}/workspaces"
    mkdir -p "${CONFIG_DIR}/scans"
    mkdir -p "${CONFIG_DIR}/phishing_pages"
    mkdir -p "${CONFIG_DIR}/phishing_templates"
    mkdir -p "${CONFIG_DIR}/captured_credentials"
    mkdir -p "${CONFIG_DIR}/ssh_keys"
    mkdir -p "${CONFIG_DIR}/traffic_logs"
    mkdir -p "${CONFIG_DIR}/nikto_results"
    mkdir -p "${CONFIG_DIR}/web_templates"
    mkdir -p "${CONFIG_DIR}/sessions"
    mkdir -p "${CONFIG_DIR}/spear_phishing"
    mkdir -p "${CONFIG_DIR}/email_templates"
    mkdir -p "${CONFIG_DIR}/dos_logs"
    mkdir -p "${CONFIG_DIR}/agents"
    mkdir -p "${CONFIG_DIR}/c2_logs"
    mkdir -p "${CONFIG_DIR}/modules"
    mkdir -p "${CONFIG_DIR}/network_monitor"
    mkdir -p "${CONFIG_DIR}/keylog_exfil"
    mkdir -p "${CONFIG_DIR}/deployments"
    mkdir -p "${CONFIG_DIR}/domain_hosting"
    mkdir -p "${CONFIG_DIR}/docker_scans"
    mkdir -p "${CONFIG_DIR}/cracking"
    mkdir -p "${CONFIG_DIR}/wordlists"
    mkdir -p "${CONFIG_DIR}/reverse_engineering"
    mkdir -p "${CONFIG_DIR}/metasploit"
    mkdir -p "${CONFIG_DIR}/post_exploitation"
    mkdir -p "${CONFIG_DIR}/exploit_db"
    
    log "SUCCESS" "Directories created"
}

setup_virtualenv() {
    log "INFO" "Setting up virtual environment..."
    
    if [ ! -d "${VENV_DIR}" ]; then
        python3 -m venv "${VENV_DIR}"
    fi
    
    source "${VENV_DIR}/bin/activate"
    
    # Upgrade pip in venv
    pip install --upgrade pip setuptools wheel
    
    # Install requirements
    if [ -f "${INSTALL_DIR}/requirements.txt" ]; then
        pip install -r "${INSTALL_DIR}/requirements.txt"
    fi
    
    log "SUCCESS" "Virtual environment ready"
}

# ==============================================================================
# OPTIONAL TOOLS
# ==============================================================================

install_optional_tools() {
    log "INFO" "Installing optional security tools..."
    
    # Metasploit (if not installed)
    if ! command -v msfconsole &> /dev/null; then
        log "INFO" "Metasploit not found. Install manually for exploitation features."
    fi
    
    # Nikto (if not installed)
    if ! command -v nikto &> /dev/null; then
        log "INFO" "Installing Nikto..."
        case $OS in
            "debian")
                apt-get install -y nikto 2>/dev/null || true
                ;;
            "redhat")
                yum install -y nikto 2>/dev/null || true
                ;;
            "macos")
                brew install nikto 2>/dev/null || true
                ;;
        esac
    fi
    
    # Hashcat (if not installed)
    if ! command -v hashcat &> /dev/null; then
        log "INFO" "Installing Hashcat..."
        case $OS in
            "debian")
                apt-get install -y hashcat 2>/dev/null || true
                ;;
            "redhat")
                yum install -y hashcat 2>/dev/null || true
                ;;
            "macos")
                brew install hashcat 2>/dev/null || true
                ;;
        esac
    fi
    
    log "SUCCESS" "Optional tools installed"
}

# ==============================================================================
# CONFIGURATION
# ==============================================================================

create_default_config() {
    log "INFO" "Creating default configuration..."
    
    cat > "${CONFIG_DIR}/config.json" << 'EOF'
{
    "version": "1.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "auto_block_threshold": 5,
    "scan_timeout": 30,
    "report_format": "both",
    "generate_graphics": true,
    "keylogger": {
        "enabled": false,
        "hotkey": "f10",
        "log_file": "~/.war_shark/keylog.txt",
        "c2_server": "",
        "upload_interval": 30
    },
    "web": {
        "enabled": false,
        "port": 5000,
        "host": "0.0.0.0"
    },
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "syn_flood_threshold": 100,
        "http_flood_threshold": 200
    },
    "traffic_generation": {
        "enabled": true,
        "max_duration": 300,
        "max_packet_rate": 1000,
        "allow_floods": false
    },
    "social_engineering": {
        "enabled": true,
        "default_port": 8080,
        "capture_credentials": true
    },
    "ssh": {
        "enabled": true,
        "default_timeout": 30,
        "max_connections": 5
    },
    "dos": {
        "enabled": true,
        "max_threads": 100,
        "default_duration": 30
    }
}
EOF
    
    log "SUCCESS" "Default configuration created"
}

create_systemd_service() {
    if [[ "$OS" == "linux" ]] && command -v systemctl &> /dev/null; then
        log "INFO" "Creating systemd service..."
        
        cat > /etc/systemd/system/war-shark.service << EOF
[Unit]
Description=WAR-SHARK Cybersecurity Platform
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=${INSTALL_DIR}
Environment="PATH=${VENV_DIR}/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=${VENV_DIR}/bin/python3 ${INSTALL_DIR}/war_shark.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
        
        systemctl daemon-reload
        log "SUCCESS" "Systemd service created (enable with: systemctl enable war-shark)"
    fi
}

create_launcher() {
    log "INFO" "Creating launcher script..."
    
    cat > /usr/local/bin/war-shark << EOF
#!/bin/bash
source ${VENV_DIR}/bin/activate
cd ${INSTALL_DIR}
python3 war_shark.py "\$@"
EOF
    
    chmod +x /usr/local/bin/war-shark
    
    log "SUCCESS" "Launcher created at /usr/local/bin/war-shark"
}

# ==============================================================================
# POST-INSTALLATION
# ==============================================================================

post_install() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                                              ║${NC}"
    echo -e "${GREEN}║   ✅ WAR-SHARK Installation Complete!                                        ║${NC}"
    echo -e "${GREEN}║                                                                              ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}📁 Installation Directory:${NC} ${INSTALL_DIR}"
    echo -e "${CYAN}📁 Configuration Directory:${NC} ${CONFIG_DIR}"
    echo -e "${CYAN}📁 Log File:${NC} ${LOG_FILE}"
    echo ""
    echo -e "${YELLOW}🚀 To run WAR-SHARK:${NC}"
    echo -e "   ${WHITE}war-shark${NC}"
    echo ""
    echo -e "${YELLOW}🔧 To activate virtual environment:${NC}"
    echo -e "   ${WHITE}source ${VENV_DIR}/bin/activate${NC}"
    echo ""
    echo -e "${YELLOW}📊 To check service status:${NC}"
    echo -e "   ${WHITE}systemctl status war-shark${NC}"
    echo ""
    echo -e "${RED}⚠️  WARNING: For authorized security testing only!${NC}"
    echo ""
}

# ==============================================================================
# MAIN INSTALLATION
# ==============================================================================

main() {
    # Initialize log
    mkdir -p "$(dirname "${LOG_FILE}")" 2>/dev/null || true
    touch "${LOG_FILE}" 2>/dev/null || true
    
    print_banner
    
    # Check root
    check_root
    
    # Detect OS
    detect_os
    
    # Check Python
    check_python
    check_pip
    
    # Install system dependencies
    install_system_deps
    
    # Create directories
    create_directories
    
    # Setup virtual environment
    setup_virtualenv
    
    # Install Python dependencies
    source "${VENV_DIR}/bin/activate"
    install_python_deps
    
    # Install optional tools
    install_optional_tools
    
    # Create configuration
    create_default_config
    
    # Create launcher
    create_launcher
    
    # Create systemd service (optional)
    read -p "Create systemd service? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        create_systemd_service
    fi
    
    # Post-installation
    post_install
}

# Run main
main "$@"
