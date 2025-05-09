# UTM Virtual Machine Setup Instructions

This document provides detailed instructions for setting up UTM virtual machines running Ubuntu Server and Rocky Linux on Apple Silicon (ARM64) Mac.

## Table of Contents
1. [Installing UTM](#installing-utm)
2. [Downloading Operating System ISOs](#downloading-operating-system-isos)
3. [Creating Ubuntu Server VM](#creating-ubuntu-server-vm)
4. [Installing Development Tools on Ubuntu](#installing-development-tools-on-ubuntu)
5. [Creating Rocky Linux VM](#creating-rocky-linux-vm)
6. [Installing Development Tools on Rocky Linux](#installing-development-tools-on-rocky-linux)
7. [Configuring File Sharing](#configuring-file-sharing)
8. [Setting Up Continuous File Syncing](#setting-up-continuous-file-syncing)
9. [Testing VM Connectivity](#testing-vm-connectivity)
10. [Troubleshooting](#troubleshooting)

## Installing UTM

### Method 1: Using Homebrew
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install UTM
brew install --cask utm
```

### Method 2: Manual Installation
```bash
# Download UTM
cd ~/Downloads
curl -L https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg -o UTM.dmg

# Mount the DMG file
hdiutil attach UTM.dmg

# Copy the application to Applications folder
cp -R /Volumes/UTM/UTM.app /Applications/

# Unmount the disk image
hdiutil detach /Volumes/UTM
```

## Downloading Operating System ISOs

### Download Ubuntu Server ARM64
```bash
cd ~/Downloads
curl -L https://cdimage.ubuntu.com/releases/22.04.3/release/ubuntu-22.04.3-live-server-arm64.iso -o ubuntu-server-arm64.iso
```

### Download Rocky Linux ARM64
```bash
cd ~/Downloads
curl -L https://download.rockylinux.org/pub/rocky/9/images/aarch64/Rocky-9.3-aarch64-minimal.iso -o rocky-linux-arm64.iso
```

## Creating Ubuntu Server VM

1. Open UTM
2. Click "+" and select "Virtualize"
3. Select "Linux"
4. Choose "Browse" and select your downloaded ubuntu-server-arm64.iso
5. Set recommended specs:
   - Memory: 4GB (4096MB)
   - CPU Cores: 2-4 (depending on your Mac's resources)
   - Storage: 40GB
6. Set name as "Ubuntu-Server-ARM64"
7. Click "Save" to create the VM
8. Start the VM and follow the Ubuntu Server installation wizard:
   - Choose language: English
   - Update to the new installer: Yes
   - Keyboard configuration: Default
   - Installation type: Ubuntu Server
   - Network connections: Use default
   - Configure proxy: Skip (unless required)
   - Configure Ubuntu archive mirror: Default
   - Guided storage configuration: Use default (entire disk)
   - Storage configuration: Accept default layout
   - Profile setup: Enter your name, server name, username, and password
   - SSH Setup: Install OpenSSH server
   - Featured server snaps: None (unless desired)
   - Wait for installation to complete and reboot

## Installing Development Tools on Ubuntu

After booting into your newly installed Ubuntu Server:

```bash
# Update the system
sudo apt update
sudo apt upgrade -y

# Install development essentials
sudo apt install -y build-essential git curl wget zip unzip 

# Install Docker
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Node.js and npm
sudo apt install -y nodejs npm

# Install SPICE Guest Tools for shared folders
sudo apt install -y spice-vdagent
```

## Creating Rocky Linux VM

1. Open UTM
2. Click "+" and select "Virtualize"
3. Select "Linux"
4. Choose "Browse" and select your downloaded rocky-linux-arm64.iso
5. Set recommended specs:
   - Memory: 4GB (4096MB)
   - CPU Cores: 2-4 (depending on your Mac's resources)
   - Storage: 40GB
6. Set name as "Rocky-Linux-ARM64"
7. Click "Save" to create the VM
8. Start the VM and follow the Rocky Linux installation wizard:
   - Select language
   - Set time zone
   - Configure installation destination (use entire disk)
   - Set root password
   - Create a user
   - Complete installation and reboot

## Installing Development Tools on Rocky Linux

After booting into your newly installed Rocky Linux:

```bash
# Update the system
sudo dnf update -y

# Install development essentials
sudo dnf groupinstall "Development Tools" -y
sudo dnf install -y git curl wget zip unzip

# Install Docker
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Python and pip
sudo dnf install -y python3 python3-pip

# Install Node.js and npm
sudo dnf install -y nodejs npm

# Install SPICE Guest Agent
sudo dnf install -y spice-vdagent
```

## Configuring File Sharing

### Ubuntu Server VM File Sharing

1. Set up shared folders in UTM:
   - Shutdown the VM
   - Select the VM in UTM
   - Click "Edit"
   - Go to "Shared Directory" tab
   - Click "Browse" and select the directory on your Mac you want to share
   - Click "Save"

2. Configure the shared folder in Ubuntu:
   ```bash
   # Create mount point if it doesn't exist
   mkdir -p ~/host_shared
   
   # Fix ownership (if needed)
   sudo chown -R $USER:$USER ~/host_shared
   
   # Mount shared folder
   sudo mount -t 9p -o trans=virtio share ~/host_shared
   
   # To make it permanent, add to /etc/fstab
   echo "share /home/$(whoami)/host_shared 9p trans=virtio 0 0" | sudo tee -a /etc/fstab
   ```

### Rocky Linux VM File Sharing

Since 9p modules aren't available in the minimal Rocky Linux ARM64 installation, we'll use SSH/rsync instead:

1. Ensure SSH is enabled:
   ```bash
   sudo systemctl enable --now sshd
   ```

2. Create a directory for shared files:
   ```bash
   mkdir -p ~/host_shared
   ```

3. Get the VM's IP address:
   ```bash
   ip addr show
   ```

## Setting Up Continuous File Syncing

### Mac to Ubuntu VM Continuous Sync

Create a script on your Mac:

```bash
#!/bin/bash

# Variables - Update with your actual values
UBUNTU_USER="your_username"
UBUNTU_IP="your_ubuntu_vm_ip"
LOCAL_DIR="$HOME/ubuntu_vm_files"
REMOTE_DIR="$HOME/host_shared"

# Create directories if they don't exist
mkdir -p "${LOCAL_DIR}"

# Initial sync from Ubuntu VM to Mac
echo "Initial sync from Ubuntu VM to Mac..."
rsync -avz --progress "${UBUNTU_USER}@${UBUNTU_IP}:${REMOTE_DIR}/" "${LOCAL_DIR}/"

# Watch for changes on Mac and sync to VM
echo "Starting continuous sync. Press Ctrl+C to stop."
fswatch -o "$LOCAL_DIR" | while read f; do
  echo "Change detected at $(date), syncing to Ubuntu VM..."
  rsync -avz --progress "${LOCAL_DIR}/" "${UBUNTU_USER}@${UBUNTU_IP}:${REMOTE_DIR}/"
done
```

### Mac to Rocky Linux VM Continuous Sync

Create a script on your Mac:

```bash
#!/bin/bash

# Variables - Update with your actual values
ROCKY_USER="your_username"
ROCKY_IP="your_rocky_vm_ip"
LOCAL_DIR="$HOME/rocky_vm_files"
REMOTE_DIR="$HOME/host_shared"

# Create directories if they don't exist
mkdir -p "${LOCAL_DIR}"

# Initial sync from Rocky VM to Mac
echo "Initial sync from Rocky VM to Mac..."
rsync -avz --progress "${ROCKY_USER}@${ROCKY_IP}:${REMOTE_DIR}/" "${LOCAL_DIR}/"

# Watch for changes on Mac and sync to VM
echo "Starting continuous sync. Press Ctrl+C to stop."
fswatch -o "$LOCAL_DIR" | while read f; do
  echo "Change detected at $(date), syncing to Rocky VM..."
  rsync -avz --progress "${LOCAL_DIR}/" "${ROCKY_USER}@${ROCKY_IP}:${REMOTE_DIR}/"
done
```

Make the scripts executable and run:

```bash
chmod +x ~/sync_ubuntu_continuous.sh
chmod +x ~/sync_rocky_continuous.sh

# Run the sync scripts in separate terminal windows
~/sync_ubuntu_continuous.sh
~/sync_rocky_continuous.sh
```

## Testing VM Connectivity

1. Ensure your VMs can access the internet:
   ```bash
   ping -c 4 google.com
   ```

2. Test communication between VMs:
   - Find the IP address of each VM:
   ```bash
   ip addr show
   ```
   - From one VM, ping the other:
   ```bash
   ping -c 4 [other-vm-ip-address]
   ```

3. Test SSH connectivity from your Mac:
   ```bash
   ssh username@vm-ip-address
   ```

4. Test file syncing:
   ```bash
   # Create a test file on your Mac
   echo "Test file from Mac" > ~/ubuntu_vm_files/test.txt
   
   # Check if it appears on Ubuntu VM
   ssh ubuntu_username@ubuntu_ip "cat ~/host_shared/test.txt"
   ```

## Troubleshooting

### File Sharing Permission Issues

If you encounter permission issues with shared folders:

```bash
# Fix ownership
sudo chown -R $USER:$USER ~/host_shared

# Fix permissions
chmod -R 755 ~/host_shared
```

### SSH Connectivity Issues

If you have SSH connectivity issues:

```bash
# Check SSH service status
sudo systemctl status sshd

# Enable and start SSH if needed
sudo systemctl enable --now sshd

# Check firewall status
sudo ufw status  # Ubuntu
sudo firewall-cmd --list-all  # Rocky Linux

# Allow SSH through firewall if needed
sudo ufw allow ssh  # Ubuntu
sudo firewall-cmd --permanent --add-service=ssh  # Rocky Linux
sudo firewall-cmd --reload  # Rocky Linux
```

### Setting Up SSH Key Authentication

To avoid entering passwords repeatedly:

```bash
# On your Mac, generate SSH key
ssh-keygen -t ed25519

# Copy to Ubuntu VM
ssh-copy-id username@ubuntu_vm_ip

# Copy to Rocky Linux VM
ssh-copy-id username@rocky_vm_ip
```

## Disclaimer

This document is in progress and provided as-is without warranty of any kind. These instructions may need to be adjusted based on specific versions of UTM and guest operating systems. Please report any issues or suggestions for improvement.

## Acknowledgements

This guide was developed with assistance from Anthropic's Claude AI assistant, which helped with:
- Documentation writing and organization
- Code structure suggestions
- Troubleshooting and debugging assistance

Claude was used as a development aid while all final implementation decisions and code review were performed by Joshua Michael Hall.
