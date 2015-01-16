# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import urllib
import os
import sys
api_key = 'AIzaSyBoFfH_aeX3PsimRsMF1uhzs7RhDqEQJUk'                
file = open("personality_data_aashray_rev_new", "wb") # o/p file
file.write('Name')
file.write('<<^>>')
mylist = []
mylist.append('/people/cause_of_death/parent_cause_of_death')
mylist.append('/people/cause_of_death/includes_causes_of_death')
mylist.append('/people/cause_of_death/people')
mylist.append('/people/deceased_person/date_of_death')
mylist.append('/people/deceased_person/place_of_death')
mylist.append('/people/deceased_person/cause_of_death')
mylist.append('/people/deceased_person/date_of_cremation')
mylist.append('/people/deceased_person/place_of_cremation')
mylist.append('/people/deceased_person/date_of_burial')
mylist.append('/people/deceased_person/place_of_burial')
mylist.append('/people/ethnicity/included_in_group')
mylist.append('/people/ethnicity/includes_groups')
mylist.append('/people/ethnicity/geographic_distribution')
mylist.append('/people/ethnicity/languages_spoken')
mylist.append('/people/ethnicity/population')
mylist.append('/people/ethnicity/people')
mylist.append('/people/family_name/people_with_this_family_name')
mylist.append('/people/group/member')
mylist.append('/people/measured_person/measurements')
mylist.append('/people/measured_person/sizes')
mylist.append('/people/person/date_of_birth')
mylist.append('/people/person/place_of_birth')
mylist.append('/people/person/nationality')
mylist.append('/people/person/gender')
mylist.append('/people/person/profession')
mylist.append('/people/person/religion')
mylist.append('/people/person/ethnicity')
mylist.append('/people/person/parents')
mylist.append('/people/person/children')
mylist.append('/people/person/sibling_s')
mylist.append('/people/person/spouse_s')
mylist.append('/people/person/employment_history')
mylist.append('/people/person/education')
mylist.append('/people/person/metaweb_user_s')
mylist.append('/people/person/signature')
mylist.append('/people/person/height_meters')
mylist.append('/people/person/weight_kg')
mylist.append('/people/person/quotations')
mylist.append('/people/person/places_lived')
mylist.append('/people/person/quotationsbook_id')
mylist.append('/people/person/age')
mylist.append('/people/person/tvrage_id')
mylist.append('/people/person/notable_professions')
mylist.append('/people/person/languages')
mylist.append('/people/person/group')
mylist.append('/people/professional_field/professions_in_this_field')
mylist.append('/people/profession/people_with_this_profession')
mylist.append('/people/profession/specialization_of')
mylist.append('/people/profession/specializations')
mylist.append('/people/profession/part_of_professional_field')

for s in mylist:
  file.write(s)
  file.write('<<^>>') 
file.write('\n')
with open("../data/personalities_id_aashray_reversed.txt") as infile: #i/p person IDs
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
                for s in mylist:
                    if s in result:
                        file.write(str(result[s]))
                    file.write('<<^>>')
                file.write('\n')
file.close()
                

# <codecell>


# <codecell>


