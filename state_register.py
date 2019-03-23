import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "party_website.settings")
django.setup()
from party.models import State, District
import json

json_file = open('states-and-districts.json', 'r')
data = json_file.read()
json_file.close()
data = json.loads(data)
data = data['states']
for state_data in data:
    state_name = state_data['state']
    print('Registering %s'%(state_name))
    state = State(name=state_name)
    state.save()
    for district_name in state_data['districts']:
        print('Registering %s in %s'%(district_name,state_name))
        district = District(name=district_name, parent_state=state)
        district.save()
