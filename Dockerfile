# ==============================================================================
# WAR-SHARK-v1 - Docker Configuration
# Author: Ian Carter Kulani
# Version: 1.0.0
# ==============================================================================

# ------------------------------------------------------------------------------
# Stage 1: Builder
# ------------------------------------------------------------------------------
FROM python:3.11-slim-bookworm AS builder

LABEL maintainer="Ian Carter Kulani <ian.kulani@warshark.io>"
LABEL org.opencontainers.image.title="WAR-SHARK"
LABEL org.opencontainers.image.description="Ultimate Cybersecurity Command & Control Platform"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.author="Ian Carter Kulani"
LABEL org.opencontainers.image.licenses="MIT"

# Build arguments
ARG DEBIAN_FRONTEND=noninteractive
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION=1.0.0

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive \
    WARSHARK_VERSION=${VERSION} \
    WARSHARK_HOME=/opt/war-shark \
    WARSHARK_CONFIG=/root/.war_shark

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
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
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Copy requirements
WORKDIR /tmp
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# ------------------------------------------------------------------------------
# Stage 2: Runtime
# ------------------------------------------------------------------------------
FROM python:3.11-slim-bookworm AS runtime

LABEL maintainer="Ian Carter Kulani <ian.kulani@warshark.io>"
LABEL org.opencontainers.image.title="WAR-SHARK"
LABEL org.opencontainers.image.description="Ultimate Cybersecurity Command & Control Platform"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.author="Ian Carter Kulani"
LABEL org.opencontainers.image.licenses="MIT"

# Build arguments
ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH" \
    WARSHARK_VERSION=${VERSION} \
    WARSHARK_HOME=/opt/war-shark \
    WARSHARK_CONFIG=/root/.war_shark

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Core utilities
    ca-certificates \
    curl \
    wget \
    git \
    # Network tools
    nmap \
    netcat-openbsd \
    dnsutils \
    traceroute \
    whois \
    tcpdump \
    iputils-ping \
    net-tools \
    iproute2 \
    # Libraries
    libpcap0.8 \
    libssl3 \
    libffi8 \
    libxml2 \
    libxslt1.1 \
    zlib1g \
    libjpeg62-turbo \
    libpng16-16 \
    libfreetype6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    # Optional security tools
    nikto \
    hashcat \
    john \
    hydra \
    sqlmap \
    # Development tools
    vim \
    nano \
    less \
    procps \
    htop \
    # Python runtime
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create application directories
RUN mkdir -p ${WARSHARK_HOME} \
    ${WARSHARK_CONFIG} \
    ${WARSHARK_CONFIG}/payloads \
    ${WARSHARK_CONFIG}/workspaces \
    ${WARSHARK_CONFIG}/scans \
    ${WARSHARK_CONFIG}/phishing_pages \
    ${WARSHARK_CONFIG}/phishing_templates \
    ${WARSHARK_CONFIG}/captured_credentials \
    ${WARSHARK_CONFIG}/ssh_keys \
    ${WARSHARK_CONFIG}/traffic_logs \
    ${WARSHARK_CONFIG}/nikto_results \
    ${WARSHARK_CONFIG}/web_templates \
    ${WARSHARK_CONFIG}/sessions \
    ${WARSHARK_CONFIG}/spear_phishing \
    ${WARSHARK_CONFIG}/email_templates \
    ${WARSHARK_CONFIG}/dos_logs \
    ${WARSHARK_CONFIG}/agents \
    ${WARSHARK_CONFIG}/c2_logs \
    ${WARSHARK_CONFIG}/modules \
    ${WARSHARK_CONFIG}/network_monitor \
    ${WARSHARK_CONFIG}/keylog_exfil \
    ${WARSHARK_CONFIG}/deployments \
    ${WARSHARK_CONFIG}/domain_hosting \
    ${WARSHARK_CONFIG}/docker_scans \
    ${WARSHARK_CONFIG}/cracking \
    ${WARSHARK_CONFIG}/wordlists \
    ${WARSHARK_CONFIG}/reverse_engineering \
    ${WARSHARK_CONFIG}/metasploit \
    ${WARSHARK_CONFIG}/post_exploitation \
    ${WARSHARK_CONFIG}/exploit_db

# Set working directory
WORKDIR ${WARSHARK_HOME}

# Copy application files
COPY . .

# Create default configuration
RUN cat > ${WARSHARK_CONFIG}/config.json << 'EOF'
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
        "log_file": "/root/.war_shark/keylog.txt",
        "c2_server": "",
        "upload_interval": 30
    },
    "web": {
        "enabled": true,
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

# Create entrypoint script
RUN cat > /entrypoint.sh << 'EOF'
#!/bin/bash
set -e

echo "🦈 Starting WAR-SHARK..."
echo "Version: ${WARSHARK_VERSION}"
echo "Home: ${WARSHARK_HOME}"
echo "Config: ${WARSHARK_CONFIG}"
echo ""

# Check if custom command provided
if [ $# -gt 0 ]; then
    exec "$@"
fi

# Default: run WAR-SHARK
cd ${WARSHARK_HOME}
exec python3 war_shark.py
EOF

RUN chmod +x /entrypoint.sh

# Create non-root user (optional, for security)
# RUN useradd -m -s /bin/bash warshark && \
#     chown -R warshark:warshark ${WARSHARK_HOME} ${WARSHARK_CONFIG}

# Expose ports
# 5000 - Web Dashboard
# 8080 - Phishing Server
# 4444 - Metasploit Handler
# 5555 - Agent C2 Server
EXPOSE 5000 8080 4444 5555

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import requests; requests.get('http://localhost:5000/api/stats', timeout=5)" || exit 1

# Volume for persistent data
VOLUME ["/root/.war_shark", "/opt/war-shark/reports"]

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command
CMD ["python3", "war_shark.py"]
