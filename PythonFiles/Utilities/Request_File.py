import requests, traceback, json, time


class requestQuery:
    def __init__(self):
        self.result={}
        self.hitrequest={}
        self.response_time=0.0


    def set_result(self):
        try:
            self.result['StatusCode'] = str(self.hitrequest.status_code)
            self.result['ResponseBody'] = str(self.hitrequest.text)
            self.result['ResponseHeader'] = str(self.hitrequest.headers)
            self.result['ResponseCookie'] = str(self.hitrequest.cookies)
        except Exception as error:
            print(error)
            traceback.print_stack()
    
    def hit_get(self,url,body,header,cookie):
        try:
            self.hitrequest = requests.get(url, data=body, headers=header,cookies=cookie, timeout=5)
        except:
            print("API HIT UNSUCCESSFUL")
        self.response_time=self.hitrequest.elapsed.total_seconds()
        self.set_result()
        return self.hitrequest , self.result, self. response_time
        
    def hit_post(self,url,body,header,cookie):
        try:
            self.hitrequest = requests.post(url, data=body, headers=header,cookies=cookie, timeout=5)
        except:
            print("API HIT UNSUCCESSFUL")
        time.sleep(3)
        self.response_time=self.hitrequest.elapsed.total_seconds()
        self.set_result()
        return self.hitrequest , self.result , self.response_time
        
    def hit_put(self,url,body,header,cookie):
        try:                
            self.hitrequest = requests.put(url, data=body, headers=header,cookies=cookie, timeout=5)
            self.set_result()
            self.response_time=self.hitrequest.elapsed.total_seconds()
            return self.hitrequest , self.result
        except requests.exceptions.HTTPError as httpErr: 
            print ("Http Error:",httpErr) 
        except requests.exceptions.ConnectionError as connErr: 
            print ("Error Connecting:",connErr) 
        except requests.exceptions.Timeout as timeOutErr: 
            print ("Timeout Error:",timeOutErr) 
        except requests.exceptions.RequestException as reqErr: 
            print ("Something Else:",reqErr)

    def hit_delete(self,url,body,header,cookie):
        try:    
            self.hitrequest = requests.delete(url, data=body, headers=header,cookies=cookie, timeout=5)
            self.set_result()
            self.response_time=self.hitrequest.elapsed.total_seconds()
            return self.hitrequest , self.result
        except requests.exceptions.HTTPError as httpErr: 
            print ("Http Error:",httpErr) 
        except requests.exceptions.ConnectionError as connErr: 
            print ("Error Connecting:",connErr) 
        except requests.exceptions.Timeout as timeOutErr: 
            print ("Timeout Error:",timeOutErr) 
        except requests.exceptions.RequestException as reqErr: 
            print ("Something Else:",reqErr)


'''
url = "https://reqres.in/api/users/2"
header = json.loads({"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Referer": "https://reqres.in/", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1"})
body=json.loads({"":""})
body=json.loads({"":""})
'''