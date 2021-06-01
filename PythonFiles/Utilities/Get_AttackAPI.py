import json

class setAPI:
    def __init__(self):
        self.api_name=""
        self.http_method=""
        self.protocol=""
        self.base_url=""
        self.relative_url=""
        self.request_body=""
        self.header=""
        self.cookies=""
    def find_api(self):
        data = {}
        try:
            data['API'] = self.api_name
            print("API is")
            print(data['API'])
            data['HTTPMethod'] =self.http_method
            print(data['HTTPMethod'])
            print("OUtside method")
        except Exception as exception:
            print("HTTP Method not recognised")
        try:
            data['Protocol'] = self.protocol
            print(data['Protocol'] + "\n")
            data['URL'] = self.protocol + "://" + self.base_url + self.relative_url
            print("URL "+ "\n")
            print(data['URL'])
        except:
            print("Exception in concatenating URL")
        try:    
            data['Body'] = json.loads(self.request_body)
            print("Fdata Body")
            print(data['Body'])
            data['Header'] = json.loads(self.header)
            print(data['Header'])
            data['Cookie'] = json.loads(self.cookies)
            print(data['Cookie'])
            print(data)
        except:
            print("Exception in reading contents")
        return data
