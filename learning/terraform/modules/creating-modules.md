# Creating Reusable Terraform Modules

## Overview

Terraform modules are containers for multiple resources that are used together. They allow you to create reusable components, improve organization, and encapsulate configuration details. For financial services environments, well-designed modules can enforce security, compliance, and best practices.

## Core Components

- **Root Module**: The main directory containing Terraform files
- **Child Modules**: Directories containing reusable Terraform configurations
- **Input Variables**: Parameters that customize module behavior
- **Output Values**: Return values from modules
- **Local Values**: Named expressions for reuse within a module
- **Resources**: AWS or other provider resources defined within the module
- **Data Sources**: Information imported from providers or other sources

## Key Principles

1. **Encapsulation**: Hide unnecessary implementation details
2. **Reusability**: Design for multiple use cases
3. **Composition**: Combine modules to create complex architectures
4. **Versioning**: Track changes to ensure stability

## Implementation Examples

### Module Directory Structure

```
vpc-module/
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
├── examples/
│   ├── simple-vpc/
│   └── complete-vpc/
└── modules/
    ├── subnets/
    └── security-groups/
```

### Module Variables with Validation

```hcl
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  
  validation {
    condition     = can(cidrnetmask(var.vpc_cidr))
    error_message = "The vpc_cidr must be a valid CIDR block."
  }
}

variable "environment" {
  description = "Environment name (e.g., dev, test, prod)"
  type        = string
  
  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "The environment must be one of: dev, test, prod."
  }
}

variable "enable_flowlogs" {
  description = "Whether to enable VPC Flow Logs"
  type        = bool
  default     = true
}
```

### Module Outputs

```hcl
output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.this.id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "security_group_ids" {
  description = "Map of security group IDs by name"
  value       = {
    for sg in aws_security_group.this :
    sg.name => sg.id
  }
}
```

### Using the Module

```hcl
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr      = "10.0.0.0/16"
  environment   = "prod"
  enable_flowlogs = true
  
  private_subnets = {
    "app" = {
      cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
      azs         = ["us-east-1a", "us-east-1b", "us-east-1c"]
    },
    "data" = {
      cidr_blocks = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
      azs         = ["us-east-1a", "us-east-1b", "us-east-1c"]
    }
  }
}
```

## Best Practices

- **Keep modules focused** on a specific piece of infrastructure
- **Use semantic versioning** for module releases
- **Include comprehensive documentation** in README.md
- **Provide examples** demonstrating various use cases
- **Add proper validation** for input variables
- **Set sensible defaults** for optional variables
- **Include thorough automated tests**
- **Enforce security by default** for financial services
- **Design for compliance** with relevant regulations

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Module bloat | Too many resources | Split into smaller, focused modules |
| Version conflicts | Dependency management | Use explicit versioning |
| Hard-coded values | Poor parameterization | Convert to variables with validation |
| Insufficient documentation | Rush to implement | Create comprehensive README.md |

## Financial Services Considerations

- **Compliance Impact**: Modules can enforce regulatory requirements
- **Security Implications**: Well-designed modules implement security by default
- **Audit Requirements**: Module usage should be documented for compliance
- **Governance**: Standardized modules ensure consistent implementation

## Related Concepts

- **Terraform Registry**: Platform for sharing modules
- **Module Composition**: Building larger systems from modules
- **Testing Frameworks**: Tools like Terratest for validation
- **Infrastructure CI/CD**: Automating module testing and deployment

## Resources

- [Terraform Module Documentation](https://developer.hashicorp.com/terraform/language/modules)
- [Module Creation Tutorial](https://developer.hashicorp.com/terraform/tutorials/modules/module-create)
- [Module Development Best Practices](https://developer.hashicorp.com/terraform/language/modules/develop)

## INSTRUCTIONS FOR COMPLETION:
1. Add diagrams showing module relationships and composition
2. Include examples of financial services security modules
3. Add more complex validation examples for compliance requirements
4. Include CI/CD workflows for module testing
5. Add real-world examples from your implementations
