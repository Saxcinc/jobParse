# Job Vacancy Parser

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12.3-yellow)
![Requests](https://img.shields.io/badge/Requests-2.31.0-green)
![TQDM](https://img.shields.io/badge/TQDM-4.66.2-orange)


Проект парсинга вакансий Python с использованием библиотек ![BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) и ![Requests](https://docs.python-requests.org/en/master/).

## Описание

Проект представляет собой скрипт для парсинга вакансий Python с сайта HeadHunter. Он фильтрует вакансии по ключевым словам "Django" и "Flask" и сохраняет информацию о каждой подходящей вакансии в формате JSON.

## Инструкции по установке

1. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

## Использование

1. Запустите скрипт `main.py`:

```bash
python main.py
```

2. После выполнения скрипта будет создан файл `finally_varancies.json`, содержащий информацию о выбранных вакансиях.


## Пример

Пример файла `finally_varancies.json`:

```json
[
    {
        "job_title": "Python Developer",
        "company_name": "ABC Company",
        "link": "https://www.example.com/vacancy/123",
        "salary": "100000-150000 руб.",
        "city": "Москва"
    },
    {
        "job_title": "Backend Python Developer",
        "company_name": "XYZ Ltd.",
        "link": "https://www.example.com/vacancy/456",
        "salary": "90000-120000 руб.",
        "city": "Санкт-Петербург"
    }
]
```




