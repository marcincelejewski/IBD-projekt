*** Settings ***
Documentation     Testowanie aplikacji na Webówke
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}    http://127.0.0.1:8000/
${BROWSER}      Chrome
${USER NAME}    testowy_ziom
${PASSWORD}     skomplikowanehaslo_123
${MAIL}         marcin@jest.fajny
${TREE NAME}    DrzewoTestowe
${MEMBER NAME}  Wojtek
${MEMBER SURNAME}   Kowalski
${MEMBER PHOTO}     C:\\Users\\marcin.DESKTOP-8O3KFDQ\\Desktop\\głupoty\\dziadek.jpg
${TREE PHOTO}   C:\\Users\\marcin.DESKTOP-8O3KFDQ\\Desktop\\głupoty\\drzewo.jpg

${MEMBER NAME2}  Kazimierz
${MEMBER SURNAME2}   Górski
${MEMBER PHOTO2}     C:\\Users\\marcin.DESKTOP-8O3KFDQ\\Desktop\\głupoty\\kat.jpg


*** Test Cases ***
#Valid Registration
#    Open Browser To Login Page
#    Go to registration
#    Input Data To Registration  ${USER NAME}  ${PASSWORD}   ${MAIL}
#    Finish Registration
#    Close Browser
#
#
#Creating Family Tree
#    Open Browser To Login Page
#    Login  ${USER NAME}  ${PASSWORD}
#    Create New Tree  ${TREE NAME}   ${TREE PHOTO}
#    Close Browser

Adding Member To Existing Empty Family Tree
    Open Browser To Login Page
    Login  ${USER NAME}  ${PASSWORD}
    Enter Tree Editing
    ${STATUS}  Run Keyword And Return Status  Element Should Be Enabled  xpath: //*[contains(text(), "Dodaj pierwszego członka rodziny")]
    Run Keyword If  ${STATUS}   Add New Family Member       ${MEMBER NAME}      ${MEMBER SURNAME}       ${MEMBER PHOTO}
    run keyword unless  ${STATUS}    Add Secound Family Member   ${MEMBER NAME2}     ${MEMBER SURNAME2}      ${MEMBER PHOTO2}

    Close Browser
    Log  Done

*** Keywords ***
Open Browser To Login Page
    Open Browser        ${LOGIN URL}    ${BROWSER}
    Title Should Be     Home

Go to registration
    Click Element        xpath: //*[contains(text(), "Rejestracja")]
    Title Should Be     Rejestracja

Finish Registration
    Click Button    xpath: //html/body/div/div/div/form/button
    ${STATUS}  Run Keyword And Return Status  Element Should Be Enabled   xpath: //html/body/div/div/div/form/div[1]/div/p/strong
    Run Keyword If  ${STATUS}     Go Back To Home Page
    Title Should Be  Logowanie

Input Data To Registration
    [Arguments]     ${username}     ${password}     ${mail}
    Input Text      id:id_username  ${username}
    Input Text      id:id_email     ${mail}
    Input Text      id:id_password1     ${password}
    Input Text      id:id_password2     ${password}

Go Back To Home Page
    Go Back
    Go Back
    Click Element  xpath://html/body/div/a[1]

Login
    [Arguments]     ${username}     ${password}
    Click Element        xpath: //*[contains(text(), "Logowanie")]
    Input Text      id:id_username  ${username}
    Input Text      id:id_password     ${password}
    Click Button    xpath: //*[contains(text(), "Zaloguj")]

Create New Tree
    [Arguments]     ${treename}     ${treeimage}
    Click Element        xpath: //*[contains(text(), "Stwórz nowe drzewo")]
    Input Text      id:id_name  ${treename}
    Choose File     id:id_photo  ${treeimage}
    Click Button    xpath: //*[contains(text(), "Stwórz drzewo")]

Enter Tree Editing
    Click Element    xpath: //html/body/div[2]/div[2]/div/div/div/div[2]/div/a


Add New Family Member
    [Arguments]     ${name}     ${surname}  ${photo}
    Click Element    xpath: //*[contains(text(), "Dodaj pierwszego członka rodziny")]
    Choose File     id:id_photo  ${photo}
    Input Text      id:id_name  ${name}
    Input Text      id:id_last_name     ${surname}
    Click Button    xpath: //*[contains(text(), "Dodaj członka rodziny")]

Add Secound Family Member
    [Arguments]     ${name}     ${surname}  ${photo}
    Click Element   xpath: //*[contains(text(), "Dzieci")]
    Click Element   xpath: //*[contains(text(), "Dodaj dziecko")]
    Choose File     id:id_photo  ${photo}
    Input Text      id:id_name  ${name}
    Input Text      id:id_last_name     ${surname}
    Click Button    xpath: //*[contains(text(), "Dodaj członka rodziny")]

