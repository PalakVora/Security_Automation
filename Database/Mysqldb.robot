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
   log to console  "Performing SQL Injection Attack on ITS-ITGue"
   @{output} =    Query    SELECT * FROM apidetails LIMIT 1;
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
   