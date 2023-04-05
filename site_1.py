import requests

cookies = {
    'cud': 'WNTqCWQqxxNzynVCAx7yAg==',
    '_ym_uid': '1680525080918348442',
    '_ym_d': '1680525080',
    '__zzatgib-w-betcity': 'MDA0dBA=Fz2+aQ==',
    'xq_icm': '10000',
    '_gid': 'GA1.2.513693867.1680699026',
    '_ym_isad': '1',
    'gsscgib-w-betcity': 'PrcZHdon+MKMxhg6/3uqwE4Wlj7xgpI8CKgGegVwiR4WTUxrKTDkTJsHjxu3hVu0R741hnbXEEK1e9LB2gC5SGRNtHaaU3mMiyIchkJw4ATEX4QObUOoniTXncaXoTj13C4LwR7yopx4LB1cDhV2NU1k2jpcJbUyYSmMlIRQ7OSLcA/zaTJXV6eyV+at32b5ZYW0Ehpo7oY8ND3qZFOuGaos70bRg4n/irXsYapbw5d6fhKsvDFJ7bga3k9RiAkehM4=',
    'fgsscgib-w-betcity': '0jiW1011dc343abe73254c9cd2c059104df552e7',
    '_ga_WQEG57XEGJ': 'GS1.1.1680702345.8.0.1680702345.60.0.0',
    '_ga': 'GA1.2.1484943170.1680525077',
    '_gat_UA-93476422-9': '1',
    'cfidsgib-w-betcity': 'c4lUMNFik3re1RdGx6mGcDx84fjTF5di71AJkHGMPi052DrJlgwDYC3Y1ovdFLJaHBfoiR6b5xHJV6HltHcSoLNEyUFq7DqiXbStk+/NWA4jmdyqPBDAchZRs0oYWdbej853KyfLj8pGpfAtuE1crYrPcsNZahKEJluQMmE=',
}

headers = {
    'authority': 'ad.betcity.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cud=WNTqCWQqxxNzynVCAx7yAg==; _ym_uid=1680525080918348442; _ym_d=1680525080; __zzatgib-w-betcity=MDA0dBA=Fz2+aQ==; xq_icm=10000; _gid=GA1.2.513693867.1680699026; _ym_isad=1; gsscgib-w-betcity=PrcZHdon+MKMxhg6/3uqwE4Wlj7xgpI8CKgGegVwiR4WTUxrKTDkTJsHjxu3hVu0R741hnbXEEK1e9LB2gC5SGRNtHaaU3mMiyIchkJw4ATEX4QObUOoniTXncaXoTj13C4LwR7yopx4LB1cDhV2NU1k2jpcJbUyYSmMlIRQ7OSLcA/zaTJXV6eyV+at32b5ZYW0Ehpo7oY8ND3qZFOuGaos70bRg4n/irXsYapbw5d6fhKsvDFJ7bga3k9RiAkehM4=; fgsscgib-w-betcity=0jiW1011dc343abe73254c9cd2c059104df552e7; _ga_WQEG57XEGJ=GS1.1.1680702345.8.0.1680702345.60.0.0; _ga=GA1.2.1484943170.1680525077; _gat_UA-93476422-9=1; cfidsgib-w-betcity=c4lUMNFik3re1RdGx6mGcDx84fjTF5di71AJkHGMPi052DrJlgwDYC3Y1ovdFLJaHBfoiR6b5xHJV6HltHcSoLNEyUFq7DqiXbStk+/NWA4jmdyqPBDAchZRs0oYWdbej853KyfLj8pGpfAtuE1crYrPcsNZahKEJluQMmE=',
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
    'rev': '3',
    'ids': '11184843',
    'ver': '316',
    'csn': 'ooca9s',
}

response = requests.get('https://ad.betcity.ru/d/off/ext', params=params, cookies=cookies, headers=headers)
