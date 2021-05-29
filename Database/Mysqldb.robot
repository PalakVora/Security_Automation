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

   ${output} =    Execute SQL String    CREATE TABLE foritfy (id integer unique,first_name varchar(20),last_name varchar(20));
   Log    ${output}
   Should Be Equal As Strings    ${output}    None

TC2
   log to console  "Performing SQL Injection Attack on ITS-ITGue"
   @{output} =    Query    SELECT * FROM exceldetails LIMIT 1;
   Log    @{output}
   ${Excel_Location} =    Set Variable    ${output[0][0]}
   ${API_Excel_Sheet_Name} =    Set Variable    ${output[0][1]}
   ${API_Module_Name} =    Set Variable    ${output[0][2]}
   ${Payload_Excel_Location} =    Set Variable    ${output[0][3]}
   ${Payload_Sheet_Name} =    Set Variable    ${output[0][4]}
   Injection Attack  ${Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
   
