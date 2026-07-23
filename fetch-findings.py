import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SEMGREP_APP_TOKEN")
DEPLOYMENT_SLUG = os.getenv("DEPLOYMENT_SLUG")

# unix timestamp for 1st Jan 2026
SINCE_TIMESTAMP = 1767225600

url = f"https://semgrep.dev/api/v1/deployments/{DEPLOYMENT_SLUG}/findings"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

all_findings = []
page = 0

while True:

    response = requests.get(
        url,
        headers=headers,
        params={
            "issue_type": "sast",
            "page": page,
            "page_size": 1000,
            "since": SINCE_TIMESTAMP
        }
    )

    data = response.json()

    findings = data.get("findings", [])

    if not findings:
        break

    all_findings.extend(findings)
    page += 1

with open("findings-output.json", "w") as outfile:
    json.dump(all_findings, outfile, indent=2)

print(f"Exported {len(all_findings)} findings")
print("Output written to findings-output.json")