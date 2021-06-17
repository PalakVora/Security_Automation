import requests, openpyxl,json, re, traceback, logging
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'PythonFiles/Utilities')

from Get_AttackAPI import setAPI
from Request_File import requestQuery
from Check_condition import injectionCondition
keyword_payload = ["union","group"]
keyword_internal_server_error = "Internal Server Error"
keyword_injection_hint = ["select ","show "," top "," distinct "," from "," from dual"," where "," group by "," order by "," having "," limit "," offset "," union all "," rownum as ","(case "]

# ****************************** SQL INJECTION CONDITIONS ************************************
def condition_check(after_hit,keyword_internal_server_error,body_text,result):
    object1=injectionCondition()
    object1.after_hit=after_hit
    object1.keyword_internal_server_error=keyword_internal_server_error
    object1.check_body=body_text
    object1.original_response=result
    object1.check_for_errors()


# ****************************** HIT API AND GET RESPONSE WITH PAYLOAD ************************************  
           

def hit_request(method,new_url,body,header,cookie):
    try:
        Object1=requestQuery()
        Object1.method=method
        Object1.url=new_url
        Object1.body=body
        Object1.header=header
        Object1.cookie=cookie
        hitreq,res=Object1.hit_it()
        return hitreq, res
    except:
        print("Failed to hit request")


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
                loaded_payload_replace = attack_area.replace(replace_this, str(payload_rowcontents.value))
                loaded_payload_replace = loaded_payload_replace.replace("$","")
                print("loaded param")
                print(loaded_payload_replace)
                after_hit, after_hit_result = hit_request(Method,loaded_payload_replace,Body,Header,Cookie)
                print("out")
                condition_check(after_hit,keyword_internal_server_error,after_hit.text,result)
                #=================================== Append with union/group ============================
                keep_variable = str(payload_rowcontents.value)
                keep_variable=keep_variable.lower()
                
                if any(x in keep_variable for x in keyword_payload) : 
                    loaded_payload_append_space = attack_area + ' ' + str(payload_rowcontents.value)
                    loaded_payload_append_space = loaded_payload_append_space.replace("$","")
                    print ("WE have a URL with UNION***********************************")
                    print(loaded_payload_append_space)
                    after_hit, after_hit_result = hit_request(Method,loaded_payload_append_space,Body,Header,Cookie)
                    condition_check(after_hit,keyword_internal_server_error,after_hit.text,result)
                    #=================================== Append ============================
                else:
                    loaded_payload_append = attack_area +  str(payload_rowcontents.value)
                    loaded_payload_append = loaded_payload_append.replace("$","")
                    print ("WE have a URL ***********************************")
                    print(loaded_payload_append)
                    after_hit, after_hit_result = hit_request(Method,loaded_payload_append,Body,Header,Cookie)
                    condition_check(after_hit,keyword_internal_server_error,after_hit.text,result)
                    #=================================== Append with space ============================
                    loaded_payload_space = attack_area +  ' ' + str(payload_rowcontents.value)
                    loaded_payload_space = loaded_payload_space.replace("$","")
                    print ("WE have a URL with space ***********************************")
                    print(loaded_payload_space)
                    after_hit, after_hit_result = hit_request(Method,loaded_payload_space,Body,Header,Cookie)
                    condition_check(after_hit,keyword_internal_server_error,after_hit.text,result)
                
                print("=======after hit")
                print(after_hit_result['ResponseBody'])
    #return loaded_payload_replace        


# ****************************** IDENTIFY ATTACK AREA, HIT CORRECT REQUEST, CALL FOR SQL INJECTION ************************************

def API_wert(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies,payload_excel_location,attack_payload_sheetname):
    result = {}
    payload_param = []
    try:
        # Get API into variables
        
        object1=setAPI()
        object1.api_name=api_name
        object1.http_method=http_method
        object1.protocol=protocol
        object1.base_url=base_url
        object1.relative_url=relative_url
        object1.request_body=request_body
        object1.header=header
        object1.cookies=cookies

        returnvalue = object1.find_api()
        
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
            abc, result = hit_request("GET",new_url,Body,Header,Cookie)
            print("Why")
            print(result)
            print(abc)
            for i in payload_param:
                if i == "URL":
                    print("inside for")
                    attack_it(Method,Check_URL,URL,Body,Header,Cookie,result,payload_excel_location,attack_payload_sheetname)
                
                        
                    
        elif (Method == 'POST'):
            print("Found POST API, So Executing It.")
            print("Found GET API, So Executing It.")
            abc, result = hit_request("POST",new_url,Body,Header,Cookie)

            print(result)
            print(abc)
            for i in payload_param:
                if i == "URL":
                    print("inside for")
                    attack_it(Method,Check_URL,URL,Body,Header,Cookie,result,payload_excel_location,attack_payload_sheetname)
            
        elif(Method == 'PUT'):
            abc, result = hit_it("PUT",new_url,Body,Header,Cookie)
            print(result)
            print(abc)
        elif(Method == 'DELETE'):
            abc, result = hit_it("DELETE",new_url,Body,Header,Cookie)

            print(result)
            print(abc)
    except Exception as error:
        print(error)
        traceback.print_stack()
    return result


"""
api_name = "TestAPI"
http_method="GET"
protocol="https"
base_url="reqres.in"
relative_url="/api/users/$2$"
request_body='{"":""}'
header='{"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Connection": "keep-alive","Referer": "https://reqres.in/","Upgrade-Insecure-Requests": "1"}'
cookies='{"":""}'
payload_excel_location = "D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx"
attack_payload_sheetname = "SQL"
if __name__ == "__main__":
    ole = API_wert(api_name,http_method,protocol,base_url,relative_url,request_body,header,cookies,payload_excel_location,attack_payload_sheetname)
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