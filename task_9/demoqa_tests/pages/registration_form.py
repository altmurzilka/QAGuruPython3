from task_9.demoqa_tests.pages import resource
from selene import have, command
from selene.support.shared import browser


class RegistrationPage:
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    @property
    def choose_gender(self):
        browser.element('[name=gender][value=Female]+label').click()
        return self

    def fill_mobile_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def choose_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()
        return self

    def select_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def choose_state_and_city(self, state, city):
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def assert_user_info(self, first_name, last_name, email,
                         gender, number, birthdate,
                         subject, hobbies, picture, address, state_and_city):
        browser.element('.table').all('td').should(have.texts(
            ('Student Name', f'{first_name} {last_name}'),
            ('Student Email', f'{email}'),
            ('Gender', f'{gender}'),
            ('Mobile', f'{number}'),
            ('Date of Birth', f'{birthdate}'),
            ('Subjects', f'{subject}'),
            ('Hobbies', f'{hobbies}'),
            ('Picture', f'{picture}.jpeg'),
            ('Address', f'{address}'),
            ('State and City', f'{state_and_city}')))
        return self
