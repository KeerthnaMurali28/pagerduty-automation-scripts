#!/usr/bin/env python


import requests
import sys
import json
import csv
import argparse

parser = argparse.ArgumentParser(description='Update Global Events')
parser.add_argument('condition', help='for mutiple conditions pass as comma separated string,eg:CPU,SQL')
parser.add_argument('route', help='route to the service ID, service ID obtained in the in the get_services.py')
parser.add_argument('pattern', help='pattern to generate the service ID ----- Eg: "(.*)(UTC)"')
parser.add_argument('rule_id', help='event rule ID')

args = parser.parse_args()
condition = args.condition.split(',')
route = args.route
pattern = args.pattern
rule_id = args.rule_id
api_key = ''

API_URL = 'https://api.pagerduty.com/event_rules/' + rule_id
api_key = ''
HEADERS = {'Content-type': 'application/json','Authorization': 'Token token=' api_key}

def update_event():
    conditionArray = []
    conditionArray.append("or")

    for i in condition:
        conditionArray.append([
            "contains",
            [
                "path",
                "description"
            ],
            i
        ])

    data = {
            "disabled": "false",
            "condition": conditionArray,
            "catch_all": "false",
            "advanced_condition": [],
            "actions": [
                [
                    "route",
                    route
                ],
                [
                    "extract",
                    pattern,
                    [
                        "path",
                        "description"
                    ],
                    "description"
                ]
            ]
        }

    print data
    result = requests.put(
        API_URL,
        headers=HEADERS,
        data=json.dumps(data)
    )
    return json.loads(result.text)

update_event()