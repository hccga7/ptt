import requests
url = 'https://www.taifex.com.tw/cht/3/optDailyMarketReport'
payload = {'queryType': '2'
    , 'marketCode': '0'
    , 'dateaddcnt': ''
    , 'commodity_id': 'TXO'
    , 'commodity_id2': ''
    , 'queryDate': '2019/06/28'
    , 'MarketCode': '0'
    , 'commodity_idt': 'TXO'
    , 'commodity_id2t': ''
    , 'commodity_id2t2': ''}
encoding = 'utf8'
r = requests.post(url, data=payload)
r.encoding = encoding
response_html = r.content
file = open('rpt.html', 'w')
file.write(response_html.decode())
file.close()