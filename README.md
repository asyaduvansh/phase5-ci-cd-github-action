# DevGuard Pro · CI/CD Pipeline

> Production-grade CI/CD pipeline demonstrating complete DevOps lifecycle —
> from code push to Kubernetes deployment with security scanning and
> approval gates.

[![CI/CD](https://github.com/USERNAME/phase5-ci-cd-github-action/actions/workflows/main.yml/badge.svg)](https://github.com/USERNAME/phase5-ci-cd-github-action/actions)

---

## 🎯 Overview

This project implements a **complete CI/CD pipeline** for a Python-based
system monitoring tool (DevGuard Pro). The pipeline demonstrates
production-grade DevOps patterns used by companies like Netflix, Uber,
and major financial institutions.

### Key Features

- ✅ **Automated testing** with coverage tracking
- ✅ **Multi-environment deployment** (dev / prod)
- ✅ **Dual-tag image strategy** for rollback capability
- ✅ **Vulnerability scanning** with Trivy
- ✅ **Manual approval gates** for production
- ✅ **Self-hosted runner** for local Kubernetes integration
- ✅ **Automated rollback workflow** with disaster recovery
- ✅ **Comprehensive failure diagnostics**

---

## 🏗️ Architecture# DevGuard Pro · CI/CD Pipeline

> Production-grade CI/CD pipeline demonstrating complete DevOps lifecycle —
> from code push to Kubernetes deployment with security scanning and
> approval gates.

[![CI/CD](https://github.com/USERNAME/phase5-ci-cd-github-action/actions/workflows/main.yml/badge.svg)](https://github.com/USERNAME/phase5-ci-cd-github-action/actions)

---

## 🎯 Overview

This project implements a **complete CI/CD pipeline** for a Python-based
system monitoring tool (DevGuard Pro). The pipeline demonstrates
production-grade DevOps patterns used by companies like Netflix, Uber,
and major financial institutions.

### Key Features

- ✅ **Automated testing** with coverage tracking
- ✅ **Multi-environment deployment** (dev / prod)
- ✅ **Dual-tag image strategy** for rollback capability
- ✅ **Vulnerability scanning** with Trivy
- ✅ **Manual approval gates** for production
- ✅ **Self-hosted runner** for local Kubernetes integration
- ✅ **Automated rollback workflow** with disaster recovery
- ✅ **Comprehensive failure diagnostics**

---

## 🏗️ Architecture

git push
↓
GitHub Repository
↓
┌────────────────────────────────────┐
│      GitHub Actions Pipeline        │
├────────────────────────────────────┤
│  Job 1: Test + Coverage  (cloud)   │
│  Job 2: Build + Push     (cloud)   │
│  Job 3: Security Scan    (cloud)   │
│  Job 4: Deploy K8s       (local)   │
└────────────────┬───────────────────┘
↓
┌──────────────┴──────────────┐
↓                              ↓
DEV Cluster                  PROD Cluster
(auto-deploy)              (approval-gated)


---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **CI/CD** | GitHub Actions |
| **Containers** | Docker, Docker Hub |
| **Orchestration** | Kubernetes (Minikube), kubectl |
| **Testing** | pytest, pytest-cov |
| **Security** | Trivy (vulnerability scanning) |
| **Runner** | Self-hosted GitHub Actions Runner |
| **Language** | Python 3.11, Bash |

---

## 🔄 Workflow

### Normal Deployment Flow

\`\`\`bash
# Development branch (auto-deploy to dev)
git checkout develop
# ... make changes ...
git commit -m "feat: new feature"
git push  # → Auto-deploys to dev cluster

# Production deployment (with approval)
git checkout main
git merge develop
git push  # → Awaits approval, then deploys to prod
\`\`\`

### Emergency Rollback

If production has an issue, trigger rollback workflow:

1. Go to **Actions** tab
2. Select **🔄 Rollback Production**
3. Click **Run workflow**
4. Enter the SHA of last known good version
5. Approve the rollback

Production rolls back in **~30 seconds**.

---

## 📊 Pipeline Jobs

### Job 1: Test + Coverage
- Runs full pytest suite
- Generates coverage report (XML + terminal)
- Uploads test results as artifacts (JUnit XML)

### Job 2: Build + Push
- Builds Docker image
- Tags with both `:latest` and `:<commit-sha>`
- Pushes to Docker Hub

### Job 3: Security Scan
- Scans built image with Trivy
- Reports CRITICAL/HIGH/MEDIUM vulnerabilities
- Uploads detailed JSON report

### Job 4: Deploy to Kubernetes
- Determines environment from branch
- Applies dynamic image tag via sed substitution
- Production deployments require manual approval
- Validates rollout success
- Provides failure diagnostics on errors

---

## 🚀 Quick Start

### Prerequisites
- Linux/macOS with Docker installed
- Minikube cluster running locally
- GitHub repository with Actions enabled
- Docker Hub account
- Self-hosted runner configured (see setup below)

### Required GitHub Secrets
- \`DOCKER_USERNAME\` — Your Docker Hub username
- \`DOCKER_PASSWORD\` — Docker Hub access token

### Required Kubernetes Setup
\`\`\`bash
# Create namespaces
kubectl create namespace dev
kubectl create namespace prod
\`\`\`

### Required GitHub Environments
- \`development\` — auto-deploy enabled
- \`production\` — required reviewers configured

---

## 📁 Repository Structure

\`\`\`
phase5-ci-cd-github-action/
├── .github/
│   └── workflows/
│       ├── main.yml          # Main CI/CD pipeline
│       └── rollback.yml      # Emergency rollback workflow
├── k8s/
│   └── devguard-job.yaml     # Kubernetes Job manifest (templated)
├── src/
│   └── main.py               # DevGuard Pro application
├── tests/
│   └── test_basic.py         # Test suite with coverage
├── Dockerfile                # Multi-stage Docker build
├── requirements.txt          # Python dependencies
├── .coveragerc              # Coverage configuration
└── README.md                # This file
\`\`\`

---

## 🎓 Learning Outcomes

This project demonstrates mastery of:

- GitHub Actions workflow design
- Docker image lifecycle (build, tag, push, scan)
- Kubernetes deployment patterns (Jobs, namespaces)
- Self-hosted runner architecture
- Multi-environment promotion strategies
- Vulnerability management
- Production safety patterns (approvals, rollbacks)
- Infrastructure as Code principles

---

## 📈 Phase 5 Roadmap (Cloud School MLOps)

This project is part of the **Cloud School MLOps** learning roadmap:

- ✅ **Phase 1** — Linux Systems + Debugging
- ✅ **Phase 2** — Code + Git + Automation
- ✅ **Phase 3** — Docker (Production Level)
- ✅ **Phase 4** — Kubernetes
- ✅ **Phase 5** — CI/CD with GitHub Actions ← **You are here**
- ⏳ **Phase 6** — AWS (EC2, ECR, EKS, S3)
- ⏳ **Phase 7** — MLflow + DVC
- ⏳ **Phase 8** — Monitoring (Prometheus + Grafana)
- ⏳ **Phase 9** — Terraform (Infrastructure as Code)
- ⏳ **Phase 10** — Capstone (SentinelML — full MLOps platform)

