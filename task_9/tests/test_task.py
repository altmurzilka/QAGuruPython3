from task_9.demoqa_tests.registration_form import RegistrationPage
from task_9.demoqa_tests.users import Hobby, Gender, User, Subject


def test_submit_form(browser_management):
    registration_page = RegistrationPage()

    user = User(
        first_name='Altyn',
        last_name='Myrzakulova',
        email='test@gmail.com',
        gender=Gender.female.value,
        mobile='9999999999',
        day='12',
        month='July',
        year='1995',
        subjects=[Subject.biology],
        hobbies=[Hobby.reading],
        picture='ditto',
        address='Almaty',
        state='NCR',
        city='Noida'
    )

    registration_page.open()

    # WHEN
    registration_page.fill_form(user)

    # THEN
    registration_page.assert_user_info(user)
