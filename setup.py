#!/usr/bin/env python3
"""
WAR-SHARK-v1 - Ultimate Cybersecurity Command & Control Platform
Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = ""
readme_path = this_directory / "README.md"
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

# Read requirements
def read_requirements(filename):
    requirements = []
    req_path = this_directory / filename
    if req_path.exists():
        with open(req_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('-'):
                    requirements.append(line)
    return requirements

setup(
    name="war-shark",
    version="1.0.0",
    author="Ian Carter Kulani",
    author_email="ian.kulani@warshark.io",
    description="Ultimate Cybersecurity Command & Control Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ian-carter-kulani/war-shark",
    project_urls={
        "Bug Tracker": "https://github.com/ian-carter-kulani/war-shark/issues",
        "Documentation": "https://war-shark.readthedocs.io",
        "Source Code": "https://github.com/ian-carter-kulani/war-shark",
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    py_modules=["war_shark"],
    python_requires=">=3.8",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
        "prod": read_requirements("requirements-prod.txt"),
    },
    entry_points={
        "console_scripts": [
            "war-shark=war_shark:main",
            "warshark=war_shark:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Utilities",
    ],
    keywords=[
        "cybersecurity", "penetration-testing", "security-tools",
        "network-scanning", "vulnerability-assessment", "red-team",
        "command-and-control", "c2", "exploitation", "post-exploitation",
    ],
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.json", "*.yml", "*.yaml", "*.cfg", "*.ini"],
    },
    zip_safe=False,
)
