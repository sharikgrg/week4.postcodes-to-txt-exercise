import requests

request_postcode = requests.get('http://api.postcodes.io/postcodes/' + 'TN234QY')

retrieving_data = request_postcode.json()

my_postcode = retrieving_data['result']['postcode']

longitude = retrieving_data['result']['longitude']
latitude = retrieving_data['result']['latitude']
print(f'My postcode is {my_postcode} with longitude {longitude} and latitude {latitude}')