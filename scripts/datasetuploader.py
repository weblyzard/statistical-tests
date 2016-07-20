import urllib
import requests
import json
import sys
import getopt

from datetime import datetime, date

'''
This module converts ASAP datasets to the Statistical Data API format.

Things to consider:
- dates might differ from one dataset to another...
- new datasets might come with additional fields 
(map them to existing fields or add fields to mapping depending on the use case)
'''

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJwZXJtaXNzaW9ucyI6WyJjb20ud2VibHl6YXJkLmFwaS5kb2N1bWVudC5yZXRyaWV2ZTp3ZWJseXphcmQuY29tL3Rlc3QiLCJjb20ud2VibHl6YXJkLmFwaS5kb2N1bWVudC5hZGQ6d2VibHl6YXJkLmNvbS90ZXN0IiwiY29tLndlYmx5emFyZC5hcGkuZG9jdW1lbnQudXBkYXRlOndlYmx5emFyZC5jb20vdGVzdCIsImNvbS53ZWJseXphcmQuYXBpLmRvY3VtZW50LmRlbGV0ZTp3ZWJseXphcmQuY29tL3Rlc3QiLCJjb20ud2VibHl6YXJkLmFwaS5hbm5vdGF0ZTpzZW50aW1lbnQiLCJjb20ud2VibHl6YXJkLmFwaS5hbm5vdGF0ZTpuYW1lZGVudGl0aWVzIl0sImlhdCI6MTQ2OTAxNzQ4OCwiZXhwIjoxNDY5MDU1ODg4LCJhdWQiOlsiY29tLndlYmx5emFyZC5hcGkiXSwiaXNzIjoiY29tLndlYmx5emFyZC5hcGkiLCJzdWIiOiJ0ZXN0QHdlYmx5emFyZCJ9.QQgvq1kPD_oTRnT2ITrV2tS8kxWduT9kFcgGkmh4vhSGOVIi6Tt_mpFXXvCjoctb7aMki_81X6WGPY4dEgBouQ=="

def dataset_uploader(service_url, dataset_path):
    
    with open(dataset_path) as dataset:
        json_data = json.load(dataset)
        for data in json_data:
            jdata = {}
            jdata['_id'] = data['_id']
            jdata['uri'] = "http://example.com/" + str(data['indicator_id']) + "/" + str(data['_id'])
            #print data
            jdata['added_date'] = datetime.now().strftime('%s')
            
            original_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')            
            jdata['date'] = original_date.strftime('%s')
            jdata['indicator_id'] = data['indicator_id']
            jdata['indicator_name'] = data['indicator_name']
            jdata['value'] = data['value']
            jdata['target_location'] = data['target_location']
            obs_data = json.dumps(jdata)
            
            upload_observation(service_url, obs_data, jdata['indicator_id'])
        #print(json_data)

def upload_observation(service_url, observation, indicator_id):
    '''
    Adds an observation to the WL SD repository.
    '''
    indicator = indicator_id
    
    if token is None:
        sys.exit()
    
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % token}
    
    r = requests.post(service_url + indicator, headers=headers, data = observation)
    print(r.text)

def dataset_uploader2(service_url, dataset_path, indicator_id):
    '''
     Converts an observation to the WL SD API format and calls the method that will upload it to the repository.
    '''
    with open(dataset_path) as dataset:
        json_data = json.load(dataset)
        for data in json_data:
            #first part of the method simply performs conversions
            jdata = {}
            
            #in order to avoid similar ids, indicator_id is added before the real id
            jdata['_id'] = indicator_id + '_' + str(data['_id'])
            jdata['indicator_id'] = indicator_id #'WINDAreaPresence'
            
            #change this to indicator_name instead of indicator_id if indicator_name present in the dataset
            jdata['indicator_name'] = indicator_id #'Area Presence'
            
            #a uri is minted using example.com, but if your data is available online (e.g. as Linked Data) you can use your own uri
            jdata['uri'] = "http://example.com/" + str(jdata['indicator_id']) + "/" + str(jdata['_id'])
            #print data
            
            #date conversion to the format used by WL_SD_API
            jdata['added_date'] = datetime.now().strftime('%s')
            
            #just a trick to load 'AreaPresence'
            if indicator_id in ('AreaPresence'):
                original_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')   
            else:
                original_date = datetime.strptime(data['date'], '%Y-%m-%d %H')            
            
            jdata['date'] = original_date.strftime('%s')
            jdata['value'] = data['value']
            
            #adding location
            if 'target_location' in data.keys():
                jdata['target_location'] = data['target_location']
        
            else:
                jdata['location_id'] = data['region_id']
            
            print jdata
            obs_data = json.dumps(jdata)
            
            #call the upload method to do the actual upload following conversion
            upload_observation(service_url, obs_data, jdata['indicator_id'])
    
def main(argv):
    service_url = ''
    dataset_path = ''
    indicator = ''
    
    #Used a classic getopt, but feel free to use Argparse or other methods to get the arguments
    try:
        opts, args = getopt.getopt(argv,"hs:d:i:",["service=","dataset=","indicator="])
    except getopt.GetoptError:
        print 'datasetuploader.py -s <serviceurl> -d <datasetpath> -i <indicator>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'datasetuploader.py -s <serviceurl> -d <datasetpath> -i <indicator>'
            sys.exit()
        elif opt in ("-s", "--service"):
            service_url = arg
        elif opt in ("-d", "--dataset"):
            dataset_path = arg
        elif opt in ("-i", "--indicator"):
            indicator = arg
            
    print 'Service URL is: ', service_url
    print 'Dataset path is: ', dataset_path
    print 'Indicator is:', indicator
    
    dataset_uploader2(service_url, dataset_path, indicator)
    
if __name__ == '__main__':
    print "start"
    
    #print "Arguments: (scriptname) service_url dataset_path indicator"
    
    main(sys.argv[1:])
    
    
    print "end"
    