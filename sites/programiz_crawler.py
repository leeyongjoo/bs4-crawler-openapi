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
    from mod.translates import get_nmt_translate, get_google_translate_list

    CSV_ENCODING = 'utf-8'

    ###################
    # PAPAGO NMT 번역 #
    ###################
    for dataType in dataTypes:
        method_description_list = method_crawling(dataType)
        result_list = []
        for m, d in method_description_list:
            result_list.append((m, d, get_nmt_translate(d)))

        data = pd.DataFrame(result_list)
        data.columns = ['method', 'description_english', 'description_korean']
        data.to_csv('programiz_python_methods/nmt/'
                    + dataType + '_' + CSV_ENCODING + '.csv', encoding=CSV_ENCODING)

    ###############
    # GOOGLE 번역 #
    ###############
    for dataType in dataTypes:
        method_description_list = method_crawling(dataType)
        description_KR_list = get_google_translate_list([_[1] for _ in method_description_list])

        result_list = []
        for i, md in enumerate(method_description_list):
            m, d = md
            result_list.append((m, d, description_KR_list[i]))

        data = pd.DataFrame(result_list)
        data.columns = ['method', 'description_english', 'description_korean']
        data.to_csv('programiz_python_methods/google/'
                    + dataType + '_' + CSV_ENCODING + '.csv', encoding=CSV_ENCODING)