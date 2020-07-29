# pagerduty-automation-scripts
PagerDuty Automation
Please update your API Key before Running any of the script

To Generate the API key:
1. Go to https://kellerwilliams.pagerduty.com/api_keys
2. Click Create API_key
3. Make sure to copy the API keys
4. USe the key for running the script


To Create Global Event Rules 

Run: python create_global_events.py condition serviceId pattern

Eg:

python create_global_events.py access PRG01ML (.*)(UTC)


To Get the Service Id

Run: python get_services.py service service_name(available in PD)

Eg:

python get_services.py service access

To get all the service ID along with the service_name

Run: python get_services.py all

To get all the serviceID along with the service_name in CSV format

python get_services.py --csv


To trigger,acknowledge and resolve an incident manually

run: python trigger_incidents.py "Incident description"

The above command will trigger,ack and resolve the manually created incident