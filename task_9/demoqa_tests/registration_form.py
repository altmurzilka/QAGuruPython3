from task_9.demoqa_tests import resource
from selene import have, command
from selene.support.shared import browser

from task_9.demoqa_tests.users import User


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
    #     browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
    #         have.size_greater_than_or_equal(3)
    #     )
    #     browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_form(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[name=gender][value={user.gender}]+label').click()
        browser.element('#userNumber').type(user.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(f'.react-datepicker__day--0{user.day}').click()

        for subject in user.subjects:
            browser.element('#subjectsInput').type(subject.value).press_enter()

        for hobby in user.hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby.value)).click()

        browser.element('#uploadPicture').send_keys(resource.path(user.picture))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()
        return self

    def assert_user_info(self, user: User):
        full_name = f'{user.first_name} {user.last_name}'
        birthday = f'{user.day} {user.month},{user.year}'
        state_and_city = f'{user.state} {user.city}'
        subject = ','.join([subject.value for subject in user.subjects])
        hobby = ','.join([hobby.value for hobby in user.hobbies])
        browser.element('.table').all('td').should(have.texts(
            ('Student Name', f'{full_name}'),
            ('Student Email', f'{user.email}'),
            ('Gender', f'{user.gender}'),
            ('Mobile', f'{user.mobile}'),
            ('Date of Birth', f'{birthday}'),
            ('Subjects', f'{subject}'),
            ('Hobbies', f'{hobby}'),
            ('Picture', f'{user.picture}.jpeg'),
            ('Address', f'{user.address}'),
            ('State and City', f'{state_and_city}')))
        return self
