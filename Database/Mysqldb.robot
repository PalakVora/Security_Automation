*** Settings ***
Library  DatabaseLibrary
Resource  ../Resources/API.robot
Variables  ../DataFiles/variables.py
Suite Setup       Connect To Database    pymysql    ${dbname}    ${dbuser}    ${dbpass}    ${dbhost}    ${dbport}


*** Variables ***
@{queryResults}
${API_to_run}
${API_Name}
${HTTP_Method}
${Protocol}
${Base_URL}
${Relative_URL}
${Request_Body}
${Header}
${Cookies}
${Payload_Excel_Location}
${Payload_Sheet_Name}

*** Keywords ***
Comparing
   Check If Not Exists In Database    SELECT * FROM apidetails WHERE API_Name = '${API_to_run}';
Insert API
   Execute SQL String    INSERT INTO apidetails VALUES('${API_to_run}','POST','https','defendtheweb.net','/playground/sqli2?q=$A$','{"":""}','{"Content-Type": "application/json","Connection": "keep-alive","Cookie": "PHPSESSID=84uven6il9vls9pl92anohvki0; cookies_dismissed=1"}','{"":""}','D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx','SQL');
Delete API
   Execute SQL String    DELETE FROM apidetails WHERE 0
Get API
   [Arguments]  @{output}
   ${API_Name} =    Set Variable    ${output[0][0]}
   ${HTTP_Method} =    Set Variable    ${output[0][1]}
   ${Protocol} =    Set Variable    ${output[0][2]}
   ${Base_URL} =    Set Variable    ${output[0][3]}
   ${Relative_URL} =    Set Variable    ${output[0][4]}
   ${Request_Body} =    Set Variable    ${output[0][5]}
   ${Header} =    Set Variable    ${output[0][6]}
   ${Cookies} =    Set Variable    ${output[0][7]}
   ${Payload_Excel_Location} =    Set Variable    ${output[0][8]}
   ${Payload_Sheet_Name} =    Set Variable    ${output[0][9]}
   [return]  ${API_to_run}  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}

*** Test Cases ***
TC1 Databse Connection
   [Tags]  database_connection
   ${status}  ${checking} =    Run Keyword And Ignore Error  Comparing   
   log to console  ${API_to_run}
   log to console  ${status}
   Run Keyword If  '${status}' =='PASS'  Insert API

TC2 Injection Detection
   [Tags]  perform_injection
   log to console  "Performing SQL Injection Attack on ITS-ITGue"
   @{output} =    Query    SELECT * FROM apidetails WHERE API_Name='${API_to_run}';
   Log    @{output}
   ${API_to_run}  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  Get API  @{output}
   Injection Attack  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
   

  