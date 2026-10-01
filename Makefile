# ==============================================================================
# WAR-SHARK-v1 - Makefile
# Author: Ian Carter Kulani
# Version: 1.0.0
# ==============================================================================

.PHONY: help install install-dev test lint clean build docker docker-build docker-run docker-stop deploy docs

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
VENV := venv
PROJECT := war-shark
VERSION := 1.0.0
DOCKER_IMAGE := warshark/war-shark
DOCKER_TAG := $(VERSION)

# Colors
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m

# ==============================================================================
# HELP
# ==============================================================================
help:
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║           🦈 WAR-SHARK-v1 - Makefile Help                        ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)Installation:$(NC)"
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install development dependencies"
	@echo "  make venv           - Create virtual environment"
	@echo ""
	@echo "$(GREEN)Testing:$(NC)"
	@echo "  make test           - Run all tests"
	@echo "  make test-unit      - Run unit tests"
	@echo "  make test-cov       - Run tests with coverage"
	@echo "  make lint           - Run linters"
	@echo ""
	@echo "$(GREEN)Building:$(NC)"
	@echo "  make build          - Build Python package"
	@echo "  make clean          - Clean build artifacts"
	@echo ""
	@echo "$(GREEN)Docker:$(NC)"
	@echo "  make docker-build   - Build Docker image"
	@echo "  make docker-run     - Run Docker container"
	@echo "  make docker-stop    - Stop Docker container"
	@echo "  make docker-logs    - View Docker logs"
	@echo ""
	@echo "$(GREEN)Documentation:$(NC)"
	@echo "  make docs           - Build documentation"
	@echo "  make docs-serve     - Serve documentation locally"
	@echo ""

# ==============================================================================
# VIRTUAL ENVIRONMENT
# ==============================================================================
venv:
	@echo "$(BLUE)🔧 Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✅ Virtual environment created$(NC)"
	@echo "$(YELLOW)   Run: source $(VENV)/bin/activate$(NC)"

# ==============================================================================
# INSTALLATION
# ==============================================================================
install: venv
	@echo "$(BLUE)📦 Installing production dependencies...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install --upgrade pip setuptools wheel
	. $(VENV)/bin/activate && $(PIP) install -r requirements-prod.txt
	@echo "$(GREEN)✅ Production dependencies installed$(NC)"

install-dev: venv
	@echo "$(BLUE)📦 Installing development dependencies...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install --upgrade pip setuptools wheel
	. $(VENV)/bin/activate && $(PIP) install -r requirements-dev.txt
	@echo "$(GREEN)✅ Development dependencies installed$(NC)"

install-all: venv
	@echo "$(BLUE)📦 Installing all dependencies...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install --upgrade pip setuptools wheel
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	. $(VENV)/bin/activate && $(PIP) install -r requirements-dev.txt
	@echo "$(GREEN)✅ All dependencies installed$(NC)"

# ==============================================================================
# TESTING
# ==============================================================================
test:
	@echo "$(BLUE)🧪 Running tests...$(NC)"
	. $(VENV)/bin/activate && pytest tests/ -v
	@echo "$(GREEN)✅ Tests complete$(NC)"

test-unit:
	@echo "$(BLUE)🧪 Running unit tests...$(NC)"
	. $(VENV)/bin/activate && pytest tests/unit/ -v
	@echo "$(GREEN)✅ Unit tests complete$(NC)"

test-integration:
	@echo "$(BLUE)🧪 Running integration tests...$(NC)"
	. $(VENV)/bin/activate && pytest tests/integration/ -v
	@echo "$(GREEN)✅ Integration tests complete$(NC)"

test-cov:
	@echo "$(BLUE)🧪 Running tests with coverage...$(NC)"
	. $(VENV)/bin/activate && pytest tests/ \
		-v \
		--cov=war_shark \
		--cov-report=term-missing \
		--cov-report=html:coverage_html \
		--cov-report=xml:coverage.xml
	@echo "$(GREEN)✅ Coverage report generated$(NC)"

test-security:
	@echo "$(BLUE)🔒 Running security tests...$(NC)"
	. $(VENV)/bin/activate && bandit -r war_shark.py
	. $(VENV)/bin/activate && safety check
	@echo "$(GREEN)✅ Security tests complete$(NC)"

# ==============================================================================
# LINTING
# ==============================================================================
lint:
	@echo "$(BLUE)🔍 Running linters...$(NC)"
	@echo "$(YELLOW)--- Black ---$(NC)"
	. $(VENV)/bin/activate && black --check --diff war_shark.py || true
	@echo "$(YELLOW)--- isort ---$(NC)"
	. $(VENV)/bin/activate && isort --check-only --diff war_shark.py || true
	@echo "$(YELLOW)--- Flake8 ---$(NC)"
	. $(VENV)/bin/activate && flake8 war_shark.py --max-line-length=120 --ignore=E501,W503,E203 || true
	@echo "$(YELLOW)--- MyPy ---$(NC)"
	. $(VENV)/bin/activate && mypy war_shark.py --ignore-missing-imports || true
	@echo "$(GREEN)✅ Linting complete$(NC)"

format:
	@echo "$(BLUE)🎨 Formatting code...$(NC)"
	. $(VENV)/bin/activate && black war_shark.py
	. $(VENV)/bin/activate && isort war_shark.py
	@echo "$(GREEN)✅ Code formatted$(NC)"

# ==============================================================================
# BUILDING
# ==============================================================================
build: clean
	@echo "$(BLUE)📦 Building package...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install build
	. $(VENV)/bin/activate && $(PYTHON) -m build
	@echo "$(GREEN)✅ Package built$(NC)"

build-wheel: clean
	@echo "$(BLUE)📦 Building wheel...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install build
	. $(VENV)/bin/activate && $(PYTHON) -m build --wheel
	@echo "$(GREEN)✅ Wheel built$(NC)"

build-sdist: clean
	@echo "$(BLUE)📦 Building source distribution...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install build
	. $(VENV)/bin/activate && $(PYTHON) -m build --sdist
	@echo "$(GREEN)✅ Source distribution built$(NC)"

clean:
	@echo "$(BLUE)🧹 Cleaning build artifacts...$(NC)"
	rm -rf build/ dist/ *.egg-info/ .eggs/
	rm -rf .pytest_cache/ .mypy_cache/ .coverage coverage.xml coverage_html/
	rm -rf htmlcov/ .tox/ .nox/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Cleaned$(NC)"

# ==============================================================================
# DOCKER
# ==============================================================================
docker-build:
	@echo "$(BLUE)🐳 Building Docker image...$(NC)"
	docker build \
		--build-arg VERSION=$(VERSION) \
		--build-arg BUILD_DATE=$$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
		--build-arg VCS_REF=$$(git rev-parse --short HEAD 2>/dev/null || echo "unknown") \
		-t $(DOCKER_IMAGE):$(DOCKER_TAG) \
		-t $(DOCKER_IMAGE):latest \
		-f Dockerfile .
	@echo "$(GREEN)✅ Docker image built$(NC)"

docker-run:
	@echo "$(BLUE)🐳 Starting Docker container...$(NC)"
	docker run -d \
		--name war-shark \
		-p 5000:5000 \
		-p 8080:8080 \
		-p 4444:4444 \
		-p 5555:5555 \
		-v warshark-config:/root/.war_shark \
		-v warshark-reports:/opt/war-shark/reports \
		$(DOCKER_IMAGE):$(DOCKER_TAG)
	@echo "$(GREEN)✅ Container started$(NC)"
	@echo "$(YELLOW)   Web dashboard: http://localhost:5000$(NC)"

docker-stop:
	@echo "$(BLUE)🐳 Stopping Docker container...$(NC)"
	docker stop war-shark || true
	docker rm war-shark || true
	@echo "$(GREEN)✅ Container stopped$(NC)"

docker-logs:
	@echo "$(BLUE)📋 Docker logs:$(NC)"
	docker logs -f war-shark

docker-compose-up:
	@echo "$(BLUE)🐳 Starting with docker-compose...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✅ Services started$(NC)"

docker-compose-down:
	@echo "$(BLUE)🐳 Stopping docker-compose...$(NC)"
	docker-compose down
	@echo "$(GREEN)✅ Services stopped$(NC)"

docker-clean:
	@echo "$(BLUE)🧹 Cleaning Docker artifacts...$(NC)"
	docker rmi $(DOCKER_IMAGE):$(DOCKER_TAG) || true
	docker rmi $(DOCKER_IMAGE):latest || true
	docker volume rm warshark-config warshark-reports || true
	@echo "$(GREEN)✅ Docker cleaned$(NC)"

# ==============================================================================
# DOCUMENTATION
# ==============================================================================
docs:
	@echo "$(BLUE)📚 Building documentation...$(NC)"
	. $(VENV)/bin/activate && mkdocs build
	@echo "$(GREEN)✅ Documentation built$(NC)"

docs-serve:
	@echo "$(BLUE)📚 Serving documentation...$(NC)"
	. $(VENV)/bin/activate && mkdocs serve

# ==============================================================================
# DEPLOYMENT
# ==============================================================================
deploy-staging:
	@echo "$(BLUE)🚀 Deploying to staging...$(NC)"
	@echo "$(YELLOW)   Configure your staging deployment here$(NC)"

deploy-production:
	@echo "$(BLUE)🚀 Deploying to production...$(NC)"
	@echo "$(YELLOW)   Configure your production deployment here$(NC)"

# ==============================================================================
# UTILITIES
# ==============================================================================
run:
	@echo "$(BLUE)🦈 Starting WAR-SHARK...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) war_shark.py

version:
	@echo "$(PROJECT) v$(VERSION)"

check:
	@echo "$(BLUE)🔍 Checking environment...$(NC)"
	@echo "Python: $$(python3 --version)"
	@echo "Pip: $$(pip3 --version)"
	@echo "Docker: $$(docker --version 2>/dev/null || echo 'not installed')"
	@echo "Git: $$(git --version 2>/dev/null || echo 'not installed')"
	@echo "Nmap: $$(nmap --version 2>/dev/null | head -1 || echo 'not installed')"

# Default target
.DEFAULT_GOAL := help
