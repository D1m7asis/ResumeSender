from seleniumbase import SB


class ResumeSender:
    def __init__(self, links):
        self.links = links

    def process_links(self):
        with SB(test=True) as sb:
            for link in self.links:
                try:
                    sb.open(link)
                    iframe = sb.find_element("iframe.lc-iframe__iframe")
                    sb.driver.switch_to.frame(iframe)

                    sb.driver.execute_script("window.scrollBy(0, 2000);")
                    sb.wait(2)

                    sb.click('div p:contains("Файл с резюме")')

                    # Заполняем форму
                    sb.choose_file("input[type='file']", cv_pdf_path)
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

                except Exception as e:
                    print(f"Ошибка при обработке ссылки {link}: {e}")
                    continue


if __name__ == "__main__":
    file_path = "links.txt"

    with open(file_path, 'r', encoding='utf-8') as file:
        links = [line.strip() for line in file if line.strip()]

    name = "Иван"
    surname = "Иванов"
    phone = "+79998887766"
    cv_pdf_path = "CV.pdf"
    email = "email@yandex.ru"
    additional_message = '''
    Доброго дня! Хочу у вас работать!
    '''

    ResumeSender(links).process_links()
