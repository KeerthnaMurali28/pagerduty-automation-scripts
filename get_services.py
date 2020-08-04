#!/usr/bin/env python

import requests
import sys
import json
import csv
import argparse

api_key = ''
HEADERS = {'Content-type': 'application/json','Authorization': 'Token token=' + api_key}

def getServicesFromAPI():
    url = 'https://api.pagerduty.com/escalation_policies/P9KJL1P'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + api_key
    }
    r = requests.get(url, headers=headers)

    return r.json()['escalation_policy']['services']

def exportToCSV(services):
    fileName = 'P9KJL1P_services.csv'
    csvfile = open(fileName, 'w')
    fieldnames = ['id', 'summary', 'html_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in services:
        row = {
            'id': i['id'],
            'summary': i['summary'],
            'html_url': i['html_url']
        }
        writer.writerow(row)
    csvfile.close()
    print ('Successfully exported as ' + fileName)

def printAllServices(services):
    for i in services:
        print ('Service_Id: ' + i['id'] + ', Service_Name: ' + i['summary'])

def getServiceByName(service_name):
    serviceId=''
    services = getServicesFromAPI()

    for i in services:
        if(i['summary'] == service_name):
            serviceId = i['id']
    return serviceId  

def getAllServices(args):
    services = getServicesFromAPI()
    if(args.csv):
        exportToCSV(services)
    else:
        printAllServices(services)

def getService(args):
    service_name = args.service_name
    service_id = getServiceByName(service_name)

    if(service_id == ''):
        print ('Provided Service Name does not exist')
    else:
        print (service_id)

def run():
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Choose a command')

    AllServicesParser = subparsers.add_parser('all', help='"all services" help')
    AllServicesParser.add_argument('--csv', action='store_true',help='Export As CSV')
    AllServicesParser.set_defaults(func=getAllServices)

    serviceParser = subparsers.add_parser('service', help='"get service id by Name" help')
    serviceParser.add_argument('service_name')
    serviceParser.set_defaults(func=getService)

    args = command_parser.parse_args()
    args.func(args)

run() 
