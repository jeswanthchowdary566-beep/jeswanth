*** Settings ***
Resource        ../Resources/equipment_keyword.resource
Suite Setup     Create API Session

*** Test Cases ***
Test Get All Equipment
    log To Console      Test1 Started
    ${response}=       Get All Equipment        
    ${data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}     200
    Length Should Be        ${data}     3
TC1_BYID
    log to Console      Test2 Started
    ${response}=       Get Equipment by id     101     200
    ${data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}    200
    Should Be Equal As Integers     ${data}[id]     101