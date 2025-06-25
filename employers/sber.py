from employee.personal_info import *


def process_application(sb):
    sb.driver.execute_script("window.scrollBy(0, 200);")
    sb.wait(2)

    # Заполняем форму
    sb.choose_file("input[type='file']", local_cv_path)
    sb.type('input[placeholder="Фамилия"]', surname)
    sb.type('input[placeholder="Имя"]', name)
    sb.type('input[placeholder="Email"]', email)
    sb.type('input[placeholder="Телефон"]', phone)

    # Выбираем пункт согласия
    sb.click("span:contains('Я даю согласие на обработку')")

    # Отправляем форму
    sb.click("button:contains('Откликнуться')")

    # Ждем подтверждения отправки
    sb.assert_text("Спасибо за отклик!", timeout=15)
