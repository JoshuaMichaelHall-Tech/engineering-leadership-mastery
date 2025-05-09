# Kubernetes Labs

## Overview
This directory contains hands-on Kubernetes lab exercises focused on container orchestration skills essential for DevOps/SRE roles in financial services environments.

## Labs Structure
Each lab follows a structured approach:
- **Objective**: Clear goal for the lab exercise
- **Prerequisites**: Required tools and environment setup
- **Implementation Steps**: Step-by-step instructions
- **Validation Tests**: How to verify successful implementation
- **Financial Services Considerations**: Security, compliance, and best practices for financial workloads

## Labs Included
1. **Kubernetes Cluster Setup**: Local development environment with Kind or Minikube
2. **Secure Pod Deployment**: Implementing security contexts and pod security policies
3. **Service Mesh Implementation**: Traffic management with Istio for microservices
4. **Secrets Management**: Secure handling of sensitive information
5. **RBAC Configuration**: Role-based access control for financial services environments
6. **Monitoring Implementation**: Prometheus and Grafana setup for observability

## Environment Setup
Labs can be completed using either:
- Local Kubernetes environment (Minikube, Kind, or K3d)
- Cloud-based Kubernetes service (EKS, GKE, or AKS)

Detailed setup instructions are provided in the `setup/` directory.

## Usage
Each lab directory contains detailed README instructions and associated YAML manifests. To begin a lab:

1. Navigate to the lab directory: `cd labs/kubernetes-labs/[lab-name]`
2. Review the README.md for objectives and prerequisites
3. Follow the implementation steps
4. Complete the validation tests
5. Document your learning in the provided template

## Acknowledgements
These labs were developed with assistance from Anthropic's Claude AI assistant, which helped with documentation writing and organization, while all final implementation decisions and review were performed by Joshua Michael Hall.

## Disclaimer
These labs are for educational purposes. Always follow Kubernetes security best practices. Remember to clean up resources after completing labs.