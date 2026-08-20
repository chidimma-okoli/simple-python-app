# Simple Python App — AWS CI/CD Deployment

A containerized Python application deployed to AWS EC2 using Docker Compose and an automated GitHub Actions CI/CD pipeline.

The project demonstrates practical DevOps practices including containerization, continuous integration, continuous deployment, SSH-based deployment, health checks, automatic rollback, manual rollback, and basic container monitoring.

---

## Project Overview

This project started as a simple Python application and was progressively developed into a containerized application with a MySQL database and an automated deployment pipeline.

The application runs on an AWS EC2 Ubuntu server using Docker Compose.

Every push to the `master` branch triggers the GitHub Actions pipeline, which:

1. Tests the Python application.
2. Establishes a secure SSH connection to the EC2 server.
3. Pulls the latest code.
4. Rebuilds and starts the Docker Compose services.
5. Performs an application health check.
6. Provides automatic rollback if deployment fails.
7. Displays deployment and Docker container status.

---

## Architecture

```text
                    Developer
                        |
                        | git push
                        v
                   GitHub Repository
                        |
                        v
                 GitHub Actions
                        |
              +---------+---------+
              |                   |
              v                   v
          CI - Test          CD - Deploy
              |                   |
              |             Secure SSH
              |                   |
              +---------+---------+
                        |
                        v
                   AWS EC2
                  Ubuntu Server
                        |
                 Docker Compose
                  /           \
                 /             \
                v               v
          Python Web App      MySQL
             :5000
                |
                v
             Users

DevOps learner focused on building practical skills through hands-on cloud, Linux, Docker, Git, and CI/CD projects.
