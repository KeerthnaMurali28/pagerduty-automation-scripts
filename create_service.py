#!/usr/bin/env python

import requests
import sys
import json
import csv
import argparse

parser = argparse.ArgumentParser(description='Create Service')
parser.add_argument('service_name', help='for mutiple conditions pass as comma separated string,eg:CPU,SQL')
args = parser.parse_args()
service_name = args.service_name.split(',')


api_key = ''
HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization':'Token token=' + api_key
    }
API_URL = 'https://api.pagerduty.com/services'
def create_service():
    # conditionArray = []
    # conditionArray.append("or")

    for i in service_name:
            data = {
                        "service": {
                            "type": "service",
                            "name": i,
                            "description": i,
                            "acknowledgement_timeout": 600,
                            "auto_resolve_timeout": 600,
                            "alert_grouping": "intelligent",
                            "status": "active",
                            "escalation_policy": {
                            "id": "P9KJL1P",
                            "type": "escalation_policy_reference",
                            "summary": "SupportOps"
                            },
                            "incident_urgency_rule": {
                             "type": "constant",
                             "urgency": "high"
                            },
                            "alert_creation": "create_alerts_and_incidents",
                            "alert_grouping": "time",
                            "alert_grouping_timeout": 2
                            }
                        }

            print data
            result = requests.post(
                API_URL,
                headers=HEADERS,
                data=json.dumps(data)
            )
    return json.loads(result.text)


create_service()