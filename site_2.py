import requests

cookies = {
    'cud': 'F2/It2QpuGdUJJi1A4TOAg==',
    '_ym_uid': '1680455784871448492',
    '_ym_d': '1680455784',
    '__zzatgib-w-betcity': 'MDA0dBA=Fz2+aQ==',
    'xq_icm': '10000',
    '_gid': 'GA1.2.1249358151.1680544462',
    '_ym_isad': '1',
    '_ga': 'GA1.1.2109130920.1680455784',
    '_gat': '1',
    '_ga_WQEG57XEGJ': 'GS1.1.1680544089.2.1.1680547370.47.0.0',
    'cfidsgib-w-betcity': 'WX2AAiREZNmueb1Kfl1+09BA5WD/g4FGZgtfE9RE2t1rB1PxSxH45LRdfv5gVDE+sUlqwD5KUE13/gvErKNtha+xGafxsLzk9e8crOgwa3Yf8dmHg1/GpOoCbB6HfBviz69rw2lh0bREwGSPfE5nQLshrS4ZMEELDYGZmA==',
    'gsscgib-w-betcity': 'PxbAfH+l6aJ7uT+vAvXQqkJLPjZTiyLvCGnAsBZC0JPzM83N0Z/IDCzlYQKPm9Mny/SwfBMk4rEoXPfM+uFReBCUj9T+lzbuCxP2digFvCAT+Z7A7n7Z+pKTsrSN5ftGn3mP06u1z6Ab2Suauj2YjsbHr7DO7HdvUMkpGIMgBZJrGHiPvNe2jFU8HaqaoPQnuzGBPTZArrisatgwdfIGJdjQ+xF81G+hc2mL0ObzKf6FjTawUdxEN1J+2lKF3zGn2KLjQMUKDL/iyeQWRmwI',
    'fgsscgib-w-betcity': 'kk1dfee0b6bc33a81b69ebbe6b55e03440fa6d4f',
}

headers = {
    'authority': 'ad.betcity.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cud=F2/It2QpuGdUJJi1A4TOAg==; _ym_uid=1680455784871448492; _ym_d=1680455784; __zzatgib-w-betcity=MDA0dBA=Fz2+aQ==; xq_icm=10000; _gid=GA1.2.1249358151.1680544462; _ym_isad=1; _ga=GA1.1.2109130920.1680455784; _gat=1; _ga_WQEG57XEGJ=GS1.1.1680544089.2.1.1680547370.47.0.0; cfidsgib-w-betcity=WX2AAiREZNmueb1Kfl1+09BA5WD/g4FGZgtfE9RE2t1rB1PxSxH45LRdfv5gVDE+sUlqwD5KUE13/gvErKNtha+xGafxsLzk9e8crOgwa3Yf8dmHg1/GpOoCbB6HfBviz69rw2lh0bREwGSPfE5nQLshrS4ZMEELDYGZmA==; gsscgib-w-betcity=PxbAfH+l6aJ7uT+vAvXQqkJLPjZTiyLvCGnAsBZC0JPzM83N0Z/IDCzlYQKPm9Mny/SwfBMk4rEoXPfM+uFReBCUj9T+lzbuCxP2digFvCAT+Z7A7n7Z+pKTsrSN5ftGn3mP06u1z6Ab2Suauj2YjsbHr7DO7HdvUMkpGIMgBZJrGHiPvNe2jFU8HaqaoPQnuzGBPTZArrisatgwdfIGJdjQ+xF81G+hc2mL0ObzKf6FjTawUdxEN1J+2lKF3zGn2KLjQMUKDL/iyeQWRmwI; fgsscgib-w-betcity=kk1dfee0b6bc33a81b69ebbe6b55e03440fa6d4f',
    'origin': 'https://betcity.ru',
    'referer': 'https://betcity.ru/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'rev': '6',
    'ver': '316',
    'csn': 'ooca9s',
}

data = {
    'ids': '75175',
}

response = requests.post('https://ad.betcity.ru/d/off/events', params=params, cookies=cookies, headers=headers, data=data)
