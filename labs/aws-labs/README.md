# AWS Labs

## Overview
This directory contains hands-on AWS lab exercises designed to develop practical cloud infrastructure skills for DevOps/SRE roles in financial services environments.

## Labs Structure
Each lab follows a structured approach:
- **Objective**: Clear goal for the lab exercise
- **Prerequisites**: Required AWS services and permissions
- **Implementation Steps**: Step-by-step instructions
- **Validation Tests**: How to verify successful implementation
- **Financial Services Considerations**: Security, compliance, and best practices for financial workloads

## Labs Included
1. **VPC Multi-Tier Architecture**: Building secure network architecture with public/private subnets
2. **ECS/Fargate Microservices Deployment**: Containerized application deployment with security controls
3. **RDS High-Availability**: Database implementation with HA for financial workloads
4. **S3 Secure Storage**: Implementing compliant object storage with encryption
5. **IAM Security Implementation**: Least privilege access for financial services

## Usage
Each lab directory contains detailed README instructions and associated terraform/CloudFormation files. To begin a lab:

1. Navigate to the lab directory: `cd labs/aws-labs/[lab-name]`
2. Review the README.md for objectives and prerequisites
3. Follow the implementation steps
4. Complete the validation tests
5. Document your learning in the provided template

## AWS Account Requirements
- AWS Free Tier account (some labs may incur minimal costs)
- IAM user with appropriate permissions
- AWS CLI configured locally

## Acknowledgements
These labs were developed with assistance from Anthropic's Claude AI assistant, which helped with documentation writing and organization, while all final implementation decisions and review were performed by Joshua Michael Hall.

## Disclaimer
These labs are for educational purposes. Always follow AWS best practices for security and cost management. Remember to destroy resources after completing labs to avoid unnecessary charges.