# 🛡️ AWS Serverless GRC & Security Control Center

> 🔗 **Live Demo:** [GRC Cybersecurity Portal](http://grc-fahd-portal-2026.s3-website.eu-west-3.amazonaws.com)
> 
## 📌 Project Overview
This project demonstrates the implementation of a **100% Serverless** microservices architecture on AWS. It is a Governance, Risk, and Compliance (GRC) portal designed to track security remediation actions, including Pentest findings, Cloud Configuration Audits, and Business Continuity Plans (BCP/PRA).

The goal is to validate core Cloud Architect concepts: decoupling, automatic scalability, and granular security (IAM Least Privilege).

## 🏗️ Technical Architecture
The application is built using the following AWS Managed Services:
![Architecture Diagram](./AWS%20CRUD%20APIGATEWAY%20ARCHI.png)
* **Frontend:** Web interface hosted on **Amazon S3** (Static Website Hosting).
* **API Layer:** **Amazon API Gateway** (REST API) acting as a single entry point.
* **Compute (Microservices):** 4 **AWS Lambda** functions (Python 3.12) handling CRUD operations.
* **Database:** **Amazon DynamoDB** (NoSQL Table) for persistent storage.
* **Security (GRC):** **AWS IAM** roles with **Least Privilege Policies** for each specific function.
* **Monitoring:** Execution logs centralized in **Amazon CloudWatch Logs**.



## 📂 Repository Structure
* `/frontend`: UI source code (HTML5/JS/CSS).
* `/backend`: Business logic for Lambda functions (Create, Read, Update, Delete).
* `/docs`: Architecture diagrams and proof of deployment.

## 🚀 Key Features
* ✅ **Intelligent Tagging:** Automatic task categorization via `[Pentest]`, `[Audit]`, and `[BCP/PRA]` tags.
* ✅ **Full CRUD Lifecycle:** Add, View, Update (Remediation), and Delete security findings.
* ✅ **Dynamic Dashboard:** Simulated compliance scoring and real-time task counting.
* ✅ **Cloud Observability:** Native integration with CloudWatch for debugging and audit trails.

---
*Project developed as part of the AWS Solutions Architect Certification - Session 4 (Manara).*
