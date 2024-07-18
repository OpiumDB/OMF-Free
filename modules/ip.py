from scripts.utils import *
import json


def ip_lookup(ip_address):
    try:
        url = f"http://ipwho.is/{ip_address}"
        response = requests.get(url)
        ipwhois_info = json.loads(response.text)
        if response.status_code == 200:
            res = (f'{green}> {white}Континент:\t\t{ipwhois_info["continent"]}'
                   f'\n{green}> {white}Страна:\t\t{green + Style.NORMAL}{ipwhois_info["country"]}'
                   f'\n{green}> {white}Регион:\t\t{green + Style.NORMAL}{ipwhois_info["region"]}'
                   f'\n{green}> {white}Город:\t\t{ipwhois_info["city"]}'
                   f'\n{green}> {white}Индекс:\t\t{ipwhois_info["postal"]}'
                   f'\n{green}> {white}Столица:\t\t{ipwhois_info["capital"]}'
                   f'\n{green}> {white}Временная зона:\t{ipwhois_info["timezone"]["id"]}'
                   f'\n{green}> {white}UTC:\t\t\t{green + Style.NORMAL}{ipwhois_info["timezone"]["utc"]}'
                   f'\n{green}> {white}Время сейчас:\t\t{ipwhois_info["timezone"]["current_time"]}')
            return res
    except:
        pass


def ip_data(ip_address):
    try:
        url = f"http://ipwho.is/{ip_address}"
        response = requests.get(url)
        ipwhois_info = json.loads(response.text)
        if response.status_code == 200:
            res = (f'{green}> {white}Тип:\t\t\t{ipwhois_info["type"]}'
                   f'\n{green}> {white}Соединение:\t\t{ipwhois_info["connection"]["org"]}'
                   f'\n{green}> {white}Домен:\t\t{ipwhois_info["connection"]["domain"]}')
            return res
    except:
        pass


def ip_geo(ip_address):
    try:
        url = f"http://ipwho.is/{ip_address}"
        response = requests.get(url)
        ipwhois_info = json.loads(response.text)
        if response.status_code == 200:
            res = (f'{green}> {white}Широта:\t\t{ipwhois_info["latitude"]}'
                   f'\n{green}> {white}Долгота:\t\t{ipwhois_info["longitude"]}'
                   f'\n{green}> {white}Yandex map:\t\thttps://yandex.ru/maps/?ll={ipwhois_info["longitude"]},{ipwhois_info["latitude"]}&z=12'
                   f'\n{green}> {white}Goggle map:\t\thttps://www.google.com/maps/@{ipwhois_info["latitude"]},{ipwhois_info["longitude"]},12z')
            return res
    except:
        pass


def check_hosting(ip_address):
    try:
        url = f"https://api.facha.dev/v1/ip/{ip_address}"
        response = requests.get(url)
        info = json.loads(response.text)
        if response.status_code == 200:
            subnet = info['subnet']
            asn_number = info['asn']['number']
            asn_name = info['asn']['name']
            asn_description = info['asn']['description']
            country = info['country']
            hosting = info['hosting']
            if hosting == 'True' or hosting == True:
                hosting = f'{green + Style.NORMAL}Да{white}'
            else:
                hosting = f'Нет'
            res = (f'{blue}──────────\t\t────────{white}'
                   f'\n{green}> {white}Подсеть:\t\t{subnet}'
                   f'\n{green}> {white}ASN номер:\t\t{asn_number}'
                   f'\n{green}> {white}ASN имя:\t\t{asn_name}'
                   f'\n{green}> {white}ASN описание:\t\t{asn_description}'
                   f'\n{green}> {white}Страна:\t\t{country}'
                   f'\n{green}> {white}Хостинг:\t\t{hosting}')
            return res
    except:
        pass


def ip(command, data_command):
    data = remove_first_space(data_command.replace(command, ''))

    if is_invalid_ip(data):
        print(f'{red}Это не IP адрес!{white}\n')
        main()

    print(f'{blue}Информация об IP адресе{white}'
          f'\n======================='
          f'\n'
          f'\nТип данных\t\tЗначение'
          f'\n{blue}──────────\t\t────────{white}'
          f'\n{green}> {white}IP:\t\t\t{data}')

    if command == 'iplookup':
        s = ip_lookup(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'ipdata':
        s = ip_data(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'ipgeo':
        s = ip_geo(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'ipcheckhost':
        s = check_hosting(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'ipall':
        s1 = ip_lookup(data)
        if s1 == None:
            error_search()
        else:
            print(s1)
        s2 = ip_data(data)
        if s2 == None:
            error_search()
        else:
            print(s2)
        s3 = ip_geo(data)
        if s3 == None:
            error_search()
        else:
            print(s3)
        s4 = check_hosting(data)
        if s4 == None:
            error_search()
        else:
            print(s4)
