*** Settings ***
Library     SeleniumLibrary
 
*** Variables ***
${url}      https://www.google.com/
${browser}      Chrome
 
*** Test Cases ***
Verify Login Functionality
    Open browser    ${url}      ${browser}
    Maximize Browser Window
    Input Text      id=ti6dpd       Bangalore
    Sleep       2s