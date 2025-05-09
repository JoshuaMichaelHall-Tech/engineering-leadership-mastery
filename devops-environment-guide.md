# DevOps/SRE Career Path: Updated Environment Setup Guide for Mid-Level First

This guide provides a streamlined setup for the development environment needed to accelerate your path to a mid-level DevOps/SRE position within 6-8 months, with a focus on financial services platform engineering.

## Table of Contents

1. [Environment Strategy Overview](#environment-strategy-overview)
2. [Hardware Configuration](#hardware-configuration)
3. [Base Operating System Setup](#base-operating-system-setup)
4. [Development Environments](#development-environments)
5. [Phase-Based Tool Installation](#phase-based-tool-installation)
6. [Project Environment Templates](#project-environment-templates)
7. [Job Search Environment](#job-search-environment)
8. [Environment Management Scripts](#environment-management-scripts)
9. [Performance Optimization](#performance-optimization)

## Environment Strategy Overview

This updated environment setup focuses on rapidly building job-ready skills for mid-level positions by:

1. **Optimizing for Portfolio Development**: Prioritizing environments that support building impressive, demonstrable projects
2. **Streamlining Certification Preparation**: Setting up dedicated environments for accelerated certification study
3. **Supporting Job Search Activities**: Configuring tools for tracking applications and interview preparation
4. **Minimizing Setup Time**: Automating environment setup to maximize productive learning time

## Hardware Configuration

Your current hardware (Mac Mini with Apple M4 chip and 16GB RAM with dual 4K monitors) is well-suited for this accelerated career path. To optimize it further:

1. **Memory Allocation Strategy**:
   - Allocate 8GB RAM for macOS and core development
   - Reserve 6GB RAM for VM/container environments
   - Keep 2GB RAM buffer for browser/research activities

2. **Storage Configuration**:
   - Dedicate 100GB for project repositories and learning materials
   - Reserve 50GB for VM environments
   - Allocate 20GB for Docker images and containers

3. **Display Setup**:
   - Primary display: Development workspace and coding
   - Secondary display: Documentation, research, and learning materials

## Base Operating System Setup

### Terminal-Centric macOS Configuration

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install essential CLI tools
brew install zsh tmux neovim git git-lfs jq yq httpie curl wget tree htop fzf ripgrep

# Install oh-my-zsh for enhanced terminal experience
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install neovim plugins manager
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# Install tmux plugin manager
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# Create optimized directory structure for career path
mkdir -p ~/DevOps/{projects,learning,certifications,job-search}
mkdir -p ~/DevOps/projects/{infrastructure-multi-env,containerized-microservices,security-automation}
mkdir -p ~/DevOps/certifications/{aws-saa,terraform,cka}
mkdir -p ~/DevOps/job-search/{applications,interview-prep,company-research}
```

### Environment Configuration Files

Create optimized configuration files for your terminal-centric workflow:

#### `.zshrc` for Enhanced Productivity
```bash
# Create enhanced .zshrc file
cat > ~/.zshrc << 'EOF'
# Path to oh-my-zsh installation
export ZSH="$HOME/.oh-my-zsh"

# Theme configuration
ZSH_THEME="robbyrussell"

# Useful plugins
plugins=(git aws docker kubectl terraform github vscode)

source $ZSH/oh-my-zsh.sh

# Environment variables
export PATH=$HOME/bin:/usr/local/bin:$PATH
export EDITOR='nvim'

# DevOps career path aliases
alias cdp="cd ~/DevOps/projects"
alias cdl="cd ~/DevOps/learning"
alias cdc="cd ~/DevOps/certifications"
alias cdj="cd ~/DevOps/job-search"

# AWS shortcuts
alias awswho="aws sts get-caller-identity"
alias awsls="aws s3 ls"

# Terraform shortcuts
alias tf="terraform"
alias tfi="terraform init"
alias tfp="terraform plan"
alias tfa="terraform apply"

# Docker shortcuts
alias dps="docker ps"
alias dimg="docker images"
alias dcp="docker-compose"

# Kubernetes shortcuts
alias k="kubectl"
alias kgp="kubectl get pods"
alias kgs="kubectl get services"
alias kgd="kubectl get deployments"

# Project navigation shortcuts
alias p1="cd ~/DevOps/projects/infrastructure-multi-env"
alias p2="cd ~/DevOps/projects/containerized-microservices"
alias p3="cd ~/DevOps/projects/security-automation"

# Study mode - clears screen and shows focus area
study() {
  clear
  echo "===================================="
  echo "FOCUSED STUDY MODE: $1"
  echo "===================================="
  echo "Time started: $(date)"
  echo "Target completion: $(date -v +1H)"
  echo "===================================="
}

# Job application tracker
jobapp() {
  echo "$(date),$1,$2,$3" >> ~/DevOps/job-search/applications/tracker.csv
  echo "Job application for $1 - $2 added to tracker"
}
EOF
```

#### `.tmux.conf` for Efficient Multi-tasking
```bash
# Create optimized tmux config
cat > ~/.tmux.conf << 'EOF'
# Improve colors
set -g default-terminal "screen-256color"

# Set prefix to Ctrl-Space
unbind C-b
set -g prefix C-Space
bind Space send-prefix

# Enable mouse mode
set -g mouse on

# Start window numbering at 1
set -g base-index 1
setw -g pane-base-index 1

# Renumber windows when a window is closed
set -g renumber-windows on

# Increase history limit
set -g history-limit 10000

# Split panes using | and -
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %

# Reload config file
bind r source-file ~/.tmux.conf \; display-message "Config reloaded!"

# DevOps workspace presets
bind d source-file ~/.tmux/dev.conf
bind s source-file ~/.tmux/study.conf
bind p source-file ~/.tmux/project.conf

# Set theme
set -g status-style bg=black,fg=white
set -g window-status-current-style bg=white,fg=black,bold

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# Initialize TMUX plugin manager
run '~/.tmux/plugins/tpm/tpm'
EOF
```

#### Neovim Configuration for Efficient Coding
```bash
# Create optimized neovim config
mkdir -p ~/.config/nvim
cat > ~/.config/nvim/init.vim << 'EOF'
" Plugins
call plug#begin('~/.local/share/nvim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'hashivim/vim-terraform'
Plug 'fatih/vim-go'
Plug 'pearofducks/ansible-vim'
Plug 'ekalinin/Dockerfile.vim'
Plug 'cespare/vim-toml'
Plug 'elzr/vim-json'
Plug 'stephpy/vim-yaml'
Plug 'martinda/Jenkinsfile-vim-syntax'
Plug 'rust-lang/rust.vim'
Plug 'vim-ruby/vim-ruby'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
call plug#end()

" Basic settings
syntax on
set number
set relativenumber
set cursorline
set expandtab
set tabstop=2
set shiftwidth=2
set softtabstop=2
set ignorecase
set smartcase
set incsearch
set hlsearch
set mouse=a
set clipboard=unnamed
set noswapfile
set autoread
set encoding=utf-8
set fileencoding=utf-8

" NERDTree settings
nnoremap <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1

" FZF settings
nnoremap <C-p> :Files<CR>

" DevOps file type specifics
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType json setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType tf setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType sh setlocal ts=2 sts=2 sw=2 expandtab

" Git integration shortcuts
nnoremap <leader>gs :Git<CR>
nnoremap <leader>ga :Git add %<CR>
nnoremap <leader>gc :Git commit<CR>
nnoremap <leader>gd :Git diff<CR>
nnoremap <leader>gl :Git log<CR>
nnoremap <leader>gp :Git push<CR>

" DevOps project navigation
command! P1 cd ~/DevOps/projects/infrastructure-multi-env
command! P2 cd ~/DevOps/projects/containerized-microservices
command! P3 cd ~/DevOps/projects/security-automation
EOF
```

## Development Environments

### 1. Virtual Machines Setup with UTM

```bash
# Install UTM
brew install --cask utm

# Create VM environments script
mkdir -p ~/DevOps/scripts
cat > ~/DevOps/scripts/setup-vms.sh << 'EOF'
#!/bin/bash

# Configuration
UBUNTU_URL="https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.3-live-server-arm64.iso"
ROCKY_URL="https://download.rockylinux.org/pub/rocky/9/images/aarch64/Rocky-9-latest-aarch64-minimal.iso"
VM_DIR="$HOME/Library/Containers/com.utmapp.UTM/Data/Documents"

# Download ISOs if not present
mkdir -p ~/Downloads/isos
[ ! -f ~/Downloads/isos/ubuntu-22.04-arm64.iso ] && curl -L $UBUNTU_URL -o ~/Downloads/isos/ubuntu-22.04-arm64.iso
[ ! -f ~/Downloads/isos/rocky-9-arm64.iso ] && curl -L $ROCKY_URL -o ~/Downloads/isos/rocky-9-arm64.iso

echo "ISOs downloaded. Please use UTM to create VMs with the following settings:"
echo ""
echo "1. Ubuntu Server VM - DevOps Environment"
echo "   - Name: devops-ubuntu"
echo "   - RAM: 4GB"
echo "   - CPU Cores: 4"
echo "   - Disk: 40GB"
echo "   - ISO: ~/Downloads/isos/ubuntu-22.04-arm64.iso"
echo "   - Shared Directory: ~/DevOps"
echo ""
echo "2. Rocky Linux VM - Financial Services Simulation"
echo "   - Name: finserv-rocky"
echo "   - RAM: 2GB"
echo "   - CPU Cores: 2"
echo "   - Disk: 20GB"
echo "   - ISO: ~/Downloads/isos/rocky-9-arm64.iso"
echo "   - Shared Directory: ~/DevOps"
echo ""
echo "After creating VMs, run the VM provisioning scripts."
EOF

# Create VM provisioning script for Ubuntu
cat > ~/DevOps/scripts/provision-ubuntu.sh << 'EOF'
#!/bin/bash

# Update and install essential packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl wget git vim tmux zsh htop jq unzip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Install Terraform
sudo apt install -y software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install -y terraform

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install k3d for local Kubernetes
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash

# Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Set up python environment
sudo apt install -y python3-pip python3-venv
python3 -m pip install --upgrade pip

# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
chsh -s $(which zsh)

echo "Ubuntu VM provisioned for DevOps work!"
EOF

# Create VM provisioning script for Rocky Linux
cat > ~/DevOps/scripts/provision-rocky.sh << 'EOF'
#!/bin/bash

# Update and install essential packages
sudo dnf update -y
sudo dnf install -y curl wget git vim tmux zsh util-linux-user

# Install Docker
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Install Terraform
sudo dnf install -y yum-utils
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo dnf install -y terraform

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Set up financial services simulation environment
mkdir -p ~/finance-simulation
git clone https://github.com/AWS-Samples/aws-financial-services-framework.git ~/finance-simulation/aws-fsf

# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
chsh -s $(which zsh)

echo "Rocky Linux VM provisioned for financial services simulation!"
EOF

chmod +x ~/DevOps/scripts/setup-vms.sh
chmod +x ~/DevOps/scripts/provision-ubuntu.sh
chmod +x ~/DevOps/scripts/provision-rocky.sh
```

### 2. Docker Development Environment

```bash
# Install Docker Desktop
brew install --cask docker

# Create Docker environment setup script
cat > ~/DevOps/scripts/setup-docker-env.sh << 'EOF'
#!/bin/bash

# Create project-specific Docker Compose configurations
mkdir -p ~/DevOps/projects/infrastructure-multi-env/docker
mkdir -p ~/DevOps/projects/containerized-microservices/docker
mkdir -p ~/DevOps/projects/security-automation/docker

# Create Docker Compose file for local development
cat > ~/DevOps/projects/containerized-microservices/docker/docker-compose.yml << 'EOFINNER'
version: '3.8'

services:
  # Application service
  app:
    build:
      context: ../app
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    volumes:
      - ../app:/app
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/appdb

  # Database service
  db:
    image: postgres:14
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=appdb

  # Redis service for caching
  redis:
    image: redis:6
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Prometheus for monitoring
  prometheus:
    image: prom/prometheus:v2.36.0
    ports:
      - "9090:9090"
    volumes:
      - ../monitoring/prometheus:/etc/prometheus
      - prometheus_data:/prometheus

  # Grafana for visualization
  grafana:
    image: grafana/grafana:9.0.0
    ports:
      - "3000:3000"
    volumes:
      - ../monitoring/grafana:/etc/grafana/provisioning
      - grafana_data:/var/lib/grafana

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
EOFINNER

# Create security tools Docker Compose file
cat > ~/DevOps/projects/security-automation/docker/docker-compose.yml << 'EOFINNER'
version: '3.8'

services:
  # OWASP ZAP for security scanning
  zap:
    image: owasp/zap2docker-stable
    ports:
      - "8080:8080"
      - "8090:8090"
    volumes:
      - ../security-scripts:/zap/scripts
    command: zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.disablekey=true

  # Vault for secrets management
  vault:
    image: hashicorp/vault
    ports:
      - "8200:8200"
    cap_add:
      - IPC_LOCK
    volumes:
      - ../vault/config:/vault/config
      - vault_data:/vault/data
    environment:
      - VAULT_ADDR=http://127.0.0.1:8200
    command: server -dev -dev-root-token-id=root

  # Trivy for container scanning
  trivy-server:
    image: aquasec/trivy:latest
    ports:
      - "8080:8080"
    volumes:
      - trivy_cache:/root/.cache
    command: server --listen 0.0.0.0:8080

volumes:
  vault_data:
  trivy_cache:
EOFINNER

# Create local AWS simulation environment
cat > ~/DevOps/projects/infrastructure-multi-env/docker/docker-compose.yml << 'EOFINNER'
version: '3.8'

services:
  # LocalStack for AWS simulation
  localstack:
    image: localstack/localstack:latest
    ports:
      - "4566:4566"
    environment:
      - SERVICES=s3,dynamodb,lambda,cloudformation,iam,apigateway,sts
      - DEBUG=1
      - DATA_DIR=/tmp/localstack/data
    volumes:
      - localstack_data:/tmp/localstack
      - "../aws:/tmp/aws"

volumes:
  localstack_data:
EOFINNER

echo "Docker development environments configured!"
EOF

chmod +x ~/DevOps/scripts/setup-docker-env.sh
```

### 3. Cloud Development Environments

```bash
# Create cloud environments setup script
cat > ~/DevOps/scripts/setup-cloud-env.sh << 'EOF'
#!/bin/bash

# Install AWS CLI
brew install awscli

# Install AWS CDK
npm install -g aws-cdk

# Install Terraform Cloud CLI
curl -LO https://github.com/hashicorp/terraform-cloud-cli/releases/download/v0.1.0/terraform-cloud-cli_0.1.0_darwin_amd64.zip
unzip terraform-cloud-cli_0.1.0_darwin_amd64.zip
chmod +x terraform-cloud
sudo mv terraform-cloud /usr/local/bin/

# Install Google Cloud SDK
brew install --cask google-cloud-sdk

# Create AWS config directory
mkdir -p ~/.aws

# Create AWS credential templates
cat > ~/.aws/credentials.template << 'EOFINNER'
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

[personal]
aws_access_key_id = YOUR_PERSONAL_ACCESS_KEY
aws_secret_access_key = YOUR_PERSONAL_SECRET_KEY

[work]
aws_access_key_id = YOUR_WORK_ACCESS_KEY
aws_secret_access_key = YOUR_WORK_SECRET_KEY
EOFINNER

# Create AWS config template
cat > ~/.aws/config.template << 'EOFINNER'
[default]
region = us-east-1
output = json

[profile personal]
region = us-east-1
output = json

[profile work]
region = us-east-2
output = json
EOFINNER

echo "Cloud development environment setup templates created!"
echo "Please customize ~/.aws/credentials.template and ~/.aws/config.template with your actual credentials and rename to remove the .template extension."
EOF

chmod +x ~/DevOps/scripts/setup-cloud-env.sh
```

## Phase-Based Tool Installation

### Phase 1: Foundation Building (Month 1-3)

```bash
# Create Phase 1 environment setup script
cat > ~/DevOps/scripts/setup-phase1.sh << 'EOF'
#!/bin/bash

# Install AWS SAA certification preparation tools
brew install --cask anki
mkdir -p ~/DevOps/certifications/aws-saa/practice-exams
mkdir -p ~/DevOps/certifications/aws-saa/study-notes
mkdir -p ~/DevOps/certifications/aws-saa/labs

# Install Terraform certification preparation tools
mkdir -p ~/DevOps/certifications/terraform/practice-questions
mkdir -p ~/DevOps/certifications/terraform/exercises
git clone https://github.com/terraform-aws-modules/terraform-aws-ec2-instance.git ~/DevOps/learning/terraform-aws-modules

# Create portfolio project skeletons
mkdir -p ~/DevOps/projects/infrastructure-multi-env/{terraform,docs,scripts,tests}
cat > ~/DevOps/projects/infrastructure-multi-env/README.md << 'EOFINNER'
# Infrastructure as Code for Multi-Environment Deployment

## Project Overview
This project demonstrates the implementation of infrastructure as code using Terraform to create secure, compliant, and repeatable infrastructure for dev, test, and production environments.

## Business Value
- **Cost Optimization**: Environment standardization reduces resource waste
- **Risk Reduction**: Security and compliance controls are built-in and consistent
- **Deployment Efficiency**: Time-to-deploy reduced from days to minutes

## Implementation Details
[To be completed as project develops]

## Skills Demonstrated
- Terraform module development
- AWS architecture design
- Security and compliance automation
- CI/CD for infrastructure
EOFINNER

# Set up Git repositories
cd ~/DevOps/projects/infrastructure-multi-env
git init
git add README.md
git commit -m "Initial commit: Project skeleton"

echo "Phase 1 environment setup complete!"
EOF

chmod +x ~/DevOps/scripts/setup-phase1.sh
```

### Phase 2: Advanced Skills (Month 4-6)

```bash
# Create Phase 2 environment setup script
cat > ~/DevOps/scripts/setup-phase2.sh << 'EOF'
#!/bin/bash

# Install Kubernetes tools
brew install kubernetes-cli kubectx kubernetes-helm k9s
brew install derailed/k9s/k9s

# Install CKA certification preparation tools
mkdir -p ~/DevOps/certifications/cka/practice-exams
mkdir -p ~/DevOps/certifications/cka/exercises
git clone https://github.com/cncf/kubernetes-community-days.git ~/DevOps/learning/kubernetes-community

# Set up Kind for local Kubernetes
brew install kind
mkdir -p ~/DevOps/projects/containerized-microservices/kubernetes
cat > ~/DevOps/projects/containerized-microservices/kubernetes/kind-config.yaml << 'EOFINNER'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 30000
    hostPort: 30000
  - containerPort: 30001
    hostPort: 30001
- role: worker
- role: worker
EOFINNER

# Create Kind cluster creation script
cat > ~/DevOps/projects/containerized-microservices/kubernetes/create-cluster.sh << 'EOFINNER'
#!/bin/bash
kind create cluster --name microservices --config kubernetes/kind-config.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
echo "Kubernetes cluster created and configured!"
EOFINNER
chmod +x ~/DevOps/projects/containerized-microservices/kubernetes/create-cluster.sh

echo "Phase 2 environment setup complete!"
EOF

chmod +x ~/DevOps/scripts/setup-phase2.sh
```

## Project Environment Templates

### Infrastructure Multi-Environment Project

```bash
# Create Infrastructure project template
mkdir -p ~/DevOps/templates/infrastructure-multi-env
cat > ~/DevOps/templates/infrastructure-multi-env/README.md << 'EOF'
# Infrastructure as Code for Multi-Environment Deployment

## Business Purpose
This project implements a secure, compliant infrastructure for financial services applications across development, testing, and production environments using Terraform and AWS.

## Technical Implementation
- Terraform modules for standard infrastructure components
- Environment separation with proper security boundaries
- Compliance controls for financial services regulations
- CI/CD pipeline for infrastructure deployment

## Directory Structure
```
infrastructure-multi-env/
├── docs/                 # Documentation and diagrams
├── environments/         # Environment-specific configurations
│   ├── dev/              # Development environment
│   ├── test/             # Testing environment
│   └── prod/             # Production environment
├── modules/              # Reusable Terraform modules
│   ├── network/          # VPC, subnets, security groups
│   ├── compute/          # EC2, ECS, Lambda
│   ├── database/         # RDS, DynamoDB
│   └── security/         # IAM, KMS, Security Hub
├── scripts/              # Utility scripts
├── tests/                # Infrastructure tests
└── .github/              # GitHub Actions workflows
```

## Key Features
- Multi-account architecture for security isolation
- Infrastructure testing with Terratest
- Security scanning with tfsec and checkov
- Compliance documentation generation

## Financial Services Considerations
- SOX compliance controls
- PCI-DSS security configurations
- Audit logging and monitoring
- Separation of duties implementation
EOF

# Create directory structure
mkdir -p ~/DevOps/templates/infrastructure-multi-env/{docs,environments/{dev,test,prod},modules/{network,compute,database,security},scripts,tests,.github/workflows}

# Create example module
cat > ~/DevOps/templates/infrastructure-multi-env/modules/network/vpc.tf << 'EOF'
variable "environment" {
  description = "Environment name (dev, test, prod)"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
    Terraform   = "true"
  }
}

resource "aws_subnet" "private" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 4, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name        = "${var.environment}-private-subnet-${count.index + 1}"
    Environment = var.environment
    Terraform   = "true"
    Tier        = "private"
  }
}

resource "aws_subnet" "public" {
  count                   = 3
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 4, count.index + 3)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name        = "${var.environment}-public-subnet-${count.index + 1}"
    Environment = var.environment
    Terraform   = "true"
    Tier        = "public"
  }
}

data "aws_availability_zones" "available" {}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}
EOF

# Create environment config
cat > ~/DevOps/templates/infrastructure-multi-env/environments/dev/main.tf << 'EOF'
provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket         = "terraform-state-dev"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

module "network" {
  source      = "../../modules/network"
  environment = "dev"
  vpc_cidr    = "10.0.0.0/16"
}

# Security group for financial application
resource "aws_security_group" "finance_app" {
  name        = "finance-app-sg"
  description = "Security group for financial application"
  vpc_id      = module.network.vpc_id

  # Example of PCI-DSS compliant rule - restrict inbound traffic
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS from anywhere"
  }

  # No direct SSH access from public internet
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]
    description = "SSH from internal network only"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound traffic"
  }

  tags = {
    Name        = "finance-app-sg"
    Environment = "dev"
    Compliance  = "PCI-DSS"
  }
}

# Implement auditing for compliance
resource "aws_cloudtrail" "compliance_trail" {
  name                          = "dev-compliance-trail"
  s3_bucket_name                = aws_s3_bucket.audit_logs.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true

  tags = {
    Name        = "dev-compliance-trail"
    Environment = "dev"
    Compliance  = "SOX,PCI-DSS"
  }
}

resource "aws_s3_bucket" "audit_logs" {
  bucket = "dev-audit-logs-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "dev-audit-logs"
    Environment = "dev"
    Compliance  = "SOX,PCI-DSS"
  }
}

data "aws_caller_identity" "current" {}
EOF
```

### Containerized Microservices Platform

```bash
# Create Containerized Microservices template
mkdir -p ~/DevOps/templates/containerized-microservices
cat > ~/DevOps/templates/containerized-microservices/README.md << 'EOF'
# Containerized Microservices Platform

## Business Purpose
This project demonstrates a production-ready containerized microservices platform for financial applications with security, observability, and scalability built-in.

## Technical Implementation
- Docker containers for application services
- Kubernetes for orchestration
- Monitoring and observability stack
- Security scanning and compliance

## Directory Structure
```
containerized-microservices/
├── docs/                 # Documentation and diagrams
├── services/             # Microservice applications
│   ├── api-gateway/      # API Gateway service
│   ├── user-service/     # User management service
│   ├── account-service/  # Account management service
│   └── transaction-service/ # Transaction processing service
├── kubernetes/           # Kubernetes manifests
│   ├── base/             # Base configurations
│   └── overlays/         # Environment-specific overlays
├── monitoring/           # Monitoring and observability
│   ├── prometheus/       # Prometheus configuration
│   └── grafana/          # Grafana dashboards
├── security/             # Security scanning and policies
└── scripts/              # Utility scripts
```

## Key Features
- Secure container configurations
- Horizontal scaling capabilities
- Comprehensive monitoring dashboards
- CI/CD pipeline with security scanning

## Financial Services Considerations
- Secure communication between services
- Audit logging for all transactions
- Encryption for sensitive data
- Compliance with financial regulations
EOF

# Create directory structure
mkdir -p ~/DevOps/templates/containerized-microservices/{docs,services/{api-gateway,user-service,account-service,transaction-service},kubernetes/{base,overlays/{dev,test,prod}},monitoring/{prometheus,grafana},security,scripts}

# Create example Dockerfile
cat > ~/DevOps/templates/containerized-microservices/services/api-gateway/Dockerfile << 'EOF'
# Use minimal base image for security
FROM node:18-alpine AS build

# Create app directory
WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy app source
COPY . .

# Build app
RUN npm run build

# Production image
FROM node:18-alpine

# Run as non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set working directory
WORKDIR /usr/src/app

# Copy from build stage
COPY --from=build --chown=appuser:appgroup /usr/src/app/node_modules ./node_modules
COPY --from=build --chown=appuser:appgroup /usr/src/app/dist ./dist
COPY --from=build --chown=appuser:appgroup /usr/src/app/package.json ./

# Expose API port
EXPOSE 8080

# Set NODE_ENV
ENV NODE_ENV=production

# Start app
CMD ["node", "dist/main"]
EOF

# Create example Kubernetes manifest
cat > ~/DevOps/templates/containerized-microservices/kubernetes/base/api-gateway.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
  labels:
    app: api-gateway
    component: gateway
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api-gateway
  template:
    metadata:
      labels:
        app: api-gateway
        component: gateway
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: api-gateway
        image: api-gateway:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
          name: http
        resources:
          limits:
            cpu: 500m
            memory: 512Mi
          requests:
            cpu: 100m
            memory: 128Mi
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 20
        securityContext:
          allowPrivilegeEscalation: false
          runAsNonRoot: true
          capabilities:
            drop:
            - ALL
        env:
        - name: NODE_ENV
          value: "production"
        - name: LOG_LEVEL
          value: "info"
---
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
  labels:
    app: api-gateway
    component: gateway
spec:
  selector:
    app: api-gateway
  ports:
  - port: 80
    targetPort: 8080
    name: http
  type: ClusterIP
EOF

# Create example monitoring configuration
cat > ~/DevOps/templates/containerized-microservices/monitoring/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - alertmanager:9093

rule_files:
  - "rules/*.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
    - targets: ['localhost:9090']

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
    - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: $1:$2
      target_label: __address__
    - action: labelmap
      regex: __meta_kubernetes_pod_label_(.+)
    - source_labels: [__meta_kubernetes_namespace]
      action: replace
      target_label: kubernetes_namespace
    - source_labels: [__meta_kubernetes_pod_name]
      action: replace
      target_label: kubernetes_pod_name
EOF
```

### Security Automation Suite

```bash
# Create Security Automation Suite template
mkdir -p ~/DevOps/templates/security-automation
cat > ~/DevOps/templates/security-automation/README.md << 'EOF'
# Security Automation Suite for Financial Services

## Business Purpose
This project implements an automated security and compliance toolchain for financial services environments, ensuring continuous compliance monitoring and security validation.

## Technical Implementation
- Infrastructure security scanning
- Container image vulnerability scanning
- Compliance reporting automation
- Secrets management workflow

## Directory Structure
```
security-automation/
├── docs/                 # Documentation and diagrams
├── scanners/             # Security scanning tools
│   ├── infrastructure/   # Infrastructure scanning
│   ├── container/        # Container scanning
│   └── code/             # Code scanning
├── compliance/           # Compliance automation
│   ├── policies/         # Policy definitions
│   ├── reports/          # Report templates
│   └── validators/       # Validation scripts
├── secrets/              # Secrets management
│   ├── vault/            # HashiCorp Vault configuration
│   └── aws-secrets/      # AWS Secrets Manager integration
├── ci-cd/                # CI/CD integration
└── scripts/              # Utility scripts
```

## Key Features
- Automated security scanning in CI/CD
- Compliance reporting for SOX, PCI-DSS, GDPR
- Secret rotation and management
- Drift detection and alerting

## Financial Services Value
- Reduced audit preparation time from weeks to hours
- Continuous compliance validation
- Proactive security risk identification
- Automatic regulatory evidence generation
EOF

# Create directory structure
mkdir -p ~/DevOps/templates/security-automation/{docs,scanners/{infrastructure,container,code},compliance/{policies,reports,validators},secrets/{vault,aws-secrets},ci-cd,scripts}

# Create example infrastructure scanning configuration
cat > ~/DevOps/templates/security-automation/scanners/infrastructure/tfsec-config.json << 'EOF'
{
  "exclude": [
    "AWS018"
  ],
  "severity_overrides": {
    "AWS017": "HIGH"
  },
  "minimum_severity": "MEDIUM",
  "include_passed": true,
  "include_skipped": false
}
EOF

# Create example compliance policy
cat > ~/DevOps/templates/security-automation/compliance/policies/pci-dss.yml << 'EOF'
policies:
  - name: PCI-DSS-Requirement-1
    description: "Install and maintain a firewall configuration to protect cardholder data"
    controls:
      - id: PCI-DSS-1.1
        description: "Establish and implement firewall and router configuration standards"
        validation_script: "validators/network/firewall_validation.py"
        severity: "HIGH"
        
      - id: PCI-DSS-1.2
        description: "Build firewall and router configurations that restrict connections"
        validation_script: "validators/network/connection_validation.py"
        severity: "HIGH"
        
      - id: PCI-DSS-1.3
        description: "Prohibit direct public access to cardholder data"
        validation_script: "validators/network/public_access_validation.py"
        severity: "CRITICAL"

  - name: PCI-DSS-Requirement-2
    description: "Do not use vendor-supplied defaults for system passwords and other security parameters"
    controls:
      - id: PCI-DSS-2.1
        description: "Change vendor defaults before installing system on the network"
        validation_script: "validators/system/default_credentials_validation.py"
        severity: "CRITICAL"
        
      - id: PCI-DSS-2.2
        description: "Develop configuration standards for all system components"
        validation_script: "validators/system/configuration_standard_validation.py"
        severity: "HIGH"
EOF

# Create example secrets management configuration
cat > ~/DevOps/templates/security-automation/secrets/vault/vault-policy.hcl << 'EOF'
# Allow management of policies
path "sys/policies/acl/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Allow management of secrets engines
path "sys/mounts/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Manage FinServ secrets
path "finserv/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Manage AWS dynamic credentials
path "aws/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
EOF

# Create example CI/CD security integration
cat > ~/DevOps/templates/security-automation/ci-cd/github-workflow.yml << 'EOF'
name: Security Scan

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      # Infrastructure scanning
      - name: tfsec
        uses: tfsec/tfsec-sarif-action@master
        with:
          sarif_file: tfsec.sarif
          
      # Container scanning          
      - name: Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'app:latest'
          format: 'sarif'
          output: 'trivy-results.sarif'
          
      # Secrets scanning
      - name: GitGuardian scan
        uses: GitGuardian/gg-shield-action@master
        env:
          GITHUB_PUSH_BEFORE_SHA: ${{ github.event.before }}
          GITHUB_PUSH_BASE_SHA: ${{ github.event.base }}
          GITHUB_PULL_BASE_SHA: ${{ github.event.pull_request.base.sha }}
          GITHUB_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}

      # Compliance validation
      - name: Run compliance checks
        run: |
          python3 ./compliance/validators/run_all.py
          
      # Upload results
      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: tfsec.sarif

      - name: Upload Trivy SARIF file
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: trivy-results.sarif
EOF
```

## Job Search Environment

```bash
# Create job search environment setup
cat > ~/DevOps/scripts/setup-job-search-env.sh << 'EOF'
#!/bin/bash

# Create job search directory structure
mkdir -p ~/DevOps/job-search/{applications,interview-prep/{technical,behavioral},company-research,resume-versions,offer-analysis}

# Create job application tracker
cat > ~/DevOps/job-search/applications/tracker.csv << 'EOFINNER'
Date,Company,Position,Source,URL,Resume_Version,Status,Next_Action,Contact,Notes
EOFINNER

# Create company research template
cat > ~/DevOps/job-search/company-research/template.md << 'EOFINNER'
# [Company Name] Research

## Company Overview
- **Industry**: [e.g., FinTech, Banking]
- **Size**: [e.g., Startup, Mid-size, Enterprise]
- **Location**: [Headquarters and offices]
- **Founded**: [Year]
- **Public/Private**: [Status]

## Technology Stack
- **Cloud Provider**: [AWS, GCP, Azure, Multi-cloud]
- **Infrastructure**: [Kubernetes, Terraform, etc.]
- **Languages**: [Primary programming languages]
- **Tools**: [CI/CD, monitoring, etc.]

## DevOps/Platform Team
- **Team Size**: [If known]
- **Reporting Structure**: [If known]
- **Key Projects**: [Notable technical projects]

## Financial Services Aspects
- **Regulations**: [SOX, PCI-DSS, etc.]
- **Security Requirements**: [Any specific security needs]
- **Compliance Focus**: [Areas of compliance focus]

## Job Details
- **Position**: [Exact title]
- **Requirements**: [Key skills required]
- **Responsibilities**: [Main duties]
- **Salary Range**: [If available]

## Interview Process
- **Stages**: [Phone screen, technical interview, etc.]
- **Technical Assessment**: [Type of assessment]
- **Key Interviewers**: [Names and roles if known]

## Questions to Ask
- [Prepared questions about the role]
- [Prepared questions about the team]
- [Prepared questions about the company]

## Why I'm a Good Fit
- [Matching skills]
- [Relevant experience]
- [Culture fit aspects]

## Networking Contacts
- [Name], [Position] - [How connected]
- [Name], [Position] - [How connected]
EOFINNER

# Create technical interview preparation guide
cat > ~/DevOps/job-search/interview-prep/technical/devops-interview-guide.md << 'EOFINNER'
# DevOps Technical Interview Preparation

## Core Technical Areas

### Infrastructure as Code
- **Key Concepts**: Terraform state management, module design, versioning
- **Sample Questions**:
  - How would you structure Terraform modules for multi-environment deployments?
  - Explain the difference between Terraform state locking and state versioning?
  - How would you handle secrets in your IaC implementation?
- **Project Examples**: Highlight infrastructure-multi-env project

### Containerization & Kubernetes
- **Key Concepts**: Docker security, Kubernetes RBAC, service networking
- **Sample Questions**:
  - Explain Kubernetes pod security contexts and why they're important
  - How would you design a secure multi-tenant Kubernetes cluster?
  - Walk through your approach to container image security scanning
- **Project Examples**: Highlight containerized-microservices project

### CI/CD Pipelines
- **Key Concepts**: Pipeline as code, security integration, deployment strategies
- **Sample Questions**:
  - How would you implement security scanning in a CI/CD pipeline?
  - Explain the difference between blue/green and canary deployments
  - How would you ensure pipeline reproducibility?
- **Project Examples**: Highlight CI/CD aspects of all projects

### Cloud Architecture
- **Key Concepts**: AWS services, networking, security, cost optimization
- **Sample Questions**:
  - Describe a highly available architecture you've designed
  - How would you implement least privilege in AWS?
  - Explain how you would set up network segmentation in a VPC
- **Project Examples**: AWS architecture from infrastructure project

### Monitoring & Observability
- **Key Concepts**: Metrics, logging, tracing, alerts
- **Sample Questions**:
  - How would you approach monitoring for a microservices architecture?
  - Explain the difference between metrics, logs, and traces
  - How would you implement meaningful alerts that avoid alert fatigue?
- **Project Examples**: Monitoring stack in containerized project

### Financial Services Compliance
- **Key Concepts**: SOX, PCI-DSS, audit trails, security controls
- **Sample Questions**:
  - How would you implement compliance as code?
  - Explain how you would set up audit logging for a financial application
  - How would you approach automating evidence collection for audits?
- **Project Examples**: Compliance aspects of security automation project

## Behavioral Scenarios

### Problem Solving
- **Scenario**: "Tell me about a challenging infrastructure problem you solved"
- **Structure**:
  - Problem: Clearly define the problem
  - Approach: Explain your thought process
  - Solution: Detail the implementation
  - Result: Quantify the impact
- **Example**: Infrastructure automation reducing deployment time

### Collaboration
- **Scenario**: "Describe a time when you had to work closely with development teams"
- **Structure**:
  - Situation: Set the context
  - Tasks: Your responsibilities
  - Actions: How you collaborated
  - Results: Outcome of the collaboration
- **Example**: Implementing developer self-service platform

### Technical Leadership
- **Scenario**: "Tell me about a time you introduced a new technology or practice"
- **Structure**:
  - Challenge: Why change was needed
  - Choice: How you selected the solution
  - Implementation: How you led the adoption
  - Impact: Business value delivered
- **Example**: Implementing infrastructure as code

## System Design Exercise Preparation

### Approach Framework
1. **Requirements Clarification**: Ask questions to understand the problem
2. **High-Level Design**: Start with a simple architecture diagram
3. **Deep Dive**: Focus on key components relevant to DevOps
4. **Scaling & Security**: Address how the system scales and stays secure
5. **Monitoring & Operations**: Explain how the system would be monitored and operated

### Practice Scenarios
- Design a CI/CD pipeline for a financial services application
- Design a multi-environment Kubernetes platform for a bank
- Design a monitoring solution for a payment processing system

## Technical Demo Preparation

- Create 5-minute demos of each portfolio project
- Practice explaining architecture decisions
- Prepare to show code snippets and diagrams
- Focus on business value and technical challenges overcome
EOFINNER

# Create resume template for mid-level position
cat > ~/DevOps/job-search/resume-versions/mid-level-devops-template.md << 'EOFINNER'
# [Your Name]
## Mid-Level DevOps Engineer | Financial Services Platform Specialist

[Your Location] | [Your Email] | [Your Phone] | [LinkedIn URL] | [GitHub URL]

## Professional Summary
DevOps engineer with expertise in infrastructure automation, container orchestration, and compliance implementation for financial services environments. Focused on building secure, scalable, and compliant cloud infrastructure using Terraform, AWS, and Kubernetes.

## Technical Skills
- **Infrastructure as Code**: Terraform, AWS CloudFormation
- **Cloud Platforms**: AWS (Certified Solutions Architect Associate)
- **Containerization**: Docker, Kubernetes (Certified Kubernetes Administrator)
- **CI/CD**: GitHub Actions, Jenkins
- **Monitoring**: Prometheus, Grafana, ELK Stack
- **Security & Compliance**: Infrastructure scanning, compliance automation, SOX/PCI-DSS
- **Programming**: Ruby, Python, Bash

## Projects
### Infrastructure as Code for Multi-Environment Deployment
- Designed and implemented Terraform modules for secure, compliant AWS infrastructure
- Created reusable components for network, compute, and security following financial services best practices
- Implemented multi-environment deployment with proper separation and security controls
- **Technologies**: Terraform, AWS, GitHub Actions, tfsec
- **Link**: [GitHub Repository URL]

### Containerized Microservices Platform
- Developed containerized microservices platform with Kubernetes orchestration
- Implemented monitoring stack with Prometheus and Grafana for full observability
- Created CI/CD pipeline with security scanning integration
- **Technologies**: Docker, Kubernetes, Prometheus, Grafana
- **Link**: [GitHub Repository URL]

### Security Automation Suite
- Built automated security scanning and compliance reporting tools
- Implemented integration with CI/CD pipelines for continuous security validation
- Created compliance evidence generation for financial services regulations
- **Technologies**: Trivy, tfsec, AWS Security Hub, HashiCorp Vault
- **Link**: [GitHub Repository URL]

## Certifications
- AWS Certified Solutions Architect - Associate
- HashiCorp Certified: Terraform Associate
- Certified Kubernetes Administrator (CKA)

## Education
**Bachelor of Science in Computer Science**
[Your University] - Graduated [Year]

## Professional Development
- Completed Linux Foundation's "DevOps and SRE Fundamentals" course
- Active participant in AWS and Kubernetes community events
- Regular contributor to DevOps and financial technology forums
EOFINNER

echo "Job search environment setup complete!"
chmod +x ~/DevOps/scripts/setup-job-search-env.sh
```

## Environment Management Scripts

```bash
# Create the main environment manager script
cat > ~/DevOps/scripts/environment-manager.sh << 'EOF'
#!/bin/bash

function show_help() {
  echo "DevOps Career Path Environment Manager"
  echo ""
  echo "Usage: $0 [command]"
  echo ""
  echo "Commands:"
  echo "  setup-all             Setup all environments"
  echo "  setup-base            Setup base macOS environment"
  echo "  setup-vms             Setup virtual machines"
  echo "  setup-docker          Setup Docker environments"
  echo "  setup-cloud           Setup cloud development environments"
  echo "  setup-phase1          Setup Phase 1 learning environment"
  echo "  setup-phase2          Setup Phase 2 learning environment"
  echo "  setup-job-search      Setup job search environment"
  echo "  start-vm [name]       Start a specific VM (devops-ubuntu or finserv-rocky)"
  echo "  start-project [num]   Start environment for project (1, 2, or 3)"
  echo "  start-study [cert]    Start study environment (aws-saa, terraform, or cka)"
  echo "  update-all            Update all environments"
  echo "  backup                Backup all environments"
  echo ""
  echo "Examples:"
  echo "  $0 setup-all          # Setup everything"
  echo "  $0 start-project 1    # Start Project 1 environment"
  echo "  $0 start-study aws-saa # Start AWS SAA study environment"
}

function setup_all() {
  bash ~/DevOps/scripts/setup-base.sh
  bash ~/DevOps/scripts/setup-vms.sh
  bash ~/DevOps/scripts/setup-docker-env.sh
  bash ~/DevOps/scripts/setup-cloud-env.sh
  bash ~/DevOps/scripts/setup-phase1.sh
  bash ~/DevOps/scripts/setup-phase2.sh
  bash ~/DevOps/scripts/setup-job-search-env.sh
  echo "All environments set up successfully!"
}

function start_vm() {
  if [ "$1" == "devops-ubuntu" ]; then
    open -a UTM --args devops-ubuntu
    echo "DevOps Ubuntu VM started"
  elif [ "$1" == "finserv-rocky" ]; then
    open -a UTM --args finserv-rocky
    echo "Financial Services Rocky Linux VM started"
  else
    echo "Unknown VM name. Use 'devops-ubuntu' or 'finserv-rocky'"
    exit 1
  fi
}

function start_project() {
  if [ "$1" == "1" ]; then
    cd ~/DevOps/projects/infrastructure-multi-env
    tmux new-session -s project1 -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/projects/infrastructure-multi-env' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/projects/infrastructure-multi-env/terraform' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/projects/infrastructure-multi-env' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "Project 1: Infrastructure as Code for Multi-Environment Deployment"' C-m
    tmux attach-session -t project1
  elif [ "$1" == "2" ]; then
    cd ~/DevOps/projects/containerized-microservices
    tmux new-session -s project2 -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/projects/containerized-microservices' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/projects/containerized-microservices/kubernetes' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/projects/containerized-microservices' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "Project 2: Containerized Microservices Platform"' C-m
    tmux attach-session -t project2
  elif [ "$1" == "3" ]; then
    cd ~/DevOps/projects/security-automation
    tmux new-session -s project3 -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/projects/security-automation' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/projects/security-automation/compliance' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/projects/security-automation' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "Project 3: Security Automation Suite"' C-m
    tmux attach-session -t project3
  else
    echo "Unknown project number. Use 1, 2, or 3"
    exit 1
  fi
}

function start_study() {
  if [ "$1" == "aws-saa" ]; then
    cd ~/DevOps/certifications/aws-saa
    tmux new-session -s aws-study -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/certifications/aws-saa/practice-exams' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/certifications/aws-saa/labs' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/certifications/aws-saa' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "AWS Certified Solutions Architect Associate Study Environment"' C-m
    tmux attach-session -t aws-study
  elif [ "$1" == "terraform" ]; then
    cd ~/DevOps/certifications/terraform
    tmux new-session -s terraform-study -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/certifications/terraform/practice-questions' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/certifications/terraform/exercises' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/certifications/terraform' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "HashiCorp Certified: Terraform Associate Study Environment"' C-m
    tmux attach-session -t terraform-study
  elif [ "$1" == "cka" ]; then
    cd ~/DevOps/certifications/cka
    tmux new-session -s cka-study -d
    tmux split-window -h
    tmux send-keys 'cd ~/DevOps/certifications/cka/practice-exams' C-m
    tmux send-keys 'clear' C-m
    tmux split-window -v
    tmux send-keys 'cd ~/DevOps/certifications/cka/exercises' C-m
    tmux send-keys 'clear' C-m
    tmux select-pane -t 0
    tmux send-keys 'cd ~/DevOps/certifications/cka' C-m
    tmux send-keys 'clear' C-m
    tmux send-keys 'echo "Certified Kubernetes Administrator Study Environment"' C-m
    tmux attach-session -t cka-study
  else
    echo "Unknown certification. Use aws-saa, terraform, or cka"
    exit 1
  fi
}

function backup_environments() {
  # Create backup directory
  BACKUP_DIR=~/DevOps/backups/$(date +"%Y-%m-%d")
  mkdir -p $BACKUP_DIR

  # Backup project directories
  tar -czf $BACKUP_DIR/projects.tar.gz -C ~/DevOps projects

  # Backup certification materials
  tar -czf $BACKUP_DIR/certifications.tar.gz -C ~/DevOps certifications

  # Backup job search materials
  tar -czf $BACKUP_DIR/job-search.tar.gz -C ~/DevOps job-search

  # Backup scripts
  tar -czf $BACKUP_DIR/scripts.tar.gz -C ~/DevOps scripts

  # Backup configuration files
  mkdir -p $BACKUP_DIR/configs
  cp ~/.zshrc $BACKUP_DIR/configs/
  cp ~/.tmux.conf $BACKUP_DIR/configs/
  cp -r ~/.config/nvim $BACKUP_DIR/configs/

  echo "Environment backup completed to $BACKUP_DIR"
}

# Main command processing
case "$1" in
  setup-all)
    setup_all
    ;;
  setup-base)
    bash ~/DevOps/scripts/setup-base.sh
    ;;
  setup-vms)
    bash ~/DevOps/scripts/setup-vms.sh
    ;;
  setup-docker)
    bash ~/DevOps/scripts/setup-docker-env.sh
    ;;
  setup-cloud)
    bash ~/DevOps/scripts/setup-cloud-env.sh
    ;;
  setup-phase1)
    bash ~/DevOps/scripts/setup-phase1.sh
    ;;
  setup-phase2)
    bash ~/DevOps/scripts/setup-phase2.sh
    ;;
  setup-job-search)
    bash ~/DevOps/scripts/setup-job-search-env.sh
    ;;
  start-vm)
    start_vm "$2"
    ;;
  start-project)
    start_project "$2"
    ;;
  start-study)
    start_study "$2"
    ;;
  backup)
    backup_environments
    ;;
  *)
    show_help
    ;;
esac
EOF

chmod +x ~/DevOps/scripts/environment-manager.sh
```

## Performance Optimization

To ensure optimal performance for your accelerated learning path, implement these system optimizations:

```bash
# Create performance optimization script
cat > ~/DevOps/scripts/optimize-performance.sh << 'EOF'
#!/bin/bash

# Show current performance metrics
echo "Current system performance status:"
echo "--------------------------------"
top -l 1 | head -n 10
echo "--------------------------------"
vm_stat
echo "--------------------------------"

# Optimize macOS performance
echo "Optimizing macOS performance..."

# Disable unnecessary animations
defaults write com.apple.dock expose-animation-duration -float 0.1
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.5
defaults write NSGlobalDomain NSWindowResizeTime -float 0.001

# Disable automatic termination of inactive apps
defaults write NSGlobalDomain NSDisableAutomaticTermination -bool true

# Speed up Mission Control animations
defaults write com.apple.dock expose-animation-duration -float 0.1

# Disable Dashboard
defaults write com.apple.dashboard mcx-disabled -bool true

# Don't automatically rearrange Spaces
defaults write com.apple.dock mru-spaces -bool false

# Restart affected services
killall Dock

# Optimize Safari (if used for documentation)
defaults write com.apple.Safari WebKitDeveloperExtrasEnabledPreferenceKey -bool true
defaults write com.apple.Safari WebKitDeveloperExtrasEnabled -bool true
defaults write com.apple.Safari IncludeDevelopMenu -bool true

# Docker performance optimization
echo "Optimizing Docker performance..."
cat > ~/Library/Group\ Containers/group.com.docker/settings.json << 'EOFINNER'
{
  "cpus" : 4,
  "memoryMiB" : 6144,
  "swapMiB" : 1024,
  "diskSizeMiB" : 61440,
  "filesharingDirectories" : [
    "/Users/$(whoami)/DevOps"
  ],
  "useCredentialHelper" : true,
  "useNightlyBuild" : false,
  "useGrpcfuse" : true,
  "enableBuildkit" : true
}
EOFINNER

# Create tmux performance profile
cat > ~/.tmux/performance.conf << 'EOFINNER'
# Performance mode - minimal UI
set -g status-interval 5
set -g status-left ""
set -g status-right "#[fg=green]#(top -l 1 | grep 'CPU usage' | awk '{print $3}')#[default] | #[fg=cyan]#(sysctl -n vm.loadavg | cut -d' ' -f2)#[default] | #[fg=yellow]#(memory_pressure | grep 'System-wide memory free percentage' | awk '{print $NF}')#[default]"
set -g window-status-format "#I:#W"
set -g window-status-current-format "#I:#W"
EOFINNER

# Create Neovim performance config
mkdir -p ~/.config/nvim/performance
cat > ~/.config/nvim/performance/init.vim << 'EOFINNER'
" Minimal Neovim config for performance
set noswapfile
set nobackup
set noundofile
set lazyredraw
set nocursorline
set nocursorcolumn
set norelativenumber
set signcolumn=no
set synmaxcol=200
set updatetime=300
syntax on
set syntax=on
set background=dark
colorscheme desert
EOFINNER

# Create performance mode alias
echo "# Performance mode alias" >> ~/.zshrc
echo "alias performance='tmux source-file ~/.tmux/performance.conf && export NVIM_CONFIG=~/.config/nvim/performance/init.vim && echo \"Performance mode activated\"'" >> ~/.zshrc

echo "Performance optimizations complete! Use 'performance' command to activate high-performance mode."
EOF

chmod +x ~/DevOps/scripts/optimize-performance.sh
```

## Next Steps After Setup

With your environment configured, follow these steps to begin your accelerated mid-level career path:

1. **Run the full environment setup**:
   ```bash
   cd ~/DevOps/scripts
   ./environment-manager.sh setup-all
   ```

2. **Start Project 1 environment**:
   ```bash
   ./environment-manager.sh start-project 1
   ```

3. **Begin AWS certification study**:
   ```bash
   ./environment-manager.sh start-study aws-saa
   ```

4. **Set up job search tracking**:
   ```bash
   ./environment-manager.sh setup-job-search
   ```

5. **Optimize system performance**:
   ```bash
   ./optimize-performance.sh
   ```

This updated environment setup is specifically designed to support your accelerated path to a mid-level DevOps position in financial services. The environment focuses on:

1. **Efficient learning**: Structured environments for each certification
2. **Portfolio building**: Templates and environments for impressive projects
3. **Job search support**: Tools for tracking applications and interview preparation
4. **Performance optimization**: Configurations to maximize productivity

By following this setup, you'll create a development environment optimized for rapidly building the skills, certifications, and portfolio projects needed to secure a mid-level DevOps position within 6-8 months.