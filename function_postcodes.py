import requests
def importing_functions(postcode):
    request_postcode = requests.get('http://api.postcodes.io/postcodes/' + postcode)
    retrieving_data = request_postcode.json()
    return retrieving_data