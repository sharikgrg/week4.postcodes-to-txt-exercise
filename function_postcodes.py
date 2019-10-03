import requests
import json

# request the data and using .json get the data in a dictionary.
# prints out relevant data using the keys
def importing_functions(postcode):
    request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
    retrieving_data = request_postcode.json()
    postcode = json.dumps(retrieving_data['result']['postcode'])
    return str(postcode)


# to add the data into the .txt file.

def append_to_file(file, postcode = {}):
    try:
        with open(file,'a') as opened_file:
            opened_file.write(postcode + '\n')
    except FileNotFoundError:
        print('File not found')