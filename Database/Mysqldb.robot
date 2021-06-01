*** Settings ***
Suite Setup       Connect To Database    pymysql    ${dbname}    ${dbuser}    ${dbpass}    ${dbhost}    ${dbport}
Library  DatabaseLibrary
Resource  ../Resources/API.robot

*** Variables ***
${dbname}  robot
${dbuser}  root
${dbpass}  
${dbhost}  localhost
${dbport}  3306
@{queryResults}

*** Test Cases ***
TC1
   [Tags]    db    smoke
   ${output1} =    Execute SQL String    INSERT INTO apidetails VALUES('TestAPIDefend','POST','https','defendtheweb.net','/playground/sqli2?q=$A$','{"":""}','{"Content-Type": "application/json","Connection": "keep-alive","Cookie": "PHPSESSID=84uven6il9vls9pl92anohvki0; cookies_dismissed=1"}','{"":""}','D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx','SQL');
   log to console    ${output1}
   Should Be Equal As Strings    ${output1}    None

TC2
   log to console  "Performing SQL Injection Attack on ITS-ITGue"
   @{output} =    Query    SELECT * FROM apidetails WHERE API_Name='TestAPIDefend';
   Log    @{output}
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
   Injection Attack  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
   