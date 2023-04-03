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
    'cfidsgib-w-betcity': 'x2FZKkF01gr005HTfhSliUhM60mwGQBnzBVa4HrAYAE2sNRAhJaNaeRoNP3hmDoARzjPmNMUyKk7VgX2HAV8THIeQ1u0vxQJ3g9RnXa2HkfdJnu8TM3QCSg8iO9F4/B+lCFQ/A8h8AtpW51xpiCHIWs6moWKYSzHisg+Cg==',
    'gsscgib-w-betcity': '64n5PSYdV5hXmauDlzRpcnDIjD+2vXqlzQNPzNiNUlDnSCDIv3odwscZdGcX7qUw8wDPb2wjA8DGyB8rd2/L8x1m2b0Imm2G8PahbU8FQFbI7bl0Y24pyOmeAmQ6Sf+FSSobMrymZDrDvGzRMIbtEXKNkZNWiiXTXGXreUqbmaSwBtqm7l6+LpGVogED2MewsNH47CNBlpqa5MeO1IYyaWwnV29G1xT72qKXFRvPvfmwtggxD4Z991K4+aLwlTd+UoNl0pr8Dup7x/ypUDuGwlArfgrR6uuMHijDP+fhoI7d',
    'fgsscgib-w-betcity': 'gvQi491ce6dfffc7d4978ed98214e3da420b41a5',
    '_ga_WQEG57XEGJ': 'GS1.1.1680544089.2.1.1680545507.48.0.0',
}

headers = {
    'authority': 'ad.betcity.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cud=F2/It2QpuGdUJJi1A4TOAg==; _ym_uid=1680455784871448492; _ym_d=1680455784; __zzatgib-w-betcity=MDA0dBA=Fz2+aQ==; xq_icm=10000; _gid=GA1.2.1249358151.1680544462; _ym_isad=1; _ga=GA1.1.2109130920.1680455784; _gat=1; cfidsgib-w-betcity=x2FZKkF01gr005HTfhSliUhM60mwGQBnzBVa4HrAYAE2sNRAhJaNaeRoNP3hmDoARzjPmNMUyKk7VgX2HAV8THIeQ1u0vxQJ3g9RnXa2HkfdJnu8TM3QCSg8iO9F4/B+lCFQ/A8h8AtpW51xpiCHIWs6moWKYSzHisg+Cg==; gsscgib-w-betcity=64n5PSYdV5hXmauDlzRpcnDIjD+2vXqlzQNPzNiNUlDnSCDIv3odwscZdGcX7qUw8wDPb2wjA8DGyB8rd2/L8x1m2b0Imm2G8PahbU8FQFbI7bl0Y24pyOmeAmQ6Sf+FSSobMrymZDrDvGzRMIbtEXKNkZNWiiXTXGXreUqbmaSwBtqm7l6+LpGVogED2MewsNH47CNBlpqa5MeO1IYyaWwnV29G1xT72qKXFRvPvfmwtggxD4Z991K4+aLwlTd+UoNl0pr8Dup7x/ypUDuGwlArfgrR6uuMHijDP+fhoI7d; fgsscgib-w-betcity=gvQi491ce6dfffc7d4978ed98214e3da420b41a5; _ga_WQEG57XEGJ=GS1.1.1680544089.2.1.1680545507.48.0.0',
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
    'ids': '445',
}

response = requests.post('https://ad.betcity.ru/d/off/events', params=params, cookies=cookies, headers=headers, data=data)

print(response.text)