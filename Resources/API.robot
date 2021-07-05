*** Settings ***
Library  SeleniumLibrary
Library  JSpringBotGlobal
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary
Library  requests
Library  ../MethodFiles/API_Injection.py
Library  ../MethodFiles/HTTP_Strict_Transport_Security.py
Library  ../MethodFiles/HTTP_Verb_Tampering.py
Library  ../MethodFiles/Injection_Attack.py
Library  ../MethodFiles/HOST_Header_Injection.py
Library  ../MethodFiles/Cross_Origin_Resource_Sharing.py

*** Variables ***

*** Keywords ***
Execute API
    [Arguments]  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}
    log to console  "Started API Execution"
    ${result}=  API_wert  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}
    log to console  "Executed Sucessfully"
    LIST SHOULD NOT CONTAIN VALUE  ${result}  200

HTTP Strict Transport Security
    [Arguments]  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  "Executing HTTP Strict Transport Security Check"
    ${result}=  HSTS  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  ${result}
    DICTIONARY SHOULD NOT CONTAIN VALUE  ${result}  200
    DICTIONARY SHOULD NOT CONTAIN VALUE  ${result}  201
    DICTIONARY SHOULD NOT CONTAIN VALUE  ${result}  202

Dangerous Method
    [Arguments]  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  "Executing Dangerous Methods"
    ${result}=  Dangerous_Methods  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  200
    LIST SHOULD NOT CONTAIN VALUE  ${result}  201
    LIST SHOULD NOT CONTAIN VALUE  ${result}  202

Injection Attack
    [Arguments]  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  "Executing Injection Attack"
    log to console  ${Payload_Excel_Location}
    ${result}=  API_injection  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  ${result}
    Run Keyword If  ${result}!= 0  Fail  msg=This might be vulnerable to SQL injection

    

Host Header Injection Attack
    [Arguments]  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  "Executing Host Header Injection Attack"
    log to console  ${Excel_Location}
    ${result}=  HHI  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  200
    LIST SHOULD NOT CONTAIN VALUE  ${result}  201
    LIST SHOULD NOT CONTAIN VALUE  ${result}  202
    LIST SHOULD NOT CONTAIN VALUE  ${result}  302

Cross Origin Resource Sharing
    [Arguments]  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  "Executing Cross Origin Resource Sharing"
    log to console  ${Excel_Location}
    ${result}=  CORS  ${Excel_Location}  ${Excel_Sheet_Name}  ${Module_Name}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  200
    LIST SHOULD NOT CONTAIN VALUE  ${result}  201
    LIST SHOULD NOT CONTAIN VALUE  ${result}  202
    LIST SHOULD NOT CONTAIN VALUE  ${result}  302


