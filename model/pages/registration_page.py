import resource

from selene import have, command
from selene.support.shared import browser
from data.users import User
import allure


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('[id="firstName"]')
        self.last_name = browser.element('[id="lastName"]')

        self.subject = browser.element('[id="subjectsInput"]')
        ...

    @staticmethod
    def open():
        with allure.step('Открываем главную страницу'):
            browser.open('/automation-practice-form').wait_until(have.title('DEMOQA'))

    def form_filling(self, user: User):
        with allure.step('Заполняем и отправляем форму'):
            self.first_name.type(user.first_name)
            self.last_name.type(user.last_name)
            browser.all('[name=gender]').element_by(have.value(user.gender)).element(
                '..'
            ).click()
            browser.element('[id="userNumber"]').type(user.mobile)
            if user.email:
                browser.element('[id="userEmail"]').type(user.email)
            if user.date_of_birth:
                day = user.date_of_birth.split(' ')[0]
                if len(str(day)) == 1:
                    day = f"00{str(day)}"
                else:
                    day = f"0{str(day)}"
                month = user.date_of_birth.split(' ')[1].split(',')[0]
                year = user.date_of_birth.split(' ')[1].split(',')[1]
                browser.element('[id="dateOfBirthInput"]').click()
                browser.element('[class="react-datepicker__month-select"]').type(month)
                browser.element('[class="react-datepicker__year-select"]').type(year)
                browser.element(
                    f'.react-datepicker__day--{day}:not(.react-datepicker__day--outside-month)'
                ).click()
            if user.subject:
                # browser.element('[id="subjectsInput"]').click().type(
                #     user.subjects
                # ).press_enter()
                self.subject.click().type(user.subject).press_enter()
            if user.hobbies:
                browser.all('.custom-checkbox').element_by(
                    have.exact_text(user.hobbies)
                ).click()
            if user.image:
                browser.element('[id="uploadPicture"]').set_value(
                    resource.path(user.image)
                )
            if user.current_address:
                browser.element('[id="currentAddress"]').type(user.current_address)
            if user.state:
                browser.element('[id="react-select-3-input"]').type(
                    user.state
                ).press_enter()
            if user.state and user.city:
                browser.element('[id="react-select-4-input"]').type(
                    user.city
                ).press_enter()

            browser.element('[id="submit"]').perform(command.js.click)

    @staticmethod
    def should_registered_user_with(user: User):
        with allure.step('Проверяем соответствие введенных данных полученным'):
            browser.element(
                '[class="table table-dark table-striped table-bordered table-hover"]'
            ).all('tr td:nth-child(2)').should(
                have.texts(
                    f'{user.first_name} {user.last_name}',
                    user.email,
                    user.gender,
                    user.mobile,
                    user.date_of_birth,
                    user.subject,
                    user.hobbies,
                    user.image,
                    user.current_address,
                    f'{user.state} {user.city}',
                )
            )
