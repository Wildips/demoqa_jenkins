import allure
from allure_commons.types import Severity
from data.users import User, Subject
from model.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя с полным набором атрибутов")

    # ARRANGE
    student = User(
        first_name='Some',
        last_name='User',
        email='some@user.io',
        gender='Male',
        mobile='8800008800',
        date_of_birth='1 September,1939',
        subject=Subject.hindi.value,
        hobbies='Sports',
        image='test.png',
        current_address='Far far away',
        state='Rajasthan',
        city='Jaipur',
    )

    registration_page.open()

    # ACTIONS
    registration_page.form_filling(student)

    # ASSERT
    registration_page.should_registered_user_with(student)
