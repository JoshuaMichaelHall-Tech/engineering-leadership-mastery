# Lab: VPC Multi-Tier Architecture

## Overview
This lab guides you through creating a secure, multi-tier VPC architecture suitable for financial services applications, with proper network segmentation and security controls.

## Learning Objectives
- Design and implement a multi-tier VPC architecture
- Configure public and private subnets across multiple Availability Zones
- Implement security groups and network ACLs for defense in depth
- Set up appropriate routing with internet and NAT gateways
- Apply financial services security best practices to network architecture

## Prerequisites
- AWS account with appropriate permissions
- AWS CLI configured locally
- Terraform installed (optional, for IaC implementation)

## Lab Tasks
1. VPC Creation and CIDR Planning
2. Subnet Configuration (Public, Private Application, Private Data)
3. Route Table Configuration
4. Security Group Implementation
5. Network ACL Configuration
6. Internet and NAT Gateway Setup
7. VPC Endpoint Configuration for AWS Services
8. Network Monitoring and Logging Setup

## Financial Services Considerations
- Regulatory requirements for network segmentation
- Data protection for sensitive financial information
- Audit logging for network traffic
- Compliance documentation

## Validation Tests
- Connectivity testing between tiers
- Security control validation
- High availability verification

## Cleanup Instructions
- Resources to remove after lab completion
- Verification steps for complete cleanup

## INSTRUCTIONS FOR COMPLETION:
1. Add detailed step-by-step instructions for each lab task
2. Include actual Terraform code or CloudFormation templates
3. Add architecture diagram showing the multi-tier design
4. Include specific financial services compliance requirements
5. Add screenshots of expected AWS Console views
6. Create validation scripts to verify successful implementation
