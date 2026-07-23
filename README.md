###########################
# Semgrep Findings Export #
########################### 

## Setup ##

- Create a '.env' file containing the following:

SEMGREP_APP_TOKEN=your-token
DEPLOYMENT_SLUG=your-deployment-slug

# Token and slug can be obtained from the Semgrep UI. Documentation below:

https://docs.semgrep.dev/api-reference/v1/Authentication
https://docs.semgrep.dev/api-reference/v1/deploymentsservice/list-deployments

# Install dependencies:
'pip install -r requirements.txt'

# Run script:
'python fetch-findings.py'

