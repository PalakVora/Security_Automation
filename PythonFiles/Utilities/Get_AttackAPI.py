#import PythonFiles.Utilities.Get_API as Getting_API
#import Get_API as Getting_API
#import Read_Excel as Getting_Sheet
#import json
#import sys
import json
from Get_API import ReadApi

def find_api(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    try:
        object1=ReadApi()
        object1.Excel_Sheet_Name=Excel_Sheet_Name
        object1.module_name = Module_Name
        object1.Excel_Location = Excel_Location
        print("Outside read excel")
        object1.readexcel()
        object1.find_sheet_name()
        print("Out of sheet name" + object1.sheetname.title)
        row_data=object1.find_module_name()
        print("Outside row")
        object1.read_api_name()
        data['API'] = str(object1.api_name.value)
        print("API is")
        print(data['API'])
        object1.read_method()
        data['HTTPMethod'] =str(object1.http_method.value)
        print(data['HTTPMethod'])
        print("OUtside method")
    except Exception as exception:
        print("HTTP Method not recognised")
    try:
        object1.read_protocol()
        data['Protocol'] = str(object1.request_protocol.value)
        print(data['Protocol'] + "\n")
        object1.read_base_url()
        object1.read_relative_url()
        try:
            data['URL'] = str(data['Protocol']) + "://" + str(object1.request_base_url.value) + str(object1.request_relative_url.value)
            print("URL "+ "\n")
            print(data['URL'])
        except:
            print("Exception in concatenating URL")
        
        object1.read_body()
        data['Body'] = json.loads(object1.body_row)
        print("Fdata Body")
        print(data['Body'])
        object1.read_header()
        data['Header'] = json.loads(object1.header_row)
        print(data['Header'])
        object1.read_cookie() 
        data['Cookie'] = json.loads(object1.cookie_row)
        print(data['Cookie'])
        print(data)
    except:
        print("Exception in reading contents")

    return data

