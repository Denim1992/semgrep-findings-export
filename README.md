# Semgrep Findings Export

## Setup

Open `fetch-findings.py` and update the following values:

```python
TOKEN = "your_semgrep_app_token"
DEPLOYMENT_SLUG = "your_deployment_slug"
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

The script retrieves Semgrep Code (SAST) findings from 1 January 2026 onwards and exports the results to `findings-output.json`.