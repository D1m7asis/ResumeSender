from urllib.parse import urlparse

from seleniumbase import SB


class ResumeSender:
    def __init__(self, links):
        self.links: [str] = links

    def process_links(self, override_employer=None):
        with SB(test=True) as sb:
            for link in self.links:
                try:
                    sb.open(link)

                    if override_employer:
                        employer = override_employer
                    else:
                        hostname = urlparse(link).hostname
                        if not hostname:
                            raise ValueError(f"Невозможно извлечь хост из ссылки: {link}")
                        employer = hostname.split('.')[0]

                    try:
                        module = __import__(f"employers.{employer}", fromlist=[f"process_application"])
                        module.process_application(sb)
                    except (ImportError, AttributeError):
                        raise NotImplementedError(f"Нет обработчика для работодателя: {employer}")

                except Exception as e:
                    print(f"Ошибка при обработке ссылки {link}: {e}")
                    continue


if __name__ == "__main__":
    file_path = "links_apply_to.txt"

    with open(file_path, 'r', encoding='utf-8') as file:
        links = [line.strip() for line in file if line.strip()]

    ResumeSender(links).process_links()
