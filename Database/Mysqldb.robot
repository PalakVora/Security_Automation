*** Settings ***
Library  DatabaseLibrary
Resource  ../Resources/API.robot
Variables  ../DataFiles/variables.py


*** Test Cases ***
TC2
   [Tags]  perform_injection
   log to console  "Performing SQL Injection Attack on ITS-ITGue"
   Injection Attack  ${API_Name}  ${HTTP_Method}  ${Protocol}  ${Base_URL}  ${Relative_URL}  ${Request_Body}  ${Header}  ${Cookies}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
   

  