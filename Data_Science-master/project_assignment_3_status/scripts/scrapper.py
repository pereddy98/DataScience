import json
import urllib
import os
import sys
api_key = 'AIzaSyBsJOMDBN_Cln1NuTemC30gA-UZCphwsXI'
file = open("../data/personalities_data_aashray_rev.txt", "wb")
with open("../data/personalities_id_aashray_reversed.txt") as infile:
    data=infile.read().splitlines()
    for line in data: 
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
        #response['result']={}
        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        s=""
        #print response
        #print len(response)
        if len(response)==2:
            for result in response['result']:
                #print result
                #reload(sys)
                #sys.setdefaultencoding("latin-1")
                file.write(str(result['name'].encode('utf-8')))
                file.write(',')
                #print result['/people/person/date_of_birth']
                file.write(str(result['/people/person/date_of_birth']).encode('utf-8'))
                file.write(',')
                file.write(str(result['/people/person/gender']).encode('utf-8'))
                file.write(',')
                #file.write(str(result['/people/person/place_of_birth']).encode('utf-8'))
                #file.write(',')
                file.write(str(result['/people/person/nationality']).encode('utf-8'))
                file.write(',')
                file.write(str(result['/people/person/age']).encode('utf-8'))
                file.write(',')
                file.write(str(result['/people/deceased_person/date_of_death']).encode('utf-8'))
                file.write(',')
                file.write(str(result['/people/deceased_person/cause_of_death']).encode('utf-8'))
                file.write(',')
                file.write(str(result['/medicine/notable_person_with_medical_condition/condition']).encode('utf-8'))
                file.write('\n')
file.close()
            
        #print response   
