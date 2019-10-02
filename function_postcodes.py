import requests
import json
def importing_functions(postcode):
    request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
    retrieving_data = request_postcode.json()
    postcode = json.dumps(retrieving_data['result']['postcode'])
    print(postcode)

def append_to_file(file, postcode):
    try:
        with open(file,'a') as opened_file:
            opened_file.write(postcode + '\n')
    except FileNotFoundError:
        print('File not found')