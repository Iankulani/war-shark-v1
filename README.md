# war-shark-v1
<div align="center">

<img width="360" height="360" alt="shark" src="https://github.com/user-attachments/assets/5a780110-7466-4a3a-8969-5b157214e08f" />


</div>

War shark

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

