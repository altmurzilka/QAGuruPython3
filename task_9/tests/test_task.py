from task_9.demoqa_tests.registration_form import RegistrationPage


def test_submit_form():
    registration_page = RegistrationPage()

    # WHEN
    registration_page
    registration_page \
        .fill_first_name('Altyn') \
        .fill_last_name('Myrzakulova') \
        .fill_email('test@gmail.com') \
        .choose_gender() \
        .fill_mobile_number('9999999999') \
        .fill_date_of_birth('July', '1995', '12') \
        .fill_subject('Biology') \
        .choose_hobbies() \
        .select_picture('ditto') \
        .fill_address('Almaty') \
        .choose_state_and_city('NCR', 'Noida') \
        .submit()

    # THEN
    registration_page.assert_user_info(
        'Altyn',
        'Myrzakulova',
        'test@gmail.com',
        'Female',
        '9999999999',
        '12 July,1995',
        'Biology',
        'Reading',
        'ditto',
        'Almaty',
        'NCR Noida'
    )
