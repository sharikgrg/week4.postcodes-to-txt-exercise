from function_postcodes import *
list = []
postcode1 = importing_functions('TN234QY')
postcode2 = importing_functions('E162RJ')
postcode3 = importing_functions('E162RD')
list.append(postcode1)
list.append(postcode2)
list.append(postcode3)
for datas in list:
    append_to_file('postcode_dets.txt', datas)