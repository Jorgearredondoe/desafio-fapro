import calendar
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from ..models import UF


class UFEndpoint():
    def __init__(self, year):
        self.year = year
        self.url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'

    def scrap_data(self):
        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id='table_export')

        job_elements = results.findAll('tr')
        arr = []
        for job_element in job_elements:
            job_element = job_element.text.replace(
                u'\xa0', u'-1')
            clean_element = job_element.strip().split('\n')
            arr.append(clean_element)
        self.days = arr[1:]

    def clean_uf_values(self):
        self.uf_list = [{'value': float(value['value'].replace('.', '')
                                        .replace(',', '.')),
                         'date': value['date']} for value in self.uf_list]

    def data_serializer(self):
        self.uf_list = []
        for month in range(1, 13):
            for index_uf, uf in enumerate(self.days):
                num_days = calendar.monthrange(int(self.year), int(month))[1]
                if index_uf + 1 > num_days:
                    continue
                date_str = f'{index_uf + 1}/{month}/{self.year}'
                date_obj = datetime.strptime(date_str, '%d/%m/%Y')
                self.uf_list.append({'value': uf[month], 'date': date_obj})


def Update_DB():
    year = '2023'
    UF_object = UFEndpoint(year)
    UF_object.scrap_data()
    UF_object.data_serializer()
    UF_object.clean_uf_values()
    for i in UF_object.uf_list:
        new_model_data = UF(value=i['value'], date=i['date'])
        new_model_data.save()
