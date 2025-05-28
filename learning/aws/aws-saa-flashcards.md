# AWS SAA-C03 Anki Flashcards

## AWS Account Fundamentals

Q: What three things are required to create an AWS account?
A: 1. Account name 2. Unique email address 3. Credit card for billing

Q: What is the AWS root user and why is it important?
A: The root user is created automatically with the account, has unrestricted access to all resources, and cannot be limited. Best practice: use sparingly and secure with MFA.

Q: What's a good strategy for managing multiple AWS accounts using a single email?
A: Use email aliases (e.g., user+aws-mgmt@email.com, user+aws-prod@email.com)

Q: What are the 4 essential steps for initial AWS account configuration?
A: 1. Enable MFA on root user 2. Grant IAM access to billing 3. Set appropriate region 4. Configure cost controls (budgets and alerts)

Q: What are the 4 types of authentication factors for MFA?
A: Knowledge (something you know), Possession (something you have), Inherent (something you are - biometric), Location (somewhere you are)

Q: How do you access AWS billing and cost management?
A: Root user → Account dropdown → Billing → Set up billing preferences and create budgets with email notifications

## IAM (Identity and Access Management)

Q: What are the key characteristics of AWS IAM?
A: Free service, Global scope (not region-specific), Globally resilient, Purpose: manage identities and permissions within an AWS account

Q: What is the principle of least privilege in IAM?
A: Grant only the minimum permissions necessary for users/services to perform their required tasks

Q: What permissions do IAM identities start with by default?
A: No permissions - all access must be explicitly granted

Q: What are the 4 main IAM components?
A: 1. Users (people/apps) 2. Groups (collections of users) 3. Roles (for services/external access) 4. Policies (JSON permission documents)

Q: How many passwords and access keys can an IAM user have?
A: One username/password and up to 2 access keys

Q: What is an IAM policy?
A: A JSON document that defines permissions, can be attached to users, groups, or roles

Q: What's the recommended alternative to using the root user for daily tasks?
A: Create an IAMADMIN user with AdministratorAccess policy

Q: What are the steps to create a secure IAMADMIN user?
A: 1. Create account alias 2. Create IAM user 3. Attach AdministratorAccess policy 4. Set strong password 5. Enable MFA 6. Use instead of root

## IAM Access Keys

Q: What are the two components of an IAM access key?
A: Access Key ID (public) and Secret Access Key (private - shown only once)

Q: What are the limitations of IAM access keys?
A: Maximum 2 per user, only for users (not roles), can be activated/deactivated

Q: Can IAM roles use access keys?
A: No, access keys are only for IAM users, not roles

Q: What security best practice should you follow with access keys?
A: Rotate them regularly and store them securely

## AWS CLI Configuration

Q: What command installs AWS CLI v2 on macOS?
A: curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg" && sudo installer -pkg AWSCLIV2.pkg -target /

Q: What command configures an AWS CLI profile?
A: aws configure --profile <profile-name>

Q: What 4 pieces of information does 'aws configure' ask for?
A: 1. Access Key ID 2. Secret Access Key 3. Default region (e.g., us-east-1) 4. Default output format

Q: How do you test if AWS CLI is configured correctly?
A: Run: aws s3 ls --profile <profile-name> - Success = no error message

Q: Why use named profiles with AWS CLI?
A: To manage multiple AWS accounts/environments from the same machine

## AWS Account Architecture

Q: What is the recommended AWS account structure for learning/development?
A: 1. Management Account (primary login, billing, IAMADMIN user) 2. Production Account (separate workloads, own root + IAMADMIN)

Q: Why should you create separate AWS accounts for different environments?
A: Security containerization - if one account is compromised, damage is limited to that account only

Q: What network ranges were used in the Animals4Life case study?
A: On-prem: 192.168.10.0/24 (Class C), AWS Pilot: 10.0.0.0/16 (Class A), Azure Pilot: 172.31.0.0/16 (Class B)

## Cost Management

Q: Where do you configure AWS cost alerts and budgets?
A: Root user → Account dropdown → Billing → Billing Preferences

Q: What cost control features should you enable immediately?
A: 1. Billing preferences with email delivery 2. Cost alerts 3. Budget with email notifications

Q: Why is it important to grant IAM users access to billing information?
A: So non-root users can monitor costs and budgets without needing root access

## Security Best Practices

Q: What should you do immediately after creating a root user?
A: Enable MFA (Multi-Factor Authentication)

Q: How often should you use the root user account?
A: As rarely as possible - only for tasks that require root permissions

Q: What's the security model for new IAM identities?
A: Explicit allow/deny model - start with no permissions

Q: Why create new AWS accounts for each course or major project?
A: To maintain clean separation, easy cleanup, and prevent accidental resource conflicts

## Real-World Application

Q: What were the main problems in the Animals4Life case study?
A: Legacy on-prem failing (18-month deadline), failed cloud pilots, performance issues, no HA/scalability, limited automation skills, high expansion costs

Q: What were the desired outcomes for Animals4Life's cloud migration?
A: Fast performance, quick regional deployment, cost-effective scaling, business agility, IoT/Big Data capabilities, automation

Q: What types of users need to be considered in a global organization?
A: HQ staff, remote workers, field workers with varying connectivity (3G/4G/Satellite)

Q: Why did the initial cloud pilots fail for Animals4Life?
A: Messy implementation, expensive, no performance improvement over on-premises

## IAM Deep Dive

Q: What does "globally resilient" mean for IAM?
A: IAM is replicated across all AWS regions automatically, providing high availability

Q: Can IAM in one account control users in another account?
A: No, IAM has no direct control over external accounts or users (but can use federation)

Q: What is identity federation in IAM?
A: Ability to grant access to AWS resources to users authenticated by external identity providers

Q: Where do you manage IAM access keys?
A: Login → Security Credentials → Access Keys → Create/Manage

Q: What should you add when creating an access key?
A: A descriptive tag to identify the key's purpose

Q: How many MFA devices should you configure per account?
A: Virtual MFA for each user for each account (root + all IAM users)