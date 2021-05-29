*** Settings ***
Library  String
Library  REST  https://reqres.in/api/users          
ssl_verify=false

Set expectations
    Expect response   { "status": { "enum": [200, 201, 204, 400] } }
    Expect response   { "seconds": { "maximum": 2} }
    
*** Test Cases ***

Get Employee
  GET  ?page=2
  Output   response body
  [Teardown]  Output  ${OUTPUTDIR}/new_user.demo.json
  Rest instances  ${OUTPUTDIR}/all.demo.json  # all the instances so far             # note the updated response schema