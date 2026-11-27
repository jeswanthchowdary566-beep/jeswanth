*** Settings ***
Library    RequestsLibrary
Library    Collections
 
*** Variables ***
${BASE_URL}     http://127.0.0.1:5000

*** Keywords ***
Create API Session
    Create Session       Equipment_API      ${BASE_URL}
Get All Equipment
    ${response}=       GET On Session      Equipment_API       /api/equipment      expected_status=200
    RETURN      ${response}
Get Equipment by id
    [Arguments]     ${equipment_id}     ${expected_status}
    ${response}=       GET On Session      Equipment_API       /api/equipment      expected_status=${expected_status} 
    RETURN      ${response}  