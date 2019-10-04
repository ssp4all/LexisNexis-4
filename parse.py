import json
import sys
import os
# import path

if os.name == 'nt':
    try:
        here = os.path.abspath(os.path.dirname(__file__))
        p = here + "\\data\\US.AK\\closed\\5GN2-XGG1-DXDT-G4MK-00000-00.json"
        print(p)
        json_data = open(p)
        # print(json_data)
        for i in json_data:
            print(i["attorney_name"])
        
# print(p)
        
    except FileNotFoundError:
        print('File Not Found Error')
else :
    print("Error")
    
 
# sys.path()


