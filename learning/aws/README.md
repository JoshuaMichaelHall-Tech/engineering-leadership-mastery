# AWS Learning Path for Financial Services

## Overview
This directory documents my journey learning Amazon Web Services (AWS) with a focus on DevOps/SRE roles in financial services environments.

## Learning Philosophy
> "Master the basics. Then practice them every day without fail." - John C. Maxwell

This learning path follows a structured approach:
- Focus on core services first before specialized offerings
- Emphasize security and compliance for financial workloads
- Build practical, real-world implementations
- Document architecture patterns and best practices
- Demonstrate business value and ROI metrics

## Core AWS Services Covered

### Foundational Services
- **IAM**: Identity and access management with financial services security patterns
- **VPC**: Network architecture for secure, multi-tier applications
- **EC2**: Compute service with security hardening and high availability
- **S3**: Object storage with compliance controls and encryption

### Database & Storage
- **RDS**: Relational database service with high availability configurations
- **DynamoDB**: NoSQL database with financial transaction patterns
- **ElastiCache**: In-memory caching for performance optimization
- **EFS/FSx**: File storage options for various workloads

### Application Services
- **ECS/EKS**: Container orchestration for microservices
- **Lambda**: Serverless computing with financial services patterns
- **API Gateway**: API management with security controls
- **SNS/SQS**: Messaging services for decoupled architectures

### Security & Compliance
- **Security Hub**: Centralized security management
- **Config**: Configuration compliance automation
- **CloudTrail**: Audit logging for regulatory requirements
- **KMS/Secrets Manager**: Encryption and secrets management

### Monitoring & Management
- **CloudWatch**: Monitoring and observability
- **X-Ray**: Distributed tracing for microservices
- **CloudFormation**: Infrastructure as Code deployment
- **Systems Manager**: Operations management

## Learning Resources
- **Courses**: Adrian Cantrill's AWS Solutions Architect Associate
- **Documentation**: AWS Well-Architected Framework, AWS Financial Services
- **Labs**: Practical implementations in the [labs/aws-labs](../../labs/aws-labs) directory
- **Projects**: Real-world applications in the [projects](../../projects) directory

## Certification Path
- [AWS Solutions Architect Associate](../../certifications/aws-saa)
- AWS DevOps Engineer Professional (future)
- AWS Security Specialty (future)

## Financial Services Focus
Special focus areas for financial services:
- **Security**: Defense-in-depth strategies for financial data
- **Compliance**: Implementing controls for SOX, PCI-DSS, GDPR
- **High Availability**: Designing for 99.99%+ uptime
- **Disaster Recovery**: Financial-grade recovery strategies
- **Cost Optimization**: Efficient resource utilization
- **Performance**: Optimizing for low-latency transactions
- **Scalability**: Handling peak trading and end-of-month processing

## Business Impact
This learning path emphasizes demonstrating business value through:
- **Cost Reduction**: Cloud optimization techniques
- **Security Posture**: Quantifiable improvement metrics
- **Operational Efficiency**: Automation and reduced MTTR
- **Compliance Automation**: Reduced audit preparation time
- **Innovation Enablement**: Faster time-to-market for new products

## Implementation Plan
The detailed implementation plan is available in the [learning-plan.md](learning-plan.md) file, which outlines the day-by-day learning path.

## Study Notes
Detailed notes on key AWS services and concepts are organized in service-specific directories.

## Acknowledgements
This learning path was developed with assistance from Anthropic's Claude AI assistant, which helped with documentation writing and organization, while all final implementation decisions and review were performed by Joshua Michael Hall.

## Disclaimer
This documentation represents personal learning and should not be considered official AWS guidance. Always refer to AWS official documentation for the most current information.