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
        self.payload_replace=[]

    def make_url(self):
        
        try:
            self.raw_url = self.raw_protocol + "://" + self.base_url + self.relative_url
        except:
            print("Exception in concatenating URL")


    def replace_dollar(self):
        payload_param=[]
        try:
            check_url = re.findall(r'\$(.*?)\$', str(self.raw_url))
            if check_url != []:
                self.payload_replace = check_url
                for key in check_url:
                    self.url = self.raw_url.replace("$","")
                payload_param = ["URL"]
            else:
                self.url=self.raw_url
        except Exception as error:
            print(error)
            traceback.print_stack()
        try:
            check_body = re.findall(r'\$(.*?)\$', str(self.raw_request_body))
            if check_body != []:
                if self.payload_replace== []:
                    self.payload_replace = check_body
                else:
                    self.payload_replace.extend(check_body)

                for key in check_body:
                    self.request_body = str(self.raw_request_body).replace("$", "")
               
                if not payload_param:
                    payload_param = ["Body"]
                else:
                    payload_param.append("Body")  
            else:
                self.request_body=self.raw_request_body
                
        except Exception as error:
            print(error)
            traceback.print_stack()
        try:
            check_header = re.findall(r'\$(.*?)\$', str(self.raw_header))
            if check_header != []:
                if self.payload_replace==[]:
                    self.payload_replace = check_header
                else:
                    self.payload_replace.extend(check_header)
                for key in check_header:
                    self.header = self.raw_header.replace("$", "")
                if not payload_param:
                    payload_param = ["Header"]
                else:
                    payload_param.append("Header")
            else:
                self.header=self.raw_header
        except Exception as error:
            print(error)
            traceback.print_stack()

        try:
            check_cookie = re.findall(r'\$(.*?)\$', str(self.raw_cookies))
            if check_cookie != []:
                if self.payload_replace==[]:
                    self.payload_replace = check_cookie
                else:
                    self.payload_replace.extend(check_cookie)
                for key in check_cookie:
                    self.cookies = self.raw_cookies.replace("$", "")
                if not payload_param:
                    payload_param = ["Cookie"]
                else:
                    payload_param.append("Cookie")
            else:
                self.cookies=self.raw_cookies
        except Exception as error:
            print(error)
            traceback.print_stack()
        
        try:
            check_method = re.findall(r'\$(.*?)\$', str(self.raw_http_method))
            if check_method != []:
                for key in check_method:
                    self.http_method = self.raw_http_method.replace("$","")
                payload_param = ["METHOD"]
            else:
                self.http_method=self.raw_http_method
        except Exception as error:
            print(error)
            traceback.print_stack()
        
        try:
            check_protocol = re.findall(r'\$(.*?)\$', str(self.raw_protocol))
            if check_protocol != []:
                for key in check_protocol:
                    self.protocol = self.raw_protocol.replace("$","")
                payload_param = ["PROTOCOL"]
            else:
                self.protocol=self.raw_protocol
        except Exception as error:
            print(error)
            traceback.print_stack()
        return self.payload_replace , payload_param
