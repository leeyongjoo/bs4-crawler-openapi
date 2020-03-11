"""
구글 번역 라이브러리 이용
"""
from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def get_google_translate_list(textENList, dest='ko'):
    translations = translator.translate(textENList, dest=dest)
    textKRList = []
    for trans in translations:
        textKRList.append(trans.text)
    return textKRList

"""
네이버 Papago NMT API 이용
"""
import requests
# 파파고 API 설정
PAPAGO_CLIENT_ID = ''
PAPAGO_CLIENT_SECRET = ''

# papago_client_info.config 파일에서 설정값 가져오기(설정값 노출 방지)
with open('papago_client_info.config') as f:
    content = f.read().split()
    PAPAGO_CLIENT_ID = content[0]
    PAPAGO_CLIENT_SECRET = content[1]

PAPAGO_NMT_URL = 'https://openapi.naver.com/v1/papago/n2mt'
HEADERS = {'X-Naver-Client-Id':PAPAGO_CLIENT_ID, 'X-Naver-Client-Secret': PAPAGO_CLIENT_SECRET}
PARAMS = {"source": "en", "target": "ko", "text":"test"}

def get_nmt_translate(text, source='en', target='ko'):
    PARAMS['text'] = text
    PARAMS['source'] = source
    PARAMS['target'] = target

    response = requests.post(PAPAGO_NMT_URL, headers=HEADERS, data=PARAMS)
    result = response.json()
    return result['message']['result']['translatedText']

if __name__ == "__main__":
    pass