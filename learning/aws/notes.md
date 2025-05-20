
## Course: Cantrill AWS Certified Solutions Architect - Associate (SAA-CO3)

### Example: Animals4Life

Animal Rescue and Awareness:
Global, HQ in Brisbane, AU - 100 staff
Call center, admin, IT, marketing, legal and Accounts
~ 100 Remote workers across AU and Global
  Animal care, activests, lobbyinsts
  London, NY, Seattle

Onprem Datacenter in Brisbane:
AWS trial in SYD, badly
Azure/GCP trials, badly
Open to trying new things

On-prem 192.168.10.0/24 Class C
AWS Pilot 10.0.0.0/16 Class A
Azure Pilot 172.31.0.0/16 Class B

Major offices in London, NY, Seattle consume services from Head Office

Field Workers use:
  Laptops
  3G, 4G, Satellite
  Data u/I & d/I
  Email, File Access
  Chat & Planning
  Research datasets

Problems:
  Legacy on-prem if failing, must move within 18 months
  Should they move to cloud?
  Pilots messy, expensive, no improvement.
  Performance issues: downtime, distance
  Lack of HA/scalability
  IT skills struggle, little automation
  Global expansion - costs for new infrastructure

Ideal Outcomes:
  Fast performance
  Able to deploy quickly into new regions
    Spin up and down quickly
  Low cost and scalable
  Agility
    Leverage real world events, need rapid deployment
  IOT, Big Data
  Automation - low cost

Use in course:
  Learn when and what questions to ask
  Cert exam is based on real world issues

### AWS Accounts

#### Creation
A container for identities (users) and resources
Require account name, unique email address, and credit card
Unique email is tied to root user
Initially, only 1 user, root user
Root can't be restricted
Resource use billed to credit card

#### IAM
Identity and Access Management
IAM service is tied to a particular AWS account
Users, Groups and Roles can be created and given full or limited permissions

#### Security/Containerization
Since each account is contained by default, bad actors who gain access can only do damage in this account.
We will create new AWS accounts for this course.

### Creating Accounts for Course
General(Management) AWS account
  Account for logging in
  Log in with account root user
  *Secure with MFA*
  *Configure a budget*
  Add IAMADMIN user with admin permissions - used to interact with account
Production
  Root and IAMADMIN user
Create new AWS structure for every course!

use email aliases for aws accounts

once account has been created:
  *grant IAM user and role access to billing information*
  *confirm that region is either global or nearby*
  *enable MFA*
    factors - different pieces of evidence to prove identity
        Knowledge, Possession, Inherent (fingerprint), Location
    virtual mfa for each user for each account

### Controlling Costs
Tools for managing costs:
  Login as root
  Upper right dropdown
  Bills on left
  *Billing Preferences: check deliviry and 2 alerts*
  *Create/set a budget*
    *Add email for alerts*


