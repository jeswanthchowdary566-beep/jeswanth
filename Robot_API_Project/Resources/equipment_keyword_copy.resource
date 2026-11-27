*** Settings ***
Library     RequestsLibrary
*** Variables ***
${BASE_URL}     http://127.0.0.1:5000
 
*** Keywords ***
Create API Session
    Create session      Equipment_API       ${BASE_URL}
GET All Equipments
    [Arguments]     ${expected_status}
    ${response}=   GET on session       Equipment_API       /api/equipment      expected_status=200
    RETURN      ${response}
Get Equipment by id
    [Arguments]    ${equipment_id}      ${expected_status}
    ${response}=        GET on session       Equipment_API       /api/equipment/${equipment_id}      expected_status=200
    RETURN      ${response}