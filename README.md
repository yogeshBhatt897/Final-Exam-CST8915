# Best Buy Staff Service Microservice

## Overview
The BestBuy Staff-Service Microservice is a cloud-native application designed to manage staff information within BestBuy. It provides CRUD (Create, Read, Update, Delete) operations via REST APIs.

## Features
- **Create**: Add new staff members with details such as name, position, department, email, and phone.
- **Read**: Retrieve a list of all staff members.
- **Update**: Update a specific staff member's details.
- **Delete**: Remove a specific staff member.

## Endpoints
- **Create Staff**: `POST /staff`
  - Request Body: `{"name": "<name>", "position": "<position>", "department": "<department>", "email": "<email>", "phone": "<phone>"}`
- **Read Staff**: `GET /staff`
- **Update Staff**: `PUT /staff/:id`
  - Request Body: `{"name": "<name>", "position": "<position>", "department": "<department>", "email": "<email>", "phone": "<phone>"}`
- **Delete Staff**: `DELETE /staff/:id`

## Docker and Deployment
- Docker Image link: https://hub.docker.com/layers/yogeshbhatt0199/staff-service/latest/images/sha256:835b8d904462ee8483f90c745b55010fe41dcaf539743cbb566b16af5d915815?uuid=96338DCD-9A63-4883-AD28-D48690F725A5
- Azure Kubernetes Service (AKS) Deployment YAML File: [bestbuy-staff-service/deployment.yml]

## CI/CD Pipeline
- The CI/CD pipeline automatically builds, tests, and deploys the staff-service to AKS using GitHub Actions.

## Documentation
- This repository contains the complete code and configuration for the staff-service microservice, including the Dockerfile, Kubernetes deployment file, and CI/CD pipeline configuration.

## Technical Issues Encountered
- Not able to Set Up and test CI/CD Pipeline 

## Commit Messages
- App.py: "Initial commit."
- Dockerfile: "Adding Dockerfile"
- deployment.yaml: "Configured Kubernetes deployment for AKS."
- README.md: "Adding README.md."
