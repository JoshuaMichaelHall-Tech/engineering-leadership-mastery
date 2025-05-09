# Terraform Labs

## Overview
This directory contains hands-on Terraform lab exercises designed to develop Infrastructure as Code skills essential for DevOps/SRE roles in financial services environments.

## Labs Structure
Each lab follows a structured approach:
- **Objective**: Clear goal for the lab exercise
- **Prerequisites**: Required tools and provider configurations
- **Implementation Steps**: Step-by-step instructions
- **Validation Tests**: How to verify successful implementation
- **Financial Services Considerations**: Security, compliance, and best practices

## Labs Included
1. **Module Development**: Creating reusable Terraform modules
2. **Multi-Environment Infrastructure**: Dev/test/prod environment configuration
3. **State Management**: Remote state configuration with locking
4. **Security Controls**: Implementing security best practices in Terraform
5. **Compliance Automation**: Implementing compliance checks and guardrails
6. **CI/CD Integration**: Terraform in automated pipelines

## Environment Setup
Labs require:
- Terraform v1.0+ installed
- AWS CLI configured (for AWS-based labs)
- Git for version control
- Text editor or IDE with Terraform support

Setup instructions are provided in the `setup/` directory.

## Usage
Each lab directory contains detailed README instructions and Terraform configuration files. To begin a lab:

1. Navigate to the lab directory: `cd labs/terraform-labs/[lab-name]`
2. Review the README.md for objectives and prerequisites
3. Follow the implementation steps
4. Complete the validation tests
5. Document your learning in the provided template

## Best Practices
All labs follow HashiCorp recommended practices:
- Modular design
- Clear variable and output definitions
- Comprehensive documentation
- Security-first approach
- State management best practices

## Acknowledgements
These labs were developed with assistance from Anthropic's Claude AI assistant, which helped with documentation writing and organization, while all final implementation decisions and review were performed by Joshua Michael Hall.

## Disclaimer
These labs are for educational purposes. Always follow security best practices and be aware of potential costs when deploying cloud resources. Remember to destroy resources after completing labs.