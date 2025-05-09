# UTM Virtual Machine User Manual

This manual provides comprehensive instructions for using the Ubuntu Server and Rocky Linux virtual machines that have been set up in UTM on your Apple Silicon Mac.

## Table of Contents

1. [Introduction](#introduction)
2. [Starting and Stopping VMs](#starting-and-stopping-vms)
3. [Accessing the VMs](#accessing-the-vms)
4. [File Sharing Between Mac and VMs](#file-sharing-between-mac-and-vms)
5. [Development Workflow](#development-workflow)
6. [Managing VM Resources](#managing-vm-resources)
7. [Backing Up VMs](#backing-up-vms)
8. [Common Tasks](#common-tasks)
9. [Troubleshooting](#troubleshooting)

## Introduction

You have set up two virtual machines running on UTM:

1. **Ubuntu Server ARM64**: A server distribution of Ubuntu optimized for ARM architecture.
2. **Rocky Linux ARM64**: A CentOS/RHEL-compatible Linux distribution optimized for ARM architecture.

These VMs are configured with:
- 4GB RAM each
- 2-4 CPU cores each
- 40GB storage each
- Development tools (Docker, Python, Node.js, etc.)
- File sharing capabilities

## Starting and Stopping VMs

### Starting a VM

1. Open the UTM app
2. Select the VM you want to start
3. Click the "Play" button
4. Wait for the boot process to complete
5. Log in with your username and password

### Properly Stopping a VM

1. From within the VM, run:
   ```bash
   sudo shutdown -h now
   ```
   Or
   ```bash
   sudo poweroff
   ```

2. Wait for the VM to power off completely
3. The UTM window will indicate when the VM is stopped

### Force Stopping (Use only when necessary)

1. In UTM, click the "Stop" button (square icon)
2. If prompted, choose "Force Stop" only if the VM is unresponsive

## Accessing the VMs

### Console Access

1. Start the VM in UTM
2. The console window will open automatically
3. Log in with your username and password

### SSH Access

#### From your Mac Terminal:

```bash
# For Ubuntu VM
ssh your_username@ubuntu_vm_ip

# For Rocky Linux VM
ssh your_username@rocky_vm_ip
```

Replace `your_username` and `vm_ip` with your actual username and VM IP address.

### Finding VM IP Addresses

From within the VM:
```bash
ip addr show
```

Look for the IPv4 address on the main network interface (typically `enp0s1` or similar).

## File Sharing Between Mac and VMs

### Ubuntu VM File Sharing

The shared folder is mounted at `~/host_shared` within your Ubuntu VM.

Files placed in this directory are accessible from both your Mac and the VM. The 9p filesystem is used for sharing.

### Rocky Linux VM File Sharing

Since 9p isn't available on the Rocky Linux VM, we use rsync for file sharing:

#### Manual Sync

From your Mac:
```bash
# Sync from Mac to Rocky VM
rsync -avz ~/rocky_vm_files/ username@rocky_vm_ip:~/host_shared/

# Sync from Rocky VM to Mac
rsync -avz username@rocky_vm_ip:~/host_shared/ ~/rocky_vm_files/
```

#### Continuous Sync

Run the sync script to continuously sync files:
```bash
~/sync_rocky_continuous.sh
```

Keep this terminal window open while working.

### Using Continuous File Syncing

For both VMs, continuous file syncing is set up with these scripts:

- `~/sync_ubuntu_continuous.sh`: Syncs between `~/ubuntu_vm_files` on Mac and `~/host_shared` on Ubuntu VM
- `~/sync_rocky_continuous.sh`: Syncs between `~/rocky_vm_files` on Mac and `~/host_shared` on Rocky Linux VM

To use continuous syncing:

1. Open a terminal window
2. Run the appropriate sync script
3. Leave the terminal window open while working
4. Changes made on either side will automatically sync to the other

## Development Workflow

### Working with Local Development Tools

Both VMs have these development tools installed:

- Docker and Docker Compose
- Git
- Python 3 and pip
- Node.js and npm
- Basic development tools (gcc, make, etc.)

### Working with Docker

```bash
# Check Docker status
sudo systemctl status docker

# Run a docker container
docker run hello-world

# Build and start services with Docker Compose
docker-compose up -d

# Stop services
docker-compose down
```

### Code Editing Workflow

For the best development experience:

1. Edit code on your Mac using your preferred editor
2. Files will automatically sync to the VM (if using continuous sync)
3. Run and test code on the VM
4. View results on the VM or sync them back to your Mac

## Managing VM Resources

### Changing VM Settings

To adjust VM resources (must be done when VM is powered off):

1. Shut down the VM
2. In UTM, select the VM
3. Click "Edit"
4. Adjust settings (RAM, CPU cores, etc.)
5. Click "Save"
6. Start the VM

### Monitoring Resource Usage

Within the VM:
```bash
# View real-time system resource usage
top

# More detailed view
htop  # Install with: sudo apt install htop (Ubuntu) or sudo dnf install htop (Rocky)

# View memory usage
free -m

# View disk usage
df -h
```

## Backing Up VMs

### Creating VM Snapshots

1. Shut down the VM
2. In UTM, right-click on the VM
3. Select "Save VM Screenshot"
4. Choose a name and location for the snapshot
5. Click "Save"

### Exporting VMs

1. Shut down the VM
2. In UTM, right-click on the VM
3. Select "Share VM"
4. Choose "Export VM"
5. Select a location to save the .utm file

### Importing VMs

1. In UTM, click "+" 
2. Select "Import Virtual Machine"
3. Select the .utm file
4. The VM will be added to UTM

## Common Tasks

### Package Management

#### Ubuntu:
```bash
# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade

# Install a package
sudo apt install package-name
```

#### Rocky Linux:
```bash
# Update package lists
sudo dnf check-update

# Upgrade installed packages
sudo dnf upgrade

# Install a package
sudo dnf install package-name
```

### System Services

```bash
# Check status of a service
sudo systemctl status service-name

# Start a service
sudo systemctl start service-name

# Enable a service at boot
sudo systemctl enable service-name

# Restart a service
sudo systemctl restart service-name
```

### Network Management

```bash
# Check network interfaces
ip addr show

# Test connectivity
ping -c 4 google.com

# Check listening ports
sudo ss -tuln

# Test specific port connectivity
nc -zv hostname port
```

### VM-to-VM Communication

To communicate between VMs:

1. Find IP addresses of both VMs:
   ```bash
   ip addr show
   ```

2. From one VM, connect to the other:
   ```bash
   # Using ping
   ping -c 4 other_vm_ip
   
   # Using SSH (if SSH is enabled on both)
   ssh username@other_vm_ip
   ```

3. For web services, use the VM's IP and port:
   ```bash
   curl http://other_vm_ip:port
   ```

## Troubleshooting

### VM Won't Start

1. Ensure your Mac has sufficient resources
2. Check UTM logs (Help > Show Log)
3. Try restarting UTM
4. Check if another VM is using conflicting resources

### Network Connectivity Issues

1. Check VM network settings in UTM
2. Verify your Mac's network connection
3. Ensure VM has proper IP configuration
   ```bash
   ip addr show
   ```
4. Check network services are running
   ```bash
   sudo systemctl status NetworkManager
   ```

### File Sharing Issues

#### Ubuntu VM:

1. Check the mount is working:
   ```bash
   mount | grep 9p
   ```

2. Remount if necessary:
   ```bash
   sudo mount -t 9p -o trans=virtio share ~/host_shared
   ```

3. Fix permissions:
   ```bash
   sudo chown -R $USER:$USER ~/host_shared
   ```

#### Rocky Linux VM:

1. Verify SSH connectivity:
   ```bash
   # From Mac
   ssh username@rocky_vm_ip
   ```

2. Check rsync is installed:
   ```bash
   rsync --version
   ```

3. Run manual sync with verbose output:
   ```bash
   # From Mac
   rsync -avvz ~/rocky_vm_files/ username@rocky_vm_ip:~/host_shared/
   ```

### Resolving "Permission Denied" Errors

```bash
# Check ownership of directory
ls -la ~/host_shared

# Change ownership if needed
sudo chown -R $USER:$USER ~/host_shared

# Set proper permissions
chmod -R 755 ~/host_shared
```

### Resolving SSH Connection Issues

```bash
# Check SSH service status
sudo systemctl status sshd

# Start SSH if not running
sudo systemctl start sshd

# Enable SSH to start at boot
sudo systemctl enable sshd

# Check SSH configuration
sudo nano /etc/ssh/sshd_config
```

## Using SSH Keys for Password-less Login

To avoid typing passwords when SSH-ing to your VMs:

1. On your Mac, generate an SSH key (if you haven't already):
   ```bash
   ssh-keygen -t ed25519
   ```

2. Copy your key to each VM:
   ```bash
   ssh-copy-id username@vm_ip_address
   ```

3. Now you can SSH without a password:
   ```bash
   ssh username@vm_ip_address
   ```

## Disclaimer

This manual is provided "as is" without warranty of any kind. While every effort has been made to ensure accuracy, the user assumes all risks associated with the use of these instructions. Please report any issues encountered.

## Acknowledgements

This manual was developed with assistance from Anthropic's Claude AI assistant, which helped with:
- Documentation writing and organization
- Code structure suggestions
- Troubleshooting and debugging assistance

Claude was used as a development aid while all final implementation decisions and code review were performed by Joshua Michael Hall.
