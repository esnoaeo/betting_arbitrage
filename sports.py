import json
import requests


def get_sports():
    cookies = {
        'cud': 'WNTqCWQqxxNzynVCAx7yAg==',
        '_gid': 'GA1.2.540339939.1680525077',
        '_ym_uid': '1680525080918348442',
        '_ym_d': '1680525080',
        '__zzatgib-w-betcity': 'MDA0dBA=Fz2+aQ==',
        'xq_icm': '10000',
        '_ym_isad': '1',
        '_gat': '1',
        '_gat_UA-93476422-9': '1',
        'cfidsgib-w-betcity': 'wGPJck+5GcmB0mp36RtJ+alc48glJxuft2SAUIc4JQVw6GWWM/pSzTPWcz5Ah3uroFGlZ9HLxiru78+diBT38NO7UN412ZcwNnsq8i8y2faJHguv9TJFj1Vr3J09mOnz2y6Nru6o4onMD/zIaF/gDiwOLOLLrtl6SdFW5w==',
        'gsscgib-w-betcity': 'OAPXXpWN32XgBC0d/2pq3jng1isilCpo+DlelYWmGvgKZa/tWrIqOu6R1OlJTv880ZFz9zwGo7XPUs4tvZVDO8CfEkFNhQKe9kPsK2+AO0UOgymsbdWxWSM/0//k1LGSOvR0vLcJR3O+h9XFrbM4Tmn1fJ9cnfwMBOhfJYgVrJA6wNfsxLG/M9gnPs/EfPC+IBWjb639dqPRi9tFhw+1i55iGfuqerrgj5riXesuxIiwjwStFlOAHyc1pL8BKiPL1g==',
        'fgsscgib-w-betcity': 'zah3e324c32a1afeeeb2f95838f44666c172d507',
        '_ga_WQEG57XEGJ': 'GS1.1.1680598044.4.1.1680599297.53.0.0',
        '_ga': 'GA1.2.1484943170.1680525077',
    }

    headers = {
        'authority': 'ad.betcity.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cud=WNTqCWQqxxNzynVCAx7yAg==; _gid=GA1.2.540339939.1680525077; _ym_uid=1680525080918348442; _ym_d=1680525080; __zzatgib-w-betcity=MDA0dBA=Fz2+aQ==; xq_icm=10000; _ym_isad=1; _gat=1; _gat_UA-93476422-9=1; cfidsgib-w-betcity=wGPJck+5GcmB0mp36RtJ+alc48glJxuft2SAUIc4JQVw6GWWM/pSzTPWcz5Ah3uroFGlZ9HLxiru78+diBT38NO7UN412ZcwNnsq8i8y2faJHguv9TJFj1Vr3J09mOnz2y6Nru6o4onMD/zIaF/gDiwOLOLLrtl6SdFW5w==; gsscgib-w-betcity=OAPXXpWN32XgBC0d/2pq3jng1isilCpo+DlelYWmGvgKZa/tWrIqOu6R1OlJTv880ZFz9zwGo7XPUs4tvZVDO8CfEkFNhQKe9kPsK2+AO0UOgymsbdWxWSM/0//k1LGSOvR0vLcJR3O+h9XFrbM4Tmn1fJ9cnfwMBOhfJYgVrJA6wNfsxLG/M9gnPs/EfPC+IBWjb639dqPRi9tFhw+1i55iGfuqerrgj5riXesuxIiwjwStFlOAHyc1pL8BKiPL1g==; fgsscgib-w-betcity=zah3e324c32a1afeeeb2f95838f44666c172d507; _ga_WQEG57XEGJ=GS1.1.1680598044.4.1.1680599297.53.0.0; _ga=GA1.2.1484943170.1680525077',
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
        'rev': '4',
        'ids_sp': '1',
        'ver': '316',
        'csn': 'ooca9s',
    }

    response = requests.get('https://ad.betcity.ru/d/off/champs', params=params, cookies=cookies, headers=headers)
    jsonobj = json.loads(response.text)

    sportlist = []
    for i in (jsonobj['reply']['sports']['1']['chmps']):
        sportlist.append(i)

    return sportlist
