#!/usr/bin/env python

import requests
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Trigger Incidents')
parser.add_argument('trigger')


args = parser.parse_args()
trigger = args.trigger


API_URL = 'https://events.pagerduty.com/generic/2010-04-15/create_event.json'
SERVICE_KEY = ''
HEADERS = {'Content-type': 'application/json'}
parser = argparse.ArgumentParser(description='Trigger Inncident manually.')

parser.add_argument('incident_key')

args = parser.parse_args()
incident_key=args.incident_key

def trigger_incident(service_key,description):
    data = {"service_key": service_key,"event_type": 'trigger',"description": description}
    result = requests.post(
        API_URL,
        headers=HEADERS,
        data=json.dumps(data)
    )
    return json.loads(result.text)['incident_key']

def acknowledge_incident(service_key,incident_key,description):
    data = {"service_key": service_key,"incident_key": incident_key,"event_type": 'acknowledge',"description": description}
    result = requests.post(
        API_URL,
        headers=HEADERS,
        data=json.dumps(data)
    )
    print result.text

def resolve_incident(service_key,incident_key,description):
    data = {"service_key": service_key,"incident_key": incident_key,"event_type": 'resolve',"description": description}
    result = requests.post(
        API_URL,
        headers=HEADERS,
        data=json.dumps(data)
    )
    print result.text

incident_key = trigger_incident(SERVICE_KEY,trigger)

acknowledge_incident(SERVICE_KEY,incident_key,"Someone is working on it.")
resolve_incident(SERVICE_KEY,incident_key,"The incident is resolved")