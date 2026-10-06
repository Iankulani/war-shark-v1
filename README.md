# war-shark-v1
<div align="center">

<img width="360" height="360" alt="shark" src="https://github.com/user-attachments/assets/5a780110-7466-4a3a-8969-5b157214e08f" />

[![GitHub stars](https://img.shields.io/github/stars/Iankulani/war-shark-v1?style=for-the-badge&logo=github)](https://github.com/Iankulani/war-shark-v1/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iankulani/war-shark-v1?style=for-the-badge&logo=github)](https://github.com/Iankulani/war-shark-v1/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/war-shark-v1?style=for-the-badge&logo=github)](https://github.com/Iankulani/war-shark-v1/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Iankulani/war-shark-v1?style=for-the-badge&logo=github)](https://github.com/Iankulani/war-shark-v1/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iankulani/war-shark-v1?style=for-the-badge&logo=git)](https://github.com/Iankulani/war-shark-v1/commits/main)
[![License](https://img.shields.io/github/license/Iankulani/war-shark-v1?style=for-the-badge)](https://github.com/Iankulani/war-shark-v1/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-blue?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Iankulani/war-shark-v1)
[![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-supported-blue?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/Iankulani/war-shark-v1)
[![Cybersecurity](https://img.shields.io/badge/cybersecurity-authorized%20testing-red?style=for-the-badge&logo=github)](https://github.com/Iankulani/war-shark-v1)

</div>


War Shark is a cybersecurity research and command platform designed to provide security professionals, researchers, penetration testers, red-team practitioners, and ethical hackers with a centralized way to interact with cybersecurity tools and authorized testing environments. The platform is built around the idea of making security operations more accessible by allowing users to send and execute approved commands through multiple communication platforms.

War Shark can be accessed through Discord, Telegram, Slack, Google Chat, and a Web Application, giving authorized users flexibility in how they interact with the platform. Instead of requiring a security researcher to remain connected to a single terminal interface, War Shark can provide a command-oriented interface through supported communication channels. Users can submit commands, receive responses, monitor activities, and interact with their authorized security environments from their preferred platform.

The primary purpose of War Shark is cybersecurity research, education, security testing, and authorized penetration testing. It can be used in controlled laboratories, capture-the-flag environments, defensive security projects, vulnerability assessments, red-team exercises, and other situations where the user has explicit permission to test the target systems.

War Shark can also serve as an experimental platform for researchers interested in remote command interfaces, security automation, network security, digital forensics, threat analysis, and cybersecurity operations. Researchers can use the platform to study how command-based security workflows can be integrated with modern communication systems and web technologies.

For red-team and penetration-testing activities, War Shark can help authorized security teams organize testing commands and interact with systems that are part of an approved assessment. Security researchers can use it to experiment with defensive controls, logging, monitoring, authentication, access management, and incident-response workflows.

War Shark may also be useful for researchers studying different hacker methodologies, including black-hat, white-hat, and red-hat concepts, from a security-research and educational perspective. However, the platform should only be used against systems, networks, applications, or devices for which the user has explicit authorization. Unauthorized access, disruption, credential theft, data destruction, or attacks against third-party infrastructure are outside the intended purpose of the project.

The architecture of War Shark can be expanded with additional cybersecurity modules, command handlers, authentication mechanisms, logging systems, monitoring capabilities, and integrations. Its multi-platform design makes it possible to build security workflows that connect communication interfaces with authorized cybersecurity environments.

War Shark is ultimately designed as a cybersecurity research platform where command execution, automation, communication, and security experimentation meet. Whether used in a personal laboratory, cybersecurity classroom, CTF environment, penetration-testing engagement, or professional security research project, War Shark provides a flexible foundation for exploring modern cybersecurity operations.


# Docker
```bash
docker run -d \
  --name war-shark \
  -p 5000:5000 \
  -p 8080:8080 \
  -v warshark-config:/root/.war_shark \
  warshark/war-shark:latest
```
# Manual Install

# Clone repository

```bash
git clone https://github.com/Iankulani/war-shark-v1.git
cd war-shark-v1
```
# Run installation script

```bash
sudo chmod +x install.sh
sudo ./install.sh
```
# 📦 Installation
* Prerequisites
* Python 3.8+

* pip

* git

* Nmap

* Netcat

* curl/wget

# Linux (Debian/Ubuntu)

# Install system dependencies
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git nmap netcat-openbsd dnsutils traceroute whois
```

# Clone and install

```bash
git clone https://github.com//Iankulani/war-shark.git
cd war-shark
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
    
# Linux (RHEL/CentOS)

# Install system dependencies
```bash
sudo yum install -y python3 python3-pip git nmap nc bind-utils traceroute whois
```
# Clone and install
```bash
git clone https://github.com/Iankulani/war-shark-v1.git
cd war-shark-v1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# macOS

# Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
# Install dependencies
```bash
brew install python3 git nmap netcat bind traceroute whois
```
# Clone and install

```bash
git clone https://github.com/ian-carter-kulani/war-shark.git
cd war-shark
python3 -m venv venv
source venv/bin/activate
```
pip install -r requirements.txt

# Windows
# powershell
# Run PowerShell as Administrator
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force
.\install.ps1
Or use the batch file:
```
cmd
install.bat
🐳 Docker
Build Image
```bash
docker build -t warshark/war-shark:latest .
Run Container
```
docker run -d \
  --name war-shark \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  -p 5000:5000 \
  -p 8080:8080 \
  -p 4444:4444 \
  -p 5555:5555 \
  -v warshark-config:/root/.war_shark \
  -v warshark-reports:/opt/war-shark/reports \
  warshark/war-shark:latest
```
# Docker Compose
```bash
docker-compose up -d
```
# Access Web Dashboard
# Open your browser and navigate to:

```bash
http://localhost:5000
```
# ⚙️ Configuration
```bash
Configuration is stored in ~/.war_shark-v1/config.json.

Example Configuration
json
{
    "version": "1.0.0",
    "web": {
        "enabled": true,
        "port": 5000,
        "host": "0.0.0.0"
    },
    "keylogger": {
        "enabled": false,
        "hotkey": "f10",
        "upload_interval": 30
    },
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "syn_flood_threshold": 100
    }
}
Environment Variables
Copy .env.example to .env and configure:

bash
cp .env.example .env
nano .env
# 🎮 Usage
Start WAR-SHARK
bash
# Activate virtual environment
```bash
source venv/bin/activate
```
# Run
```bash
python3 war_shark.py
Interactive Shell
```

🦈> help                    # Show all commands
🦈> nmap 192.168.1.1        # Scan target
🦈> phish_gmail             # Generate phishing link
🦈> metasploit_search smb   # Search exploits
🦈> rev_analyze /bin/ls     # Analyze binary
🦈> crack md5 5d41402abc4b2a76b9719d911017c592
```

# 🤖 Platform Integrations

# Discord
```bash

!nmap 192.168.1.1
!phish_gmail
!status
```
# Telegram
```bash
/nmap 192.168.1.1
/phish_gmail
/status
```

# Slack
```bash
!nmap 192.168.1.1
!phish_gmail
!status
```

# 🛠️ Development
```bash
Setup Develo
pment Environment
```

# Clone repository

```bash
git clone https://github.com/ian-carter-kulani/war-shark.git
cd war-shark
```
# Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
# Install development dependencies
```bash
pip install -r requirements-dev.txt
```

# Install pre-commit hooks
```bash
pre-commit install
Run Tests
bash
# All tests
pytest tests/ -v

# Unit tests
pytest tests/unit/ -v

# With coverage
```bash
pytest tests/ --cov=war_shark --cov-report=html
Linting
```
# Run all linters
```bash
make lint
```

# Format code
make format
Build
bash
# Build package
```bash
make build
```
# Build Docker image
```bash
make docker-build
🧪 Testing
```

# Run all tests
```bash
make test
```

# Run unit tests
```bash
make test-unit
```

# Run integration tests
```bash
make test-integration
```

# Run with coverage
make test-cov
🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Guidelines
Follow PEP 8 style guide

Write tests for new features

Update documentation

Run linters before committing




# 📚 Commands

## Network Commands

| Command | Description |
|---------|-------------|
| `ping <target>` | Ping a target |
| `traceroute <target>` | Trace route |
| `nmap <target> [type]` | Port scan |
| `curl <url>` | HTTP request |
| `netcat <host> <port>` | Netcat connection |

## Exploitation Commands

| Command | Description |
|---------|-------------|
| `metasploit_search <query>` | Search exploits |
| `metasploit_exploit <exploit> <payload> <target>` | Run exploit |
| `metasploit_payload <type> <lhost> <lport> <output>` | Generate payload |
| `metasploit_handler <lhost> <lport>` | Start handler |

## Social Engineering Commands

| Command | Description |
|---------|-------------|
| `phish_<platform>` | Generate phishing link |
| `phish_start <link_id> [port]` | Start phishing server |
| `phish_stop` | Stop phishing server |
| `phish_creds [link_id]` | View captured credentials |

## Keylogger Commands

| Command | Description |
|---------|-------------|
| `keylogger_start` | Start keylogger |
| `keylogger_stop` | Stop keylogger |
| `keylogger_status` | Check status |
| `keylogger_logs [limit]` | View keylogs |
| `keylogger_screenshots` | View screenshots |

## System Commands

| Command | Description |
|---------|-------------|
| `status` | System status |
| `history [limit]` | Command history |
| `system` | System info |
| `threats [limit]` | Recent threats |
| `report` | Security report |
| `help` | Help menu |

# Docuemtation

# References

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Iankulani/war-shark-v1&type=Date)](https://star-history.com/#Iankulani/war-shark-v1&Date)


