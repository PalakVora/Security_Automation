import requests, traceback, json

verifyssl=True

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
            print("abc")
            print(self.result)
            print("cde")
            print(self.hitrequest)
        except Exception as error:
            print(error)
            traceback.print_stack()
    
    def hit_get(self,url,body,header,cookie):
        print("Its GET API")
        self.hitrequest = requests.get(url, data=body, headers=header,cookies=cookie, verify=verifyssl)
        print(type(self.hitrequest.elapsed.total_seconds()))
        self.response_time=self.hitrequest.elapsed.total_seconds()
        print("Executed GET Method for payload")
        self.set_result()
        return self.hitrequest , self.result, self. response_time

    def hit_post(self,url,body,header,cookie):
        print("Its POST API")
        self.hitrequest = requests.post(url, data=body, headers=header,cookies=cookie, verify=verifyssl)
        self.response_time=self.hitrequest.elapsed.total_seconds()
        print("Executed POST Method for payload")
        self.set_result()
        return self.hitrequest , self.result , self.response_time

    def hit_put(self,url,body,header,cookie):
        print("Its PUT API")
        self.hitrequest = requests.put(url, data=body, headers=header,cookies=cookie, verify=verifyssl)
        print("Executed POST Method for payload")
        self.set_result()
        return self.hitrequest , self.result

    def hit_delete(self,url,body,header,cookie):
        print("Its DELETE API")
        self.hitrequest = requests.delete(url, data=body, headers=header,cookies=cookie, verify=verifyssl)
        print("Executed DELETE Method for payload")
        self.set_result()
        return self.hitrequest , self.result
