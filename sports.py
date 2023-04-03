import requests

cookies = {
    'cud': 'F2/It2QpuGdUJJi1A4TOAg==',
    '_ym_uid': '1680455784871448492',
    '_ym_d': '1680455784',
    '__zzatgib-w-betcity': 'MDA0dBA=Fz2+aQ==',
    'xq_icm': '10000',
    '_gid': 'GA1.2.1249358151.1680544462',
    '_ym_isad': '1',
    'cfidsgib-w-betcity': 'UbnZRwz+Jm85Q6j7083wAf8E1xnHG0AtnxC2C0qEqaDSgiH4carHpJyfrxVkajQsX8BgyW4dFsu5TxQnZiaipa7vjbksQ4lI/A11K/+nRriJb2u2XdLchTcJYHz49lRpD4eT+gkoX8Yu4ZooL/5Dg2NAYIaHNFxmNbEkEQ==',
    'gsscgib-w-betcity': 'dgEeOz+l2lSBGL8SyrYE46CYP213oa+aWmZ1RsGRKWwuBwn8BPhHIuD73RUh4NeRAgqTzrd1bHXr1CL4HOuSTWVlCD/raamZVOXA/xd5WW5B1nbsiAh3imKSVKOYA+QlL4BB0/w71SsXEMv/cJDr/gIRdmrQBDbzlJhigsQyY7wNMY6dbO3M42JID1eV5JBKKzD55gNiSbCHvFk7o7l7JzQjF1FvY70vn2LM0RxQI3/dgPtYzapCZ1ufSUhnrD8iDtNIDD/MEtD/gAmDEucp',
    'fgsscgib-w-betcity': '8W7o62be280958e096f550a9d2c679986fee7f11',
    '_ga_WQEG57XEGJ': 'GS1.1.1680544089.2.1.1680548937.60.0.0',
    '_ga': 'GA1.2.2109130920.1680455784',
}

headers = {
    'authority': 'ad.betcity.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cud=F2/It2QpuGdUJJi1A4TOAg==; _ym_uid=1680455784871448492; _ym_d=1680455784; __zzatgib-w-betcity=MDA0dBA=Fz2+aQ==; xq_icm=10000; _gid=GA1.2.1249358151.1680544462; _ym_isad=1; cfidsgib-w-betcity=UbnZRwz+Jm85Q6j7083wAf8E1xnHG0AtnxC2C0qEqaDSgiH4carHpJyfrxVkajQsX8BgyW4dFsu5TxQnZiaipa7vjbksQ4lI/A11K/+nRriJb2u2XdLchTcJYHz49lRpD4eT+gkoX8Yu4ZooL/5Dg2NAYIaHNFxmNbEkEQ==; gsscgib-w-betcity=dgEeOz+l2lSBGL8SyrYE46CYP213oa+aWmZ1RsGRKWwuBwn8BPhHIuD73RUh4NeRAgqTzrd1bHXr1CL4HOuSTWVlCD/raamZVOXA/xd5WW5B1nbsiAh3imKSVKOYA+QlL4BB0/w71SsXEMv/cJDr/gIRdmrQBDbzlJhigsQyY7wNMY6dbO3M42JID1eV5JBKKzD55gNiSbCHvFk7o7l7JzQjF1FvY70vn2LM0RxQI3/dgPtYzapCZ1ufSUhnrD8iDtNIDD/MEtD/gAmDEucp; fgsscgib-w-betcity=8W7o62be280958e096f550a9d2c679986fee7f11; _ga_WQEG57XEGJ=GS1.1.1680544089.2.1.1680548937.60.0.0; _ga=GA1.2.2109130920.1680455784',
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
    'rev': '1',
    'tp': '2',
    'ver': '316',
    'csn': 'ooca9s',
}

response = requests.get('https://ad.betcity.ru/d/popular', params=params, cookies=cookies, headers=headers)

print(response.text)