*** Settings ***
Variables  ../DataFiles/variables.py
Suite Setup       Connect To Database    pymysql    ${dbname}    ${dbuser}    ${dbpass}    ${dbhost}    ${dbport}
Test Setup    Hit apidetails
*** Keywords ***
Hit API
    [Arguments]  ${Api_to_run}
    