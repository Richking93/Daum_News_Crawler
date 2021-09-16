import requests
import json
from bs4 import BeautifulSoup as bs

headers = { "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
}
pages = 1
sectors = ["economic","politics","society"]
sector = ""
page = 0
url = f'https://news.daum.net/{sector}'

result = []
i = 0
while True:
    print(f'page : {i+1}')
    res = requests.get(url.format(sectors[i]), headers = headers)
    if res.status_code == 200:
        html = bs(res.text, 'html.parser')
        cont = html.find('main')
        try:
            items = cont.findAll('li')
        except Exception as e:
            print(str(e))
            break
        else:
            for item in items:
                tit = item.find('strong','tit_thumb')
                tit_cmtrank = item.find('strong','tit_cmtrank')
                if tit != None:
                    try:
                        result.append({
                        'page': i,
                        'title': tit[span].get_text()
                        })
                    except:
                        result.append({
                            'page': i,
                            'title': tit.get_text()
                        })
                elif tit_cmtrank != None :
                   result.append({
                       'page': i,
                       'title': tit_cmtrank.get_text()
                   })
                else:
                    pass
    i = i+1
    if i == 3:
       print(f"reached page {i} break")
       break


with open('result.json' , 'w', encoding = 'utf-8') as f:
    json.dump(result, f, indent='\t', ensure_ascii=False)

print('완료')
'현재기준, - 심리 가격 , 호재 지수'