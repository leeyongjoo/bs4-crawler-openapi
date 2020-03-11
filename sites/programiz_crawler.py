'''
programiz.com
메소드 리스트 수집하여 csv 파일로 저장
'''
import requests
from bs4 import BeautifulSoup

dataTypes = ['built-in', 'dictionary', 'list', 'set', 'string', 'tuple']

def method_crawling(dataType):
    url = 'https://www.programiz.com/python-programming/methods/' + dataType

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    rows = soup.select('div.reference-data--row')

    methodNameList = []
    descriptionENList = []
    descriptionKRList = []
    for row in rows:
        methodNameSplit = row.find('a').get_text().split()

        if methodNameSplit[1].lower() != dataType\
                and dataType != 'built-in': continue

        methodName = methodNameSplit[-1]
        descriptionEN = row.find('p').get_text()
        methodNameList.append(methodName)
        descriptionENList.append(descriptionEN)

    method_description_list = list(zip(methodNameList, descriptionENList))

    return method_description_list

if __name__ == "__main__":
    import pandas as pd

    for dataType in dataTypes:
        method_description_list = method_crawling(dataType)

        data = pd.DataFrame(method_description_list)
        data.columns = ['method', 'description']
        data.to_csv('programiz_python_methods/'
                    + dataType + '.csv', encoding='cp949')