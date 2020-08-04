#!/usr/bin/env python

import argparse
import requests
import sys
import json

parser = argparse.ArgumentParser(description='Graph alert volumes for a given escalation policy.')

# adding condtions ex: condition1,condition2........
parser.add_argument('condition')
# Name of the service
parser.add_argument('route_to_service')
# Regex Pattern
parser.add_argument('pattern')

args = parser.parse_args()
condition = args.condition.split(',')
route = args.route_to_service
pattern = args.pattern

print ('condition: ' + args.condition)
print ('route service: ' + route)
print ('pattern: ' + pattern)

API_URL = 'https://api.pagerduty.com/event_rules'
API_KEY = ''
HEADERS = {'Content-type': 'application/json','Authorization': 'Token token=' + API_KEY}

def get_services():
    serviceId=''
    url = 'https://api.pagerduty.com/escalation_policies/P9KJL1P'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    r = requests.get(url, headers=headers)

    for i in r.json()['escalation_policy']['services']:
        if(i['summary'] == route):
            serviceId = i['id']
    
    print ('service id: ' + serviceId)
    return serviceId

def create_event(serviceId):
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
                    serviceId
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

    print (data)
    result = requests.post(
        API_URL,
        headers=HEADERS,
        data=json.dumps(data)
    )
    return json.loads(result.text)['id']

def run():
    serviceId = get_services()

    if(serviceId == ''):
        print ('Service Not Found')
        return -1

    print ("Success :) " + create_event(serviceId))

run()