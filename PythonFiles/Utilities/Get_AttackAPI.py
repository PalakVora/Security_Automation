import json,re

class setAPI:
    def __init__(self):
        self.api_name=""
        self.http_method=""
        self.raw_http_method=""
        self.protocol=""
        self.raw_protocol=""
        self.base_url=""
        self.relative_url=""
        self.request_body=""
        self.raw_request_body=""
        self.header=""
        self.raw_header=""
        self.cookies=""
        self.raw_cookies=""
        self.url=""
        self.raw_url=""

    def make_url(self):
        
        try:
            self.raw_url = self.raw_protocol + "://" + self.base_url + self.relative_url
            print(self.url)
        except:
            print("Exception in concatenating URL")


    def replace_dollar(self):
        try:
            check_url = re.findall(r'\$(.*?)\$', str(self.raw_url))
            if check_url != []:
                for key in check_url:
                    self.url = self.raw_url.replace("$","")
                print(self.url)
                payload_param = ["URL"]
                #print(payload_param)
            else:
                print("No Change in URL")
                self.url=self.raw_url
        except Exception as error:
            print(error)
            traceback.print_stack()
        try:
            check_body = re.findall(r'\$(.*?)\$', str(self.raw_request_body))
            if check_body != []:
                for key in check_body:
                    self.request_body = self.raw_request_body.replace("$", "")
                print(self.request_body)
                if not payload_param:
                    payload_param = ["Body"]
                else:
                    payload_param.append("Body")
                print(payload_param)
            else:
                print("No Change in Body")
                self.request_body=self.raw_request_body
                print(self.request_body)
        except Exception as error:
            print(error)
            traceback.print_stack()
        try:
            check_header = re.findall(r'\$(.*?)\$', str(self.raw_header))
            if check_header != []:
                for key in check_header:
                    self.header = self.raw_header.replace("$", "")
                print(self.header)
                if not payload_param:
                    payload_param = ["Header"]
                else:
                    payload_param.append("Header")
                print(payload_param)
            else:
                print("No Change in Header")
                self.header=self.raw_header
                print(self.header)
        except Exception as error:
            print(error)
            traceback.print_stack()

        try:
            check_cookie = re.findall(r'\$(.*?)\$', str(self.raw_cookies))
            if check_cookie != []:
                for key in check_cookie:
                    self.cookies = self.raw_cookies.replace("$", "")
                print(self.cookies)
                if not payload_param:
                    payload_param = ["Cookie"]
                else:
                    payload_param.append("Cookie")
                print(payload_param)
            else:
                print("No Change in Cookie")
                self.cookies=self.raw_cookies
                print(self.cookies)
        except Exception as error:
            print(error)
            traceback.print_stack()
        
        try:
            check_method = re.findall(r'\$(.*?)\$', str(self.raw_http_method))
            if check_method != []:
                for key in check_method:
                    self.http_method = self.raw_http_method.replace("$","")
                print(self.http_method)
                payload_param = ["METHOD"]
                #print(payload_param)
            else:
                print("No Change in Method")
                self.http_method=self.raw_http_method
        except Exception as error:
            print(error)
            traceback.print_stack()
        
        try:
            check_protocol = re.findall(r'\$(.*?)\$', str(self.raw_protocol))
            if check_protocol != []:
                for key in check_protocol:
                    self.protocol = self.raw_protocol.replace("$","")
                print(self.protocol)
                payload_param = ["PROTOCOL"]
                #print(payload_param)
            else:
                print("No Change in PROTOCOL")
                self.protocol=self.raw_protocol
        except Exception as error:
            print(error)
            traceback.print_stack()
        return check_url , payload_param
