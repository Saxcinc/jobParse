import json

import bs4
import requests
from fake_headers import Headers
from tqdm import tqdm


def get_fake_headers():
    return Headers(browser='chrome', os='win').generate()


def get_main_ads():
    # Функция возвращает основную информацию по заданной ссылке для поиска вакансии в МСК и СПб

    response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=get_fake_headers())
    main_soup = bs4.BeautifulSoup(response.text, features='lxml')
    full_tag = main_soup.findAll('div', 'serp-item serp-item_link')

    return full_tag


def get_link_ads():
    # Функция возвращает наименование вакансии, наименование компании, з/п и её ссылки
    info = []

    for link in tqdm(get_main_ads()):

        ad_information = link.find('a', class_='bloko-link')
        # Получаем общую информацию о компании
        info_about_the_company = link.find('a', class_='bloko-link bloko-link_kind-tertiary')
        # Получаем ссылку на вакансию
        ad_link = ad_information['href']
        # Получаем заработную плату вакансии
        salary = link.find('span', class_="bloko-header-section-2")
        # Получаем город вакансии
        city = link.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text
        # Получаем наименование вакансии
        job_title = ad_information.find('span').text.strip()
        # Получаем наименование компании
        company_name = info_about_the_company.find('span').text.strip()

        # Проверяем, пустое ли значение в salary
        if salary is None:
            salary = 'З/п не указана.'
        else:
            salary = salary.text

        # Условие истинно пока есть ссылка
        if ad_link:
            response_url = requests.get(f'{ad_link}', headers=get_fake_headers())
            soup = bs4.BeautifulSoup(response_url.text, features='lxml')

            find_description = soup.find('div', class_='vacancy-section')
            # Происходит парсинг описания вакансий
            if find_description:
                vacancy_text = find_description.get_text(separator='\n', strip=True)

                data_company = {
                    'job_title': job_title,
                    'company_name': company_name,
                    'link': ad_link,
                    'salary': salary,
                    'vacancy_text': vacancy_text,
                    'city': city,
                }

                info.append(data_company)

    return info


def job_selection():
    # Функция возвращает объявления, если в них содержатся ключевые слова
    suitable_vacancies = []

    # Проверка описаний вакансий по ключевым словам
    print('Собираем информацию о вакансии...\n')

    for desc in get_link_ads():
        if 'flask' in desc['vacancy_text'].lower() and 'django' in desc['vacancy_text'].lower():
            suitable_vacancies.append(desc)

    with open('finally_varancies.json', 'w') as file:
        json.dump(suitable_vacancies, file, ensure_ascii=False)
