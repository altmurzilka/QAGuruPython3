import os
from selene import have, command
from selene.support.shared import browser


def test_submit_form():
    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Altyn')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element('[name=gender][value=Female]+label').click()
    browser.element('#userNumber').type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type("July")
    browser.element('.react-datepicker__year-select').type("1995")
    browser.element('.react-datepicker__day--012').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '/image/ditto.jpeg')))
    browser.element('#currentAddress').type('Almaty')
    browser.element("#state").perform(command.js.scroll_into_view)

    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()

    browser.element('#submit').press_enter()

    browser.element('.table').all('td').should(have.texts(
        ('Student Name', 'Test Altyn'),
        ('Student Email', 'test@gmail.com'),
        ('Gender', 'Female'),
        ('Mobile', '9999999999'),
        ('Date of Birth', '12 July,1995'),
        ('Subjects', 'Biology'),
        ('Hobbies', 'Reading'),
        ('Picture', 'ditto.jpeg'),
        ('Address', 'Almaty'),
        ('State and City', 'NCR Noida')))
