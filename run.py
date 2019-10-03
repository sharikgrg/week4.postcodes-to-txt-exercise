from function_postcodes import *



#inserted postcodes into the functions
postcode1 = importing_functions('TN234QY')
postcode2 = importing_functions('E162RD')
postcode3 = importing_functions('E162RJ')
# print(type(postcode1))

# to add the postcodes into the .txt file
list = [postcode1, postcode2, postcode3]
for data in list:
    append_to_file('postcode.txt', data)

