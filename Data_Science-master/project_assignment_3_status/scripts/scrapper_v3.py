# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import urllib
import os
import sys
import pandas as pd
actual_data = pd.read_csv('properties_freebase.csv')
api_key = 'AIzaSyBoFfH_aeX3PsimRsMF1uhzs7RhDqEQJUk'                
file = open("rev_personality_data_aashray_v2.txt", "wb")
file.write('Name')
file.write('<<^>>')
for index, row in actual_data.iterrows():
  file.write((row['header']))
  file.write('<<^>>') 
file.write('\n')
with open("../data/personalities_id_aashray_reversed.txt") as infile:
    data=infile.read().splitlines()   
    for line in data: 
        query=[{'id':line,
        'name':None,
        '/people/cause_of_death/parent_cause_of_death':[],
        '/people/cause_of_death/includes_causes_of_death':[],
        '/people/cause_of_death/people':[],
        '/people/deceased_person/date_of_death':None,
        '/people/deceased_person/place_of_death':None,
        '/people/deceased_person/cause_of_death':[],
        '/people/deceased_person/date_of_cremation':None,
        '/people/deceased_person/place_of_cremation':[],
        '/people/deceased_person/date_of_burial':None,
        '/people/deceased_person/place_of_burial':[],
        '/people/ethnicity/included_in_group':[],
        '/people/ethnicity/includes_groups':[],
        '/people/ethnicity/geographic_distribution':[],
        '/people/ethnicity/languages_spoken':[],
        '/people/ethnicity/population':[],
        '/people/ethnicity/people':[],
        '/people/family_name/people_with_this_family_name':[],
        '/people/person/gender':[],
        '/people/group/member':None,
        '/people/measured_person/measurements':[],
        '/people/measured_person/sizes':[],
        '/people/person/date_of_birth':None,
        '/people/person/place_of_birth':None,
        '/people/person/nationality':[],
        '/people/person/gender':None,
        '/people/person/profession':[],
        '/people/person/religion':[],
        '/people/person/ethnicity':[],
        '/people/person/parents':[],
        '/people/person/children':[],
        '/people/person/sibling_s':[],
        '/people/person/spouse_s':[],
        '/people/person/employment_history':[],
        '/people/person/education':[],
        '/people/person/metaweb_user_s':[],
        '/people/person/signature':[],
        '/people/person/height_meters':None,
        '/people/person/weight_kg':None,
        '/people/person/quotations':[],
        '/people/person/places_lived':[],
        '/people/person/quotationsbook_id':[],
        '/people/person/age':[],
        '/people/person/tvrage_id':[],
        '/people/person/notable_professions':[],
        '/people/person/languages':[],
        '/people/person/group':None,
        '/people/professional_field/professions_in_this_field':[],
        '/people/profession/people_with_this_profession':[],
        '/people/profession/specialization_of':[],
        '/people/profession/specializations':[],
        '/people/profession/part_of_professional_field':[]}]
        service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
        params = {
        'query': json.dumps(query),
        'cursor': '',
        'key': api_key
        }
        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        if 'result' in response:     
            for result in response['result']:
                reload(sys)
                sys.setdefaultencoding("utf-8")
                #file = open("rev11.txt", "wb")
                if 'name' in result:
                    file.write(str(result['name']))
                file.write('<<^>>')
                for index, row in actual_data.iterrows():
                    if row['header'] in result:
                        file.write(str(result[row['header']]))
                    file.write('<<^>>')
                file.write('\n')
file.close()
                

# <codecell>


# <codecell>


