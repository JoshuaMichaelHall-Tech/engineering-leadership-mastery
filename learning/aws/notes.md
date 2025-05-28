# AWS Certified Solutions Architect - Associate (SAA-C03)

## Course: Adrian Cantrill's AWS SAA-C03

### Case Study: Animals4Life

**Organization Overview:**
- **Type:** Animal Rescue and Awareness (Global)
- **HQ:** Brisbane, Australia (100 staff)
- **Departments:** Call center, admin, IT, marketing, legal, accounts
- **Remote Workers:** ~100 across AU and globally
  - Animal care, activists, lobbyists
  - Locations: London, New York, Seattle

**Current Infrastructure:**
- **On-premises:** Brisbane datacenter
  - Network: 192.168.10.0/24 (Class C)
- **Cloud Pilots (unsuccessful):**
  - AWS Sydney: 10.0.0.0/16 (Class A)
  - Azure: 172.31.0.0/16 (Class B)
  - GCP: attempted

**Field Worker Requirements:**
- Hardware: Laptops with 3G/4G/Satellite connectivity
- Services needed:
  - Data upload/download
  - Email access
  - File access
  - Chat & planning tools
  - Research dataset access

**Current Problems:**
- Legacy on-prem failing (must migrate within 18 months)
- Failed cloud pilots (messy, expensive, no improvement)
- Performance issues (downtime, latency)
- No HA/scalability
- Limited IT automation skills
- High costs for global expansion

**Desired Outcomes:**
- Fast, reliable performance
- Quick regional deployment capability
- Cost-effective and scalable
- Business agility for rapid response
- IoT and Big Data capabilities
- Automation to reduce costs

**Course Application:**
- Learn to ask the right questions
- Apply real-world scenarios to exam preparation

## AWS Account Fundamentals

### AWS Account Basics

**What is an AWS Account?**
- Container for identities (users) and resources
- Requirements:
  - Account name
  - Unique email address
  - Credit card for billing

**Root User:**
- Created automatically with account
- Tied to the account's email address
- Cannot be restricted (full permissions)
- Best practice: Use sparingly, secure with MFA

### Account Structure for Learning

**Recommended Setup:**
1. **Management Account**
   - Primary login account
   - Secure root user with MFA
   - Configure billing alerts and budgets
   - Create IAMADMIN user for daily operations

2. **Production Account**
   - Separate account for production workloads
   - Root user + IAMADMIN user

**Pro tip:** Use email aliases (e.g., user+aws-mgmt@email.com) for multiple accounts

### Initial Account Configuration

**Essential Steps:**
1. **Enable MFA on root user**
   - Authentication factors: Knowledge, Possession, Inherent, Location
   - Use virtual MFA for each user/account

2. **Grant IAM access to billing**
   - Allow IAM users to view billing information

3. **Set appropriate region**
   - Choose closest region for best performance

4. **Configure cost controls**
   - Access: Root user → Account dropdown → Billing
   - Enable billing preferences and alerts
   - Create budget with email notifications

## Identity and Access Management (IAM)

### IAM Overview

**Key Characteristics:**
- **Cost:** Free service
- **Scope:** Global (not region-specific)
- **Resilience:** Globally resilient service
- **Purpose:** Manage identities and permissions within an AWS account

**Core Principles:**
- Principle of least privilege
- All identities start with no permissions
- Explicit allow/deny model

### IAM Components

1. **Users**
   - Represent people or applications
   - One username, one password per user
   - Can have up to 2 access keys

2. **Groups**
   - Collections of related users
   - Simplify permission management

3. **Roles**
   - For AWS services or external access
   - Temporary credentials

4. **Policies**
   - JSON documents defining permissions
   - Can be attached to users, groups, or roles

### Creating an Admin User

**Steps to create IAMADMIN:**
1. Create account alias for easier login
2. Create new IAM user
3. Attach AdministratorAccess policy
4. Set strong password
5. Enable MFA
6. Use this user instead of root for daily tasks

### CLI Authentication

**IAM Access Keys:**
- **Components:**
  - Access Key ID (public)
  - Secret Access Key (private)
- **Limitations:**
  - Maximum 2 per user
  - Only for users (not roles)
  - Can be activated/deactivated

**AWS CLI Setup:**

1. **Install AWS CLI v2 (macOS):**
   ```bash
   curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
   sudo installer -pkg AWSCLIV2.pkg -target /
   ```

2. **Configure profile:**
   ```bash
   aws configure --profile <profile-name>
   # Enter:
   # - Access Key ID
   # - Secret Access Key
   # - Default region (e.g., us-east-1)
   # - Default output format (press Enter for default)
   ```

3. **Test configuration:**
   ```bash
   aws s3 ls --profile <profile-name>
   # Success = no error message
   ```

**Access Key Management:**
- Login → Security Credentials → Create Access Key
- Select purpose and add descriptive tag
- Store securely (shown only once)
- Rotate regularly for security
