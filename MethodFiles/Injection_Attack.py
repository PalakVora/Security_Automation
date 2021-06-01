import requests, openpyxl,json, re, traceback, logging
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'PythonFiles/Utilities')

import Get_AttackAPI

#Excel_Location =  "D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx"
#Excel_Sheet_Name = "ITSM"  
#Module_Name = "TestAPIDefend"
#attack_payload_sheetname = "SQL"
keyword_payload = ['union','group']
keyword_internal_server_error = "Internal Server Error"
keyword_injection_hint = "select"
#payload_excel_location = "D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx"



# ****************************** SQL INJECTION CONDITIONS ************************************

def check_for_errors(after_hit,keyword_internal_server_error,check_body,original_response):

#================================== API didn't respond to injection =============================================
    if after_hit.status_code == 200:
        print("The functionality didn't respond")
        check_body=check_body.lower()
        search_sql_query = check_body.index(keyword_injection_hint)
        if(search_sql_query):
            print("Query found")
            print(check_body[search_sql_query:search_sql_query+35])
        else:
            print(search_sql_query)
    else:
        print("The functionality responded")

#================================== Internal server Error =============================================
    search_server_error = re.search(keyword_internal_server_error,check_body)
    if after_hit.status_code == 500:
        print("SQL Injection found")
        #raise ApiError('GET /tasks/ {}'.format(after_hit.status_code))
    else:
        print("Your status code" + str(after_hit.status_code))
        if (search_server_error):
            print("SQL Injection found")
        else :
            print("Safe from this use case")
    
 #================================== Loading blank page =============================================   
    if original_response['ResponseBody'] and original_response['ResponseBody'] != ' ' and original_response['ResponseBody'] != '{}':
        if (not check_body) or (check_body == ' ') :
            print("A blank page loaded")
    elif ( not original_response['ResponseBody']) or (original_response['ResponseBody'] == ' ') or (original_response['ResponseBody'] == '{}') :
        print("The original was blank itself")



# ****************************** HIT API AND GET RESPONSE WITH PAYLOAD ************************************  
           
def hit_it(Method,URL,Body,Header,Cookie):
    result={}
    if(Method == 'GET'):
        print("Its GET API")
        try:
            GET = requests.get(URL, data=Body, headers=Header,cookies=Cookie)
            print("Executed GET Method for payload")
            result['StatusCode'] = str(GET.status_code)
            result['ResponseBody'] = str(GET.text)
            result['ResponseHeader'] = str(GET.headers)
            result['ResponseCookie'] = str(GET.cookies)
            print(result)
            return GET,result
        except Exception as error:
            print(error)
            traceback.print_stack()
    elif (Method == 'POST'):
        print("Found POST API, So Executing It.")
        try:
            POST = requests.post(URL, data=Body, headers=Header, cookies=Cookie)
            print("Executed POST Method")
            result['StatusCode'] = str(POST.status_code)
            result['ResponseBody'] = str(POST.text)
            result['ResponseHeader'] = str(POST.headers)
            result['ResponseCookie'] = str(POST.cookies)
            print("Got it")
            print(result)
            return POST , result
        except Exception as error:
            print(error)
            traceback.print_stack()


# ****************************** LOAD PAYLOAD SHEET AND MODIFY ATTACK AREA ************************************     
   
def attack_it(Method,attack_position,attack_area,Body,Header,Cookie,result,payload_excel_location,attack_payload_sheetname):
    print("Something up")
    payload_excel_workbook_location=openpyxl.load_workbook(payload_excel_location)
    replace_this = ""
    for key in attack_position:
        replace_this = key
    for payload_sheetname in payload_excel_workbook_location.worksheets:
        if payload_sheetname.title == attack_payload_sheetname:
            print("Worksheet Found = " + payload_sheetname.title)
            payload_activeworksheet = payload_excel_workbook_location[payload_sheetname.title]
            print("Title of Sheet = " + payload_activeworksheet.title)
            payload_rowlength = payload_sheetname.max_row
            print("Number of Payloads for " + str(payload_sheetname.title) + " = " + str(payload_rowlength - 1))
            for i in range(2, payload_rowlength + 1):
                payload_rowcontents = payload_sheetname.cell(row=i, column=1)
                print("Shhetname" + str(payload_sheetname))
                print("Row " + str(payload_rowcontents.row - 1) + " = " + str(payload_rowcontents.value), end="" + "\n")
                #=============================== Replace ==================
                loaded_payload_replace = attack_area.replace(replace_this, "'")
                loaded_payload_replace = loaded_payload_replace.replace("$","")
                print("loaded param")
                print(loaded_payload_replace)
                after_hit, after_hit_result = hit_it(Method,loaded_payload_replace,Body,Header,Cookie)
                check_for_errors(after_hit,keyword_internal_server_error,after_hit.text,result)
                #=================================== Append with union/group ============================
                keep_variable = str(payload_rowcontents.value)
                keep_variable=keep_variable.lower()
                
                if any(x in keep_variable for x in keyword_payload) : 
                    loaded_payload_append_space = attack_area + ' ' + str(payload_rowcontents.value)
                    loaded_payload_append_space = loaded_payload_append_space.replace("$","")
                    print ("WE have a URL with UNION***********************************")
                    print(loaded_payload_append_space)
                    after_hit, after_hit_result = hit_it(Method,loaded_payload_append_space,Body,Header,Cookie)
                    check_for_errors(after_hit,keyword_internal_server_error,after_hit.text,result)
                    #=================================== Append ============================
                else:
                    loaded_payload_append = attack_area +  str(payload_rowcontents.value)
                    loaded_payload_append = loaded_payload_append.replace("$","")
                    print ("WE have a URL ***********************************")
                    print(loaded_payload_append)
                    after_hit, after_hit_result = hit_it(Method,loaded_payload_append,Body,Header,Cookie)
                    check_for_errors(after_hit,keyword_internal_server_error,after_hit.text,result)
                    #=================================== Append with space ============================
                    loaded_payload_space = attack_area +  ' ' + str(payload_rowcontents.value)
                    loaded_payload_space = loaded_payload_space.replace("$","")
                    print ("WE have a URL with space ***********************************")
                    print(loaded_payload_space)
                    after_hit, after_hit_result = hit_it(Method,loaded_payload_space,Body,Header,Cookie)
                    check_for_errors(after_hit,keyword_internal_server_error,after_hit.text,result)
                
                print("=======after hit")
                print(after_hit_result['ResponseBody'])
    #return loaded_payload_replace        


# ****************************** IDENTIFY ATTACK AREA, HIT CORRECT REQUEST, CALL FOR SQL INJECTION ************************************

def API_wert(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies,payload_excel_location,attack_payload_sheetname):
    result = {}
    payload_param = []
    try:
        # Get API into variables
        returnvalue = Get_AttackAPI.find_api(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies)
        
        print("Data from Excel")
        print(returnvalue)
    except Exception as error:
        print(error)
        traceback.print_stack()
    
    try:
        API = returnvalue['API']
        
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Method = returnvalue['HTTPMethod']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Protocol = returnvalue['Protocol']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        URL = returnvalue['URL']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Body = returnvalue['Body']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Header = returnvalue['Header']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Cookie = returnvalue['Cookie']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_URL = re.findall(r'\$(.*?)\$', str(URL))
        if Check_URL != []:
            for key in Check_URL:
                new_url = URL.replace("$","")
            print(new_url)
            payload_param = ["URL"]
            print(payload_param)
        else:
            print("No Change in URL")
    except Exception as error:
            print(error)
            traceback.print_stack()

    try:
        Check_Body = re.findall(r'\$(.*?)\$', str(Body))
        if Check_Body != []:
            for key in Check_Body:
                Body = Body.replace("$", "")
            print(Body)
            if not payload_param:
                payload_param = ["Body"]
            else:
                payload_param.append("Body")
            print(payload_param)
        else:
            print("No Change in Body")
            print(Body)
    except Exception as error:
        print(error)
        traceback.print_stack()


    try:
        Check_Header = re.findall(r'\$(.*?)\$', str(Header))
        if Check_Header != []:
            for key in Check_Header:
                Header = Header.replace("$", "")
            print(Header)
            if not payload_param:
                payload_param = ["Header"]
            else:
                payload_param.append("Header")
            print(payload_param)
        else:
            print("No Change in Header")
            print(Header)
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_Cookie = re.findall(r'\$(.*?)\$', str(Cookie))
        if Check_Cookie != []:
            for key in Check_Cookie:
                Cookie = Cookie.replace("$", "")
            print(Cookie)
            if not payload_param:
                payload_param = ["Cookie"]
            else:
                payload_param.append("Cookie")
            print(payload_param)
        else:
            print("No Change in Cookie")
            print(Cookie)
    except Exception as error:
        print(error)
        traceback.print_stack()

    
    try:
        if(Method == 'GET'):
            print("Found GET API, So Executing It.")
            try:
                GET = requests.get(new_url, data=Body, headers=Header,cookies=Cookie)
                print("Executed GET Method")
                result['StatusCode'] = str(GET.status_code)
                result['ResponseBody'] = str(GET.text)
                result['ResponseHeader'] = str(GET.headers)
                result['ResponseCookie'] = str(GET.cookies)
                print(result)
                
               # stripped = re.search('Ja',GET.text)
                #print(result['StatusCode'])
                #if (stripped):
                 #   print("SQL Injection found")
                #else :
                #    print("Safe from this use case")
                for i in payload_param:
                    if i == "URL":
                        print("inside for")
                        attack_it(Method,Check_URL,URL,Body,Header,Cookie,result,payload_excel_location,attack_payload_sheetname)
            except Exception as error:
                print(error)
                traceback.print_stack()
                
                        
                    
        elif (Method == 'POST'):
            print("Found POST API, So Executing It.")
            try:
                print("The url")
                print(type(Cookie))
                POST = requests.post(new_url, data=Body, headers=Header, cookies=Cookie)
                print("Executed POST Method")
                result['StatusCode'] = str(POST.status_code)
                result['ResponseBody'] = str(POST.text)
                result['ResponseHeader'] = str(POST.headers)
                result['ResponseCookie'] = str(POST.cookies)
                print("Got it before")
                print(result)
                for i in payload_param:
                    if i == "URL":
                        print("inside for")
                        attack_it(Method,Check_URL,URL,Body,Header,Cookie,result,payload_excel_location,attack_payload_sheetname)
            except Exception as error:
                print(error)
                traceback.print_stack()
        elif(Method == 'PUT'):
            print("Found PUT API, So Executing It.")
            try:
                PUT = requests.put(URL, data=Body, headers=Header)
                print("Executed POST Method")
                result['StatusCode'] = str(PUT.status_code)
                result['ResponseBody'] = str(PUT.text)
                result['ResponseHeader'] = str(PUT.headers)
                result['ResponseCookie'] = str(PUT.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()
        elif(Method == 'DELETE'):
            print("Found DELETE API, So Executing It.")
            try:
                DELETE = requests.put(URL, data=Body, headers=Header)
                print("Executed POST Method")
                result['StatusCode'] = str(DELETE.status_code)
                result['ResponseBody'] = str(DELETE.text)
                result['ResponseHeader'] = str(DELETE.headers)
                result['ResponseCookie'] = str(DELETE.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()
    except Exception as error:
        print(error)
        traceback.print_stack()
    return result


"""
if __name__ == "__main__":
    API_wert(Excel_Location, Excel_Sheet_Name, Module_Name,payload_excel_location,attack_payload_sheetname)

    try:
        print("Executing PDF")
        pdf = FPDF()
        print("Adding Page")
        pdf.add_page()
        pdf.set_margins(5, 5 , 5)
        print("Setting Font")
        pdf.set_font("Cambria", size=5)
        print("Setting Page Title")
        pdf.cell(200, 10, txt="COE SECURITY TEST REPORT", ln=2, align='C')


        print("Setting Second Line")
        pdf.cell(100, 5, txt='Status Code: ' + str(URL), ln=2, align='A')
        pdf.cell(100, 5, txt='Status Code: ' + result['StatusCode'], ln=1, align='A')
        print("Converting as Output")
        pdf.output("COE - Security Scan Report - " + API+".pdf")

    except Exception as error:
        print(error)
        traceback.print_stack()




        def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
        data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except Exception as error:
        print("Error in opening API Excel File")
        traceback.print_stack()

    try:
        for SheetName in Excel_WorkBook.worksheets:
            if SheetName.title == Excel_Sheet_Name:
                ActiveWorkSheet = Excel_WorkBook[SheetName.title]
                print("Title of Sheet = " + ActiveWorkSheet.title)
                RowLength = SheetName.max_row
                ColumnLength = SheetName.max_column
                for i in range(1, RowLength + 1):
                    RowContents = SheetName.cell(row=i, column=1)
                    print("Row " + str(RowContents.row) + " = " + str(RowContents.value))
                    if ((RowContents.value) == Module_Name):
                        print("Module Found : " + str(RowContents.value) + " in Row - " + str(
                            RowContents.row) + " of Worksheet - " + ActiveWorkSheet.title)
                    else:
                        continue

                    for j in range(1, ColumnLength + 1):
                        Response = dict()
                        ColumnContents = SheetName.cell(row=RowContents.row, column=j)
                        print(ColumnContents.value, end="" + "\n")

                        try:
                            API_Name = (SheetName["A" + str(RowContents.row)])
                            print(API_Name.value)
                            data['API'] = str(API_Name.value)
                            print(data['API'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            HTTP_Method = (SheetName["B" + str(RowContents.row)])
                            print(HTTP_Method.value)
                            data['HTTPMethod'] = str(HTTP_Method.value)
                            print(data['HTTPMethod'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_Protocol = (SheetName["C" + str(RowContents.row)])
                            print(Request_Protocol.value)
                            data['Protocol'] = str(Request_Protocol.value)
                            print(data['Protocol'] + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_BaseURL = (SheetName["D" + str(RowContents.row)])
                            print("BaseURL = " + str(Request_BaseURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_RelativeURL = (SheetName["E" + str(RowContents.row)])
                            print("RelativeURL = " + str(Request_RelativeURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['URL'] = str(data['Protocol']) + "://" + str(Request_BaseURL.value) + str(Request_RelativeURL.value)
                            print(data['URL'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Body_Row = (SheetName["F" + str(RowContents.row)])
                            Body_Content = str(Body_Row.value)
                            print("Body = " + Body_Content + "\n")
                            data['Body'] = json.loads(Body_Content)
                            print(data['Body'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Header_Row = (SheetName["G" + str(RowContents.row)])
                            Header_Content = str(Header_Row.value)
                            print("Header = " + Header_Content + "\n")
                            data['Header'] = json.loads(Header_Content)
                            print(data['Header'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Cookie_Row = (SheetName["H" + str(RowContents.row)])
                            Cookie_Content = str(Cookie_Row.value)
                            print("Cookie = " + Cookie_Content + "\n")
                            data['Cookie'] = json.loads(Cookie_Content)
                            print(data['Cookie'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break
                        break
                    break
                    print(data)
                    Excel_WorkBook.close()

    except:
        print("Error in reading contents")
    return data
"""