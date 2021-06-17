import requests, traceback, json
verifyssl=True

class requestQuery:
    def __init__(self):
        self.method=""
        self.url=""
        self.body=""
        self.header=""
        self.cookie=""
        #self.hitrequest=""
        #self.result=""

    def hit_it(self):
        result={}
        if(self.method == 'GET'):
            print("Its GET API")
            try:
                hitrequest = requests.get(self.url, data=self.body, headers=self.header,cookies=self.cookie, verify=verifyssl)
                print("Executed GET Method for payload")
                result['StatusCode'] = str(hitrequest.status_code)
                result['ResponseBody'] = str(hitrequest.text)
                result['ResponseHeader'] = str(hitrequest.headers)
                result['ResponseCookie'] = str(hitrequest.cookies)
                print("abc")
                print(result)
                print("cde")
                print(hitrequest)
            except Exception as error:
                print(error)
                traceback.print_stack()
            return hitrequest,result
        elif (Method == 'POST'):
            print("Found POST API, So Executing It.")
            try:
                hitrequest = requests.post(self.url, data=self.body, headers=self.header,cookies=self.cookie)
                print("Executed POST Method")
                result['StatusCode'] = str(hitrequest.status_code)
                result['ResponseBody'] = str(hitrequest.text)
                result['ResponseHeader'] = str(hitrequest.headers)
                result['ResponseCookie'] = str(hitrequest.cookies)
                print("Got it")
                print(result)
                return hitrequest , result
            except Exception as error:
                print(error)
                traceback.print_stack()
        elif(Method == 'PUT'):
            print("Found PUT API, So Executing It.")
            try:
                hitrequest = requests.put(self.url, data=self.body, headers=self.header,cookies=self.cookie)
                print("Executed POST Method")
                result['StatusCode'] = str(hitrequest.status_code)
                result['ResponseBody'] = str(hitrequest.text)
                result['ResponseHeader'] = str(hitrequest.headers)
                result['ResponseCookie'] = str(hitrequest.cookies)
                return hitrequest , result
            except Exception as error:
                print(error)
                traceback.print_stack()
        elif(Method == 'DELETE'):
            print("Found DELETE API, So Executing It.")
            try:
                hitrequest = requests.delete(self.url, data=self.body, headers=self.header,cookies=self.cookie)
                print("Executed POST Method")
                result['StatusCode'] = str(hitrequest.status_code)
                result['ResponseBody'] = str(hitrequest.text)
                result['ResponseHeader'] = str(hitrequest.headers)
                result['ResponseCookie'] = str(hitrequest.cookies)
                return hitrequest , result
            except Exception as error:
                print(error)
                traceback.print_stack()
        
