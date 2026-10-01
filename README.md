# war-shark-v1
<div align="center">

<img width="360" height="360" alt="shark" src="https://github.com/user-attachments/assets/5a780110-7466-4a3a-8969-5b157214e08f" />


</div>



Docker
bash
docker run -d \
  --name war-shark \
  -p 5000:5000 \
  -p 8080:8080 \
  -v warshark-config:/root/.war_shark \
  warshark/war-shark:latest
Manual Install
bash
# Clone repository
git clone https://github.com/ian-carter-kulani/war-shark.git
cd war-shark

# Run installation script
```bash
sudo chmod +x install.sh
sudo ./install.sh
```
# 📦 Installation
Prerequisites
Python 3.8+

pip

git

Nmap

Netcat

curl/wget

Linux (Debian/Ubuntu)
bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git nmap netcat-openbsd dnsutils traceroute whois

# Clone and install
git clone https://github.com/ian-carter-kulani/war-shark.git
cd war-shark
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Linux (RHEL/CentOS)
bash
# Install system dependencies
sudo yum install -y python3 python3-pip git nmap nc bind-utils traceroute whois

# Clone and install
```bash
git clone https://github.com/ian-carter-kulani/war-shark.git
cd war-shark
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
Windows
powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
.\install.ps1
Or use the batch file:

cmd
install.bat
🐳 Docker
Build Image
bash
docker build -t warshark/war-shark:latest .
Run Container
```bash
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
Configuration is stored in ~/.war_shark/config.json.

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
🎮 Usage
Start WAR-SHARK
bash
# Activate virtual environment
source venv/bin/activate

# Run
python3 war_shark.py
Interactive Shell
```bash
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
pytest tests/ --cov=war_shark --cov-report=html
Linting
bash
# Run all linters
make lint

# Format code
make format
Build
bash
# Build package
make build

# Build Docker image
make docker-build
🧪 Testing
bash
# Run all tests
```basg
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

