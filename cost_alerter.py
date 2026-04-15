import boto3
import json
from datetime import datetime, timedelta

# Your threshold — alert if daily cost goes above this
THRESHOLD = 5.00

def get_yesterday_cost():
    client = boto3.client('ce', region_name='us-east-1')
    
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.today().strftime('%Y-%m-%d')
    
    response = client.get_cost_and_usage(
        TimePeriod={'Start': yesterday, 'End': today},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    
    cost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    return float(cost), yesterday

def check_and_alert():
    print("Checking AWS costs...")
    
    cost, date = get_yesterday_cost()
    print(f"Date: {date}")
    print(f"Total cost: ${cost:.2f}")
    
    if cost > THRESHOLD:
        print(f"ALERT! Cost ${cost:.2f} is above threshold ${THRESHOLD:.2f}")
    else:
        print(f"All good! Cost ${cost:.2f} is within normal range.")
    
    # Save report
    report = {
        'date': date,
        'cost': cost,
        'threshold': THRESHOLD,
        'alert': cost > THRESHOLD
    }
    
    with open('cost_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    
    print("Report saved to cost_report.json")

check_and_alert()