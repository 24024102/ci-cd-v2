# DevOps Pipeline: FastAPI, Kubernetes, and Terraform

This repository contains a full deployment pipeline for a Python FastAPI application connected to a Redis database. It demonstrates containerization, continuous integration/continuous deployment (CI/CD), Kubernetes orchestration, and AWS infrastructure provisioning.

## Technologies Used
- Python (FastAPI)
- Redis
- Docker & Docker Hub
- Kubernetes
- GitHub Actions
- Terraform
- Amazon Web Services (AWS EC2)

## Project Structure
- `app.py`: The main Python application code.
- `Dockerfile`: Instructions for building the application's Docker image.
- `k8s.yml`: Kubernetes manifests (Deployments and Services) for both the FastAPI application and the Redis database.
- `.github/workflows/main.yml`: GitHub Actions pipeline for automated Docker image building and pushing.
- `main.tf`: Terraform configuration to provision an AWS EC2 instance, configure security groups, and automatically deploy the Docker container on startup.

## CI/CD Pipeline
The project uses GitHub Actions for automation. Every time code is pushed to the `main` branch, the pipeline automatically:
1. Checks out the source code.
2. Logs into Docker Hub using encrypted repository secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`).
3. Builds a new Docker image.
4. Pushes the latest image to Docker Hub.

## Local Deployment (Kubernetes)
To run this project locally, you need Docker Desktop with Kubernetes enabled.

1. Apply the Kubernetes configuration to your local cluster:
   kubectl apply -f k8s.yml

2. Set up port forwarding to access the service:
   kubectl port-forward svc/fastapi-service 8080:80

3. Open your browser and navigate to:
   http://localhost:8080

## Cloud Deployment (AWS via Terraform)
To deploy the application to a public AWS server, you need the AWS CLI configured and Terraform installed.

1. Initialize the Terraform working directory:
   terraform init

2. Review the infrastructure plan:
   terraform plan

3. Provision the resources on AWS:
   terraform apply

4. Type "yes" when prompted. Once complete, Terraform will output the public IP address of your new EC2 instance. Note: It may take 1-2 minutes for the startup script to install Docker and pull your image before the website becomes accessible.

5. To delete all AWS resources and prevent unwanted charges, run:
   terraform destroy
