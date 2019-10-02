import requests
def importing_functions(postcode):
    request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
    retrieving_data = request_postcode.json()
    postcode = retrieving_data['result']['postcode']
    longitude = retrieving_data['result']['longitude']
    latitude = retrieving_data['result']['latitude']
    print(postcode, longitude, latitude)

def append_to_file(file, postcode):
    try:
        with open(file,'a') as opened_file:
            opened_file.write(postcode + '\n')
    except FileNotFoundError:
        print('File not found')