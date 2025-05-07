# DevOps/SRE Career Path: Development Environment Setup Guide

This guide provides comprehensive setup instructions for the learning environment needed to complete the 24-month DevOps/SRE career roadmap, with a focus on financial services platform engineering.

## Table of Contents

1. [Environment Overview](#environment-overview)
2. [Hardware Recommendations](#hardware-recommendations)
3. [Base Operating System Setup](#base-operating-system-setup)
4. [Linux Environment Setup](#linux-environment-setup)
5. [Essential Development Tools](#essential-development-tools)
6. [Phase-Specific Environment Configurations](#phase-specific-environment-configurations)
7. [Project Environment Templates](#project-environment-templates)
8. [Learning Resources Access](#learning-resources-access)
9. [Environment Management Scripts](#environment-management-scripts)
10. [Tracking System Integration](#tracking-system-integration)

## Environment Overview

The learning environment for this DevOps/SRE career roadmap requires a dual approach:

1. **Primary Development System**: MacOS with terminal-centric workflow
2. **Linux Learning Environments**: Virtualized Linux distributions for hands-on practice

This approach provides the flexibility of your familiar MacOS system while ensuring you gain deep experience with Linux environments that are essential for DevOps roles.

## Hardware Recommendations

Your current hardware is well-suited for this learning path:

- **Mac Mini with Apple M4 chip and 16GB RAM**
- **Dual 4K monitors** (excellent for documentation alongside practical work)

This configuration provides sufficient resources for running:
- Your primary MacOS workspace
- 2-3 concurrent Linux virtual machines
- Docker containers for development
- Cloud-based development environments

## Base Operating System Setup

### MacOS Configuration

1. **Terminal Setup**:
   ```bash
   # Install Homebrew
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install terminal essentials
   brew install zsh tmux neovim git jq httpie tree
   
   # Install oh-my-zsh for enhanced terminal experience
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```

2. **Development Directory Structure**:
   ```bash
   # Create primary directory structure
   mkdir -p ~/DevOps/{projects,learning,environments,certifications,scripts}
   
   # Create project-specific directories
   mkdir -p ~/DevOps/projects/{ruby-microservice,terraform-modules,kubernetes-platform}
   
   # Create certification directories
   mkdir -p ~/DevOps/certifications/{terraform,aws-associate,kubernetes-cka,aws-devops-pro,kubernetes-cks}
   ```

3. **macOS System Preferences**:
   - Enable full disk access for Terminal
   - Configure keyboard shortcuts for window management
   - Set up hot corners for workspace switching
   - Configure Time Machine backups for your learning material

## Linux Environment Setup

For this roadmap, you'll need to set up Linux environments for hands-on practice. The best approach is to use virtualization on your Mac mini.

### UTM Setup for Linux VMs

1. **Install UTM**:
   ```bash
   brew install --cask utm
   ```

2. **Linux Distribution Selection**:
   - **Primary Learning VM**: Ubuntu Server ARM64 (LTS version)
   - **Secondary VM**: Rocky Linux ARM64 (RHEL-compatible)
   
   These two distributions cover the major Linux families (Debian-based and RHEL-based) that you'll encounter in enterprise environments.

3. **VM Resource Allocation (per VM)**:
   - 4GB RAM
   - 4 CPU cores
   - 50GB storage
   - Shared folder for easy file exchange

### Setting Up Primary Ubuntu VM

1. **Download Ubuntu Server ARM64**:
   - Visit [Ubuntu Server download page](https://ubuntu.com/download/server/arm) 
   - Select the ARM64 LTS version

2. **VM Creation in UTM**:
   - Open UTM application
   - Click "Create VM"
   - Select "Virtualize"
   - Choose "Linux"
   - Select the Ubuntu Server ISO
   - Set 4GB RAM, 4 CPU cores
   - Create 50GB virtual disk
   - Enable shared directory 

3. **Post-Installation Setup**:
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install essential development tools
   sudo apt install -y build-essential curl wget git vim tmux zsh htop
   
   # Setup shared directory for file exchange with your Mac
   mkdir ~/host-share
   
   # Install oh-my-zsh
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```

### Setting Up Rocky Linux VM

1. **Download Rocky Linux ARM64**:
   - Visit [Rocky Linux download page](https://rockylinux.org/download/) 
   - Select the ARM64 minimal version

2. **VM Creation in UTM**:
   - Follow similar steps as for Ubuntu VM
   - Adjust settings appropriately

3. **Post-Installation Setup**:
   ```bash
   # Update system
   sudo dnf update -y
   
   # Install development group
   sudo dnf groupinstall "Development Tools" -y
   
   # Install essential packages
   sudo dnf install -y curl wget git vim tmux zsh htop
   ```

## Essential Development Tools

Install these core tools on your Mac system to support your DevOps learning journey:

```bash
# Install CLI tools
brew install awscli terraform kubectl kubectx helm docker jq yq

# Install development tools
brew install --cask visual-studio-code postman

# Install UTM for virtualization
brew install --cask utm

# Install Docker Desktop (ARM native)
brew install --cask docker

# Install language tools
brew install ruby python@3.11 node
```

## Phase-Specific Environment Configurations

### Phase 1: Foundation Building (Months 1-3)

#### Linux/Unix Environment Setup
```bash
# Create Linux practice directory
mkdir -p ~/DevOps/environments/linux-practice

# Create Docker practice directory
mkdir -p ~/DevOps/environments/docker-practice

# Create Git workflow directory
mkdir -p ~/DevOps/environments/git-practice

# Create Terraform practice directory
mkdir -p ~/DevOps/environments/terraform-practice
```

### Phase 2: Cloud and Infrastructure Automation (Months 4-6)

#### AWS Environment Setup
```bash
# Install AWS CLI (if not already installed)
brew install awscli

# Configure AWS CLI with credentials (after creating account)
aws configure

# Create AWS practice directory
mkdir -p ~/DevOps/environments/aws-practice

# Create Terraform + AWS directory
mkdir -p ~/DevOps/environments/terraform-aws
```

### Phase 3-6 (Docker Desktop Setup)

For later phases involving container orchestration, ensure Docker Desktop is properly configured:

```bash
# Verify Docker installation
docker --version

# Configure Docker Desktop resources
# Open Docker Desktop > Settings > Resources
# Allocate at least 6GB RAM and 4 CPUs

# Test Docker installation
docker run --rm hello-world
```

## Project Environment Templates

Create template environments for each major project:

### Ruby Microservice Project Template
```bash
mkdir -p ~/DevOps/templates/ruby-microservice
cd ~/DevOps/templates/ruby-microservice

# Create directory structure
mkdir -p {app,config,spec,docker,ci}

# Create template Dockerfile
cat > docker/Dockerfile << 'EOF'
FROM ruby:3.2-alpine
WORKDIR /app
COPY Gemfile* ./
RUN bundle install
COPY . .
CMD ["bundle", "exec", "rackup", "-p", "4567", "-o", "0.0.0.0"]
EOF

# Create template GitHub Actions workflow
mkdir -p .github/workflows
cat > .github/workflows/ci.yml << 'EOF'
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.2'
      - name: Install dependencies
        run: bundle install
      - name: Run tests
        run: bundle exec rspec
EOF

# Create template README
cat > README.md << 'EOF'
# Ruby Microservice Template

This template provides the foundation for building a Ruby microservice with CI/CD integration.

## Features
- Ruby application structure
- Docker containerization
- GitHub Actions CI/CD pipeline
- Testing framework

## Acknowledgements

This project was developed with assistance from Anthropic's Claude AI assistant, which helped with:
- Documentation writing and organization
- Code structure suggestions
- Troubleshooting and debugging assistance

Claude was used as a development aid while all final implementation decisions and code review were performed by Joshua Michael Hall.

## Disclaimer
This project is in progress. No liability for any issues that may arise from its use. Please report any issues you encounter.
EOF
```

### Infrastructure as Code Project Template
```bash
mkdir -p ~/DevOps/templates/terraform-aws
cd ~/DevOps/templates/terraform-aws

# Create directory structure
mkdir -p {modules,environments/{dev,prod},scripts}

# Create template provider configuration
cat > provider.tf << 'EOF'
provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
    }
  }
}

terraform {
  required_version = ">= 1.0.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  
  backend "s3" {
    # Will be configured per environment
  }
}
EOF

# Create template README
cat > README.md << 'EOF'
# Terraform AWS Infrastructure Template

This template provides a structured approach to managing AWS infrastructure as code.

## Features
- Modular design for reusable components
- Environment separation (dev/prod)
- S3 backend for state management
- Compliance documentation

## Acknowledgements

This project was developed with assistance from Anthropic's Claude AI assistant, which helped with:
- Documentation writing and organization
- Code structure suggestions
- Troubleshooting and debugging assistance

Claude was used as a development aid while all final implementation decisions and code review were performed by Joshua Michael Hall.

## Disclaimer
This project is in progress. No liability for any issues that may arise from its use. Please report any issues you encounter.
EOF
```

## Learning Resources Access

Set up easy access to learning resources:

```bash
# Create learning resources directory
mkdir -p ~/DevOps/learning/{books,courses,documentation,labs}

# Create shell script to organize resources
cat > ~/DevOps/scripts/setup-resources.sh << 'EOF'
#!/bin/bash

# Create directory structure for learning resources
mkdir -p ~/DevOps/learning/books/{linux,docker,terraform,aws,kubernetes,devops}
mkdir -p ~/DevOps/learning/courses/{linux-foundation,aws,terraform,kubernetes}
mkdir -p ~/DevOps/learning/documentation/{linux,docker,terraform,aws,kubernetes}
mkdir -p ~/DevOps/learning/labs/{linux,docker,terraform,aws,kubernetes}

# Create README files for each resource type
cat > ~/DevOps/learning/books/README.md << 'END'
# Books for DevOps Learning

## Linux
- "The Linux Command Line" by William Shotts
- "Linux Pocket Guide" by Daniel J. Barrett

## Docker
- "Docker Deep Dive" by Nigel Poulton
- "Docker in Practice" by Ian Miell & Aidan Hobson Sayers

## Terraform
- "Terraform: Up & Running" by Yevgeniy Brikman
- "Infrastructure as Code" by Kief Morris

## AWS
- "AWS Certified Solutions Architect Study Guide" by Piper & Clinton
- "AWS Lambda in Action" by Danilo Poccia

## Kubernetes
- "Kubernetes: Up and Running" by Kelsey Hightower
- "Kubernetes Patterns" by Bilgin Ibryam & Roland Huß

## DevOps/SRE
- "The Phoenix Project" by Gene Kim, Kevin Behr, and George Spafford
- "Site Reliability Engineering: How Google Runs Production Systems" by Betsy Beyer et al.
END

cat > ~/DevOps/learning/courses/README.md << 'END'
# Courses for DevOps Learning

## Linux Foundation
- Essentials of Linux System Administration (LFS201)
- Linux Networking and Administration (LFS211)

## AWS
- Adrian Cantrill's AWS Certified Solutions Architect course
- A Cloud Guru's AWS courses

## Terraform
- HashiCorp Learn platform (all Terraform modules)
- Terraform Cloud Getting Started collection

## Kubernetes
- KodeKloud's Certified Kubernetes Administrator with Practice Tests
- KodeKloud's Certified Kubernetes Security Specialist
END

# Make script executable
chmod +x ~/DevOps/scripts/setup-resources.sh
EOF

# Run the setup script
chmod +x ~/DevOps/scripts/setup-resources.sh
~/DevOps/scripts/setup-resources.sh
```

## Environment Management Scripts

Create utility scripts to manage your learning environments:

```bash
# Create scripts directory
mkdir -p ~/DevOps/scripts

# VM management script
cat > ~/DevOps/scripts/vm-manage.sh << 'EOF'
#!/bin/bash

function start_ubuntu() {
  echo "Starting Ubuntu VM..."
  # Replace with actual UTM CLI command or applescript
  open -a "UTM" --args "Ubuntu"
}

function start_rocky() {
  echo "Starting Rocky Linux VM..."
  # Replace with actual UTM CLI command or applescript
  open -a "UTM" --args "Rocky"
}

function backup_vms() {
  echo "Backing up VM configurations..."
  # Add backup commands here
}

case "$1" in
  "ubuntu")
    start_ubuntu
    ;;
  "rocky")
    start_rocky
    ;;
  "backup")
    backup_vms
    ;;
  *)
    echo "Usage: $0 {ubuntu|rocky|backup}"
    exit 1
    ;;
esac
EOF

# AWS environment setup script
cat > ~/DevOps/scripts/aws-setup.sh << 'EOF'
#!/bin/bash

# Configure AWS profile
if [ -z "$1" ]; then
  echo "Usage: $0 <profile_name>"
  exit 1
fi

PROFILE=$1

# Setup AWS profile
aws configure --profile $PROFILE

# Verify configuration
aws sts get-caller-identity --profile $PROFILE

# Create S3 bucket for Terraform state (optional)
read -p "Create S3 bucket for Terraform state? (y/n): " CREATE_BUCKET
if [[ $CREATE_BUCKET == "y" ]]; then
  read -p "Enter bucket name: " BUCKET_NAME
  aws s3api create-bucket --bucket $BUCKET_NAME --profile $PROFILE
  
  # Enable versioning
  aws s3api put-bucket-versioning --bucket $BUCKET_NAME --versioning-configuration Status=Enabled --profile $PROFILE
  
  # Enable encryption
  aws s3api put-bucket-encryption --bucket $BUCKET_NAME --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}' --profile $PROFILE
  
  echo "S3 bucket $BUCKET_NAME created with versioning and encryption enabled."
fi
EOF

# Make scripts executable
chmod +x ~/DevOps/scripts/vm-manage.sh
chmod +x ~/DevOps/scripts/aws-setup.sh
```

## Tracking System Integration

Setup the learning progress tracking system as documented in your roadmap:

```bash
# Clone the tracking repository
cd ~/DevOps
git clone https://github.com/yourusername/devops-roadmap-tracker.git

# Navigate to the repository
cd devops-roadmap-tracker

# Initialize tracking system
bash init-tracker.sh

# Verify repository structure
ls -la
```

## Next Steps

After setting up your environment following this guide:

1. **Start with Linux VM**: Begin hands-on Linux system administration practice
2. **Initialize your tracking system**: Set up first week goals
3. **Acquire learning resources**: Download books and register for courses
4. **Schedule dedicated practice time**: Block time on your calendar 
5. **Join communities**: Connect with DevOps communities for support

By following this setup guide, you've created a comprehensive learning environment aligned with your DevOps/SRE career roadmap that leverages your Mac mini while providing essential Linux environments for hands-on practice.

---

*This guide was created specifically for Joshua Michael Hall's DevOps/SRE career development plan, with focus on creating a terminal-centric workflow environment leveraging both macOS and Linux systems.*
