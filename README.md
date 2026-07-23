# Semgrep Findings Export

## Setup

Create a `.env` file containing:

```text
SEMGREP_APP_TOKEN=your-token
DEPLOYMENT_SLUG=your-deployment-slug
```

The token and deployment slug can be obtained from the Semgrep UI.

Documentation:

- Authentication:
  https://docs.semgrep.dev/api-reference/v1/Authentication

- List Deployments:
  https://docs.semgrep.dev/api-reference/v1/deploymentsservice/list-deployments

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Script

```bash
python fetch-findings.py
```