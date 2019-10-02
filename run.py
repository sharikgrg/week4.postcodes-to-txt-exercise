from function_postcodes import *

#chose 3 random postcodes
postcode1 = 'TN234QY'
postcode2 = 'E162RD'
postcode3 = 'E162RJ'

#inserted postcodes into the functions
importing_functions(postcode1)
importing_functions(postcode2)
importing_functions(postcode3)

# to add the postcodes into the .txt file
list = [postcode1, postcode2, postcode3]
for data in list:
    append_to_file('postcode.txt', data)

