# AWS SAA-C03 Anki Flashcards

## AWS Account Fundamentals

What three things are required to create an AWS account?; 1. Account name 2. Unique email address 3. Credit card for billing

What is the AWS root user and why is it important?; The root user is created automatically with the account, has unrestricted access to all resources, and cannot be limited. Best practice: use sparingly and secure with MFA.

What's a good strategy for managing multiple AWS accounts using a single email?; Use email aliases (e.g., user+aws-mgmt@email.com, user+aws-prod@email.com)

What are the 4 essential steps for initial AWS account configuration?; 1. Enable MFA on root user 2. Grant IAM access to billing 3. Set appropriate region 4. Configure cost controls (budgets and alerts)

What are the 4 types of authentication factors for MFA?; Knowledge (something you know), Possession (something you have), Inherent (something you are - biometric), Location (somewhere you are)

How do you access AWS billing and cost management?; Root user → Account dropdown → Billing → Set up billing preferences and create budgets with email notifications

## IAM (Identity and Access Management)

What are the key characteristics of AWS IAM?; Free service, Global scope (not region-specific), Globally resilient, Purpose: manage identities and permissions within an AWS account

What is the principle of least privilege in IAM?; Grant only the minimum permissions necessary for users/services to perform their required tasks

What permissions do IAM identities start with by default?; No permissions - all access must be explicitly granted

What are the 4 main IAM components?; 1. Users (people/apps) 2. Groups (collections of users) 3. Roles (for services/external access) 4. Policies (JSON permission documents)

How many passwords and access keys can an IAM user have?; One username/password and up to 2 access keys

What is an IAM policy?; A JSON document that defines permissions, can be attached to users, groups, or roles

What's the recommended alternative to using the root user for daily tasks?; Create an IAMADMIN user with AdministratorAccess policy

What are the steps to create a secure IAMADMIN user?; 1. Create account alias 2. Create IAM user 3. Attach AdministratorAccess policy 4. Set strong password 5. Enable MFA 6. Use instead of root

## IAM Access Keys

What are the two components of an IAM access key?; Access Key ID (public) and Secret Access Key (private - shown only once)

What are the limitations of IAM access keys?; Maximum 2 per user, only for users (not roles), can be activated/deactivated

Can IAM roles use access keys?; No, access keys are only for IAM users, not roles

What security best practice should you follow with access keys?; Rotate them regularly and store them securely

## AWS CLI Configuration

What command installs AWS CLI v2 on macOS?; curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg" && sudo installer -pkg AWSCLIV2.pkg -target /

What command configures an AWS CLI profile?; aws configure --profile <profile-name>

What 4 pieces of information does 'aws configure' ask for?; 1. Access Key ID 2. Secret Access Key 3. Default region (e.g., us-east-1) 4. Default output format

How do you test if AWS CLI is configured correctly?; Run: aws s3 ls --profile <profile-name> - Success = no error message

Why use named profiles with AWS CLI?; To manage multiple AWS accounts/environments from the same machine

## AWS Account Architecture

What is the recommended AWS account structure for learning/development?; 1. Management Account (primary login, billing, IAMADMIN user) 2. Production Account (separate workloads, own root + IAMADMIN)

Why should you create separate AWS accounts for different environments?; Security containerization - if one account is compromised, damage is limited to that account only

What network ranges were used in the Animals4Life case study?; On-prem: 192.168.10.0/24 (Class C), AWS Pilot: 10.0.0.0/16 (Class A), Azure Pilot: 172.31.0.0/16 (Class B)

## Cost Management

Where do you configure AWS cost alerts and budgets?; Root user → Account dropdown → Billing → Billing Preferences

What cost control features should you enable immediately?; 1. Billing preferences with email delivery 2. Cost alerts 3. Budget with email notifications

Why is it important to grant IAM users access to billing information?; So non-root users can monitor costs and budgets without needing root access

## Security Best Practices

What should you do immediately after creating a root user?; Enable MFA (Multi-Factor Authentication)

How often should you use the root user account?; As rarely as possible - only for tasks that require root permissions

What's the security model for new IAM identities?; Explicit allow/deny model - start with no permissions

Why create new AWS accounts for each course or major project?; To maintain clean separation, easy cleanup, and prevent accidental resource conflicts

## Real-World Application

What were the main problems in the Animals4Life case study?; Legacy on-prem failing (18-month deadline), failed cloud pilots, performance issues, no HA/scalability, limited automation skills, high expansion costs

What were the desired outcomes for Animals4Life's cloud migration?; Fast performance, quick regional deployment, cost-effective scaling, business agility, IoT/Big Data capabilities, automation

What types of users need to be considered in a global organization?; HQ staff, remote workers, field workers with varying connectivity (3G/4G/Satellite)

Why did the initial cloud pilots fail for Animals4Life?; Messy implementation, expensive, no performance improvement over on-premises

## IAM Deep Dive

What does "globally resilient" mean for IAM?; IAM is replicated across all AWS regions automatically, providing high availability

Can IAM in one account control users in another account?; No, IAM has no direct control over external accounts or users (but can use federation)

What is identity federation in IAM?; Ability to grant access to AWS resources to users authenticated by external identity providers

Where do you manage IAM access keys?; Login → Security Credentials → Access Keys → Create/Manage

What should you add when creating an access key?; A descriptive tag to identify the key's purpose

How many MFA devices should you configure per account?; Virtual MFA for each user for each account (root + all IAM users)