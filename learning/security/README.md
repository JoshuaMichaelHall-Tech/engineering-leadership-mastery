# Security Learning Path for DevOps/SRE

## Overview
This directory documents my journey learning security practices essential for DevOps/SRE roles in financial services environments, with a focus on implementing security as code and automation.

## Learning Philosophy
> "Master the basics. Then practice them every day without fail." - John C. Maxwell

This learning path follows a structured approach:
- Start with security fundamentals and mindset
- Focus on practical implementation of security controls
- Emphasize automation and "security as code"
- Apply financial services regulatory requirements

## Security Topics Covered

### Foundation
- **Security Fundamentals**: Core principles and concepts
- **Threat Modeling**: Identifying and prioritizing threats
- **Security Architecture**: Defense-in-depth strategies
- **Secure Development**: Secure coding practices
- **Vulnerability Management**: Scanning, prioritization, remediation

### Infrastructure & Cloud Security
- **AWS Security**: Service-specific security controls
- **Infrastructure as Code Security**: Securing Terraform and CloudFormation
- **Network Security**: Firewalls, NACLs, VPCs, TLS
- **Identity & Access Management**: Zero trust implementation
- **Secrets Management**: Vault, AWS Secrets Manager, key management

### Application & Container Security
- **Container Security**: Image scanning, runtime protection
- **Kubernetes Security**: RBAC, network policies, admission control
- **API Security**: Gateway protection, authentication, authorization
- **SAST/DAST**: Code and application scanning
- **Data Protection**: Encryption, tokenization, masking

### Compliance & Governance
- **Financial Services Regulations**: SOX, PCI-DSS, GDPR
- **Compliance as Code**: Automated compliance verification
- **Audit Logging**: Comprehensive logging for investigations
- **Evidence Collection**: Automated evidence for audits
- **Security Policies**: Implementation and enforcement

### DevSecOps Implementation
- **Pipeline Security**: CI/CD security integration
- **Security Testing Automation**: Automated security validation
- **Incident Response**: Detection and remediation automation
- **Security Monitoring**: Real-time security monitoring
- **Security Metrics**: Measuring security effectiveness

## Learning Resources
- **Courses**: SANS SEC540 (Cloud Security), AWS Security Specialty
- **Documentation**: OWASP, NIST, CIS Benchmarks
- **Labs**: Practical implementations in the [labs/security-labs](../../labs/security-labs) directory
- **Projects**: Security automation in the [projects/security-automation](../../projects/security-automation) directory

## Certification Path
- AWS Security Specialty (future)
- Certified Kubernetes Security Specialist (future)

## Study Notes
Detailed notes on key security concepts are organized in topic-specific directories.

## Acknowledgements
This learning path was developed with assistance from Anthropic's Claude AI assistant, which helped with documentation writing and organization, while all final implementation decisions and review were performed by Joshua Michael Hall.

## Disclaimer
This documentation represents personal learning and should not be considered authoritative security guidance. Always follow your organization's security policies and consult qualified security professionals.