from selenium.webdriver import Keys

from employee.personal_info import *


def process_application(sb):
    # Личные данные
    sb.type('input[aria-label="Фамилия"]', surname)
    sb.type('input[aria-label="Имя"]', name)
    sb.type('input[aria-label="Отчество"]', middle_name)
    city_placeholder = 'input[aria-label="Город проживания"]'
    sb.type(city_placeholder, city)
    sb.wait(1)
    sb.send_keys(city_placeholder, Keys.ENTER)

    sb.type('input[aria-label="Дата рождения"]', date_of_birth)
    sb.type('input[aria-label="Телефон"]', short_phone)
    sb.type('input[aria-label="Электронная почта"]', email)

    sb.type('input[aria-label="Ник в telegram, WhatsApp"]', contacts)

    work_type = 'div[data-test-id="youth-form-work-type"]'
    sb.click(work_type)
    sb.send_keys(work_type, Keys.DOWN)
    sb.send_keys(work_type, Keys.ENTER)

    # Образование
    study_placeholder = 'input[aria-label="Место учёбы"]'
    sb.type(study_placeholder, study_place)
    sb.wait(1)
    sb.send_keys(study_placeholder, Keys.ENTER)
    sb.type('input[aria-label="Специальность"]', speciality)
    sb.type('input[aria-label="Год окончания"]', year_of_end)

    # Опыт работы
    # sb.click('button > span:contains("Добавить место работы")')

    # Дополнительно
    sb.type('input[aria-label="Ссылка на резюме"]', uploaded_cv_url)
    sb.type('input[aria-label="Ссылка на портфолио"]', portfolio_link)
    sb.type('textarea[name="coverLetter"]', motivation_letter)

    sb.click('div[data-test-id="sopdConfirmed-checkbox-caption"]')
    sb.click('button[type="submit"')

    sb.assert_text("Отклик отправлен", timeout=20)
