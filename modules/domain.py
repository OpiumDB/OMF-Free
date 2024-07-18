from scripts.utils import *
from bs4 import BeautifulSoup


def domain_lookup(domain):
    try:
        url = f'https://check-host.net/ip-info?host={domain}&lang=ru'
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            data = soup.find("div", class_='ipinfo-item mb-3')
            ip_domain = data.find_all("tr")[0].get_text(strip=True).replace('IP адрес', '')
            ip_range = data.find_all("tr")[2].get_text(strip=True).replace('IP диапазон', '')
            provider_domain = data.find_all("tr")[3].get_text(strip=True).replace('Провайдер', '')
            organization_domain = data.find_all("tr")[4].get_text(strip=True).replace('Организация', '')
            country_domain = data.find_all("tr")[5].get_text(strip=True).replace('Страна', '')
            region_domain = data.find_all("tr")[6].get_text(strip=True).replace('Регион', '')
            city_domain = data.find_all("tr")[7].get_text(strip=True).replace('Город', '')
            timezone_domain = data.find_all("tr")[8].get_text(strip=True).replace('Часовой пояс', '')
            time_now_domain = data.find_all("tr")[9].get_text(strip=True).replace('Местное время', '')
            index_domain = data.find_all("tr")[10].get_text(strip=True).replace('Индекс', '')
            res = (f'{green}> {white}IP адрес:\t\t{green + Style.NORMAL}{ip_domain}'
                   f'\n{green}> {white}IP диапазон:\t\t{ip_range}'
                   f'\n{green}> {white}Провайдер:\t\t{green + Style.NORMAL}{provider_domain}'
                   f'\n{green}> {white}Организация:\t\t{organization_domain}'
                   f'\n{green}> {white}Страна:\t\t{country_domain}'
                   f'\n{green}> {white}Регион:\t\t{green + Style.NORMAL}{region_domain}'
                   f'\n{green}> {white}Город:\t\t{green + Style.NORMAL}{city_domain}'
                   f'\n{green}> {white}Часовой пояс:\t{timezone_domain}'
                   f'\n{green}> {white}Время сейчас:\t{time_now_domain}'
                   f'\n{green}> {white}Индекс:\t\t{index_domain}')

            return res
    except:
        pass


def whois(domain):
    try:
        url = f'https://www.whois.com/whois/{domain}'
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            data = soup.find("pre", class_='df-raw').get_text(strip=True)
            res = f'{blue}────────────────────────────────{white}'
            data_split = data.split('\n')
            for i in data_split:
                res += f"\n{i.replace(':', f': ')}"
            return res
    except:
        pass


def dns_records(domain):
    try:
        url = f'https://bgp.he.net/dns/{domain}'
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            data = soup.find("div", class_="tabdata")
            head_dns = data.find_all("div", class_="dnshead")
            data_dns = data.find_all("div", class_="dnsdata")
            head_texts = [head.get_text() for head in head_dns]
            data_texts = [data.get_text() for data in data_dns]

            res = f'{blue}────────────────────────────────{white}'

            for head, data in zip(head_texts, data_texts):
                clear_data = clean_text(data)
                res += (f"\n{green}> {white}{head}"
                        f"\n{clear_data}")
            return res
    except:
        pass


def domain(command, data_command):
    data = remove_first_space(data_command.replace(command, ''))

    if correct_domain(data):
        data = correct_domain(data)
    else:
        print(f'{red}Это не домен!{white}\n')
        main()

    print(f'Информация о домене'
          f'\n{blue}==================={white}'
          f'\n'
          f'\nТип данных\t\tЗначение'
          f'\n{blue}──────────\t\t────────'
          f'\n{green}> {white}Домен:\t\t{data}')

    if command == 'domainlookup':
        s = domain_lookup(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'whois':
        s = whois(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'dnsrecords':
        s = dns_records(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'domainall':
        s1 = domain_lookup(data)
        if s1 == None:
            error_search()
        else:
            print(s1)
        s2 = whois(data)
        if s2 == None:
            error_search()
        else:
            print(s2)
        s3 = dns_records(data)
        if s3 == None:
            error_search()
        else:
            print(s3)
