# AWS Cost Anomaly Alerter

A Python script that monitors your AWS daily costs and alerts you when spending goes above a set threshold. No more surprise AWS bills.

## Tech Stack
- Python 3
- boto3 (AWS SDK)
- AWS Cost Explorer

## What It Does
- Connects to AWS Cost Explorer using boto3
- Gets yesterday's total AWS spend
- Compares against a set threshold
- Alerts if cost is too high
- Saves a daily JSON report to cost_report.json

## How to Run

1. Install dependencies: pip install -r requirements.txt
2. Configure AWS: aws configure
3. Run the script: python3 cost_alerter.py

## Sample Output
Checking AWS costs...
Date: 2026-04-13
Total cost: $0.00
All good! Cost $0.00 is within normal range.
Report saved to cost_report.json

## Author
Sadhvi - Cloud Engineer | AWS Certified Solutions Architect
