# 🛡️ AWS Serverless GRC & Security Control Center

> 🔗 **Live Demo:** [Consulter le Portail GRC en direct](http://grc-fahd-portal-2026.s3-website.eu-west-3.amazonaws.com)

## 📌 Project Overview
This project demonstrates the implementation of a **100% Serverless** microservices architecture on AWS. It is a Governance, Risk, and Compliance (GRC) portal designed to track security remediation actions, including Pentest findings, Cloud Configuration Audits, and Business Continuity Plans (BCP/PRA).

## 🏗️ Technical Architecture
The application is built using a modern decoupled approach:

* **Frontend:** Web interface hosted on **Amazon S3**.
* **API Layer:** **Amazon API Gateway** (REST API) as a secure entry point.
* **Compute:** 4 **AWS Lambda** functions (Python 3.12) for CRUD logic.
* **Database:** **Amazon DynamoDB** (NoSQL) for high-availability storage.

![Architecture Diagram](./images/AWS%20CRUD%20APIGATEWAY%20ARCHI.png)

## 🔐 Security & Governance (IAM)
Following the **Principle of Least Privilege**, each microservice is isolated.

### 🛡️ IAM Policy Evidence
Below is the JSON structure applied to the `DeleteTodoFunction` role, restricting access ONLY to the delete action on our specific table:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dynamodb:DeleteItem",
            "Resource": "arn:aws:dynamodb:eu-west-3:*:table/Todos"
        },
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:eu-west-3:*:*"
        }
    ]
}
