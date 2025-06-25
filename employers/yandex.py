from employee.personal_info import *


def process_application(sb):
    iframe = sb.find_element("iframe.lc-iframe__iframe")
    sb.driver.switch_to.frame(iframe)

    sb.driver.execute_script("window.scrollBy(0, 2000);")
    sb.wait(4)

    sb.click('div p:contains("Файл с резюме")')

    # Заполняем форму
    sb.choose_file("input[type='file']", local_cv_path)
    sb.type("#answer_param_name", name)
    sb.type("#answer_param_surname", surname)
    sb.type("#answer_param_phone", phone)
    sb.type("#answer_non_profile_email_5257", email)
    sb.type("#answer_long_text_5258", additional_message)

    # Выбираем пункт согласия
    sb.click("p:contains('Рассмотрения моей')")

    # Отправляем форму
    sb.click("button[type='submit']")

    # Ждем подтверждения отправки
    sb.assert_text("Заявка отправлена! Спасибо", timeout=5)
