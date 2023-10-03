from selene import browser, be, have, by, command


def test_form():
    browser.open('/automation-practice-form')
    # Name and Email
    browser.element('#firstName').should(be.blank).type('Test_name')
    browser.element('#lastName').should(be.blank).type('Test_Lastname')
    browser.element('#userEmail').should(be.blank).type('Test@test.com')

    # Choose gender +
    browser.element('[for=gender-radio-2]').click()
    # Write phone
    browser.element('#userNumber').should(be.blank).type('1234567890')
    # Calendar
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2020')).click()
    browser.element('.react-datepicker__day.react-datepicker__day--025').click()

    # Subject
    browser.element('#subjectsInput').type('Maths').press_enter()
    # Choose hobby
    browser.element('[for=hobbies-checkbox-1]').with_(timeout=4.0).click()
    # Write address
    browser.element('#currentAddress').type('Tbilisi')
    # Choose country and city
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    # Press button
    browser.element('#submit').click()

    browser.all('.modal-content').should(have.exact_texts(
        'Testname',
        'Test_Lastname',
        '1234567890',
        'Test@test.com',
        'Tbilisi'
    ))


