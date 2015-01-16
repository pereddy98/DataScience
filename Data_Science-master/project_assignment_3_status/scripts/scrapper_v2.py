import json
import urllib
import os
import sys
api_key = 'AIzaSyBoFfH_aeX3PsimRsMF1uhzs7RhDqEQJUk'
file = open("rev_personality_data_1.txt", "wb")
with open("properties_freebase.txt") as pfile
with open("../data/personalities_id_aashray_reversed.txt") as infile:
    data=infile.read().splitlines()
    for line in data: 
        #print line
        query = [{'id': line, 'name': None, 
          '/people/person/date_of_birth': None, 
          '/people/person/gender': None, 
          '/people/person/place_of_birth': None,
          '/people/person/nationality': [],
          '/people/person/age': [],
          '/people/deceased_person/date_of_death': None,
          '/people/deceased_person/cause_of_death': [],
          '/medicine/notable_person_with_medical_condition/condition': [],
          '/people/person/profession': []}]
        service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
        params = {
        'query': json.dumps(query),
        'cursor': '',
        'key': api_key
        }
        #print query
        #print query
        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        s=""
        if 'result' in response:
            for result in response['result']:
                reload(sys)
                sys.setdefaultencoding("utf-8")
                if 'name' in result:
                    file.write(str(result['name']))
                file.write(',')
                if '/people/person/date_of_birth' in result:
                    file.write(str(result['/people/person/date_of_birth']))
                file.write(',')
                if '/people/person/gender' in result:
                    file.write(str(result['/people/person/gender']))
                file.write(',')
                if '/people/person/place_of_birth' in result:
                    file.write(str(result['/people/person/place_of_birth']))
                file.write(',')
                if '/people/person/nationality' in result:
                    file.write(str(result['/people/person/nationality']))
                file.write(',')
                if '/people/person/age' in result:
                    file.write(str(result['/people/person/age']))
                file.write(',')
                if '/people/deceased_person/date_of_death' in result:
                    file.write(str(result['/people/deceased_person/date_of_death']))
                file.write(',')
                if '/people/deceased_person/cause_of_death' in result:
                    file.write(str(result['/people/deceased_person/cause_of_death']))
                file.write(',')
                if '/medicine/notable_person_with_medical_condition/condition' in result:
                    file.write(str(result['/medicine/notable_person_with_medical_condition/condition']))
                file.write('\n')
file.close()
