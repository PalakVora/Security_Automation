import json


def find_api(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies):
    data = {}
    try:
        data['API'] = api_name
        print("API is")
        print(data['API'])
        data['HTTPMethod'] =http_method
        print(data['HTTPMethod'])
        print("OUtside method")
    except Exception as exception:
        print("HTTP Method not recognised")
    try:
        data['Protocol'] = protocol
        print(data['Protocol'] + "\n")
        data['URL'] = protocol + "://" + base_url + relative_url
        print("URL "+ "\n")
        print(data['URL'])
    except:
        print("Exception in concatenating URL")
    try:    
        data['Body'] = json.loads(request_body)
        print("Fdata Body")
        print(data['Body'])
        data['Header'] = json.loads(header)
        print(data['Header'])
        data['Cookie'] = json.loads(cookies)
        print(data['Cookie'])
        print(data)
    except:
        print("Exception in reading contents")

    return data
if __name__ == "__main__":
    value=find_api(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies)
    print(value)
