from scripts.utils import *
import json


def mail_lookup(email):
    try:
        mail = str(email)
        d = mail.split('@')[1]
        l = mail.split('@')[0]
        result = f'{green}> {white}Логин:\t\t{l}'
        result += f'\n{green}> {white}Домен:\t\t{d}'
        url = f"http://api.eva.pingutil.com/email?email={mail}"
        response = requests.get(url)
        info_mail = json.loads(response.text)
        if response.status_code == 200:
            valid_syntax = info_mail['data']['valid_syntax']
            disposable = info_mail['data']['disposable']
            webmail = info_mail['data']['webmail']
            deliverable = info_mail['data']['deliverable']
            catch_all = info_mail['data']['catch_all']
            spam = info_mail['data']['spam']

            if valid_syntax == True:
                valid_syntax = f'{green + Style.NORMAL}Валидный'
            else:
                valid_syntax = f'{red + Style.NORMAL}Не валидный'
            if disposable == True:
                disposable = f'{red + Style.NORMAL}Да'
            else:
                disposable = f'{green + Style.NORMAL}Нет'
            if webmail == True:
                webmail = 'Да'
            else:
                webmail = 'Нет'
            if deliverable == True:
                deliverable = 'Да'
            else:
                deliverable = 'Нет'
            if catch_all == True:
                catch_all = 'Да'
            else:
                catch_all = f'Нет'
            if spam == True:
                spam = f'{red + Style.NORMAL}Да'
            else:
                spam = f'{green + Style.NORMAL}Нет'

            result += (f'\n{green}> {white}Синтаксис:\t\t{valid_syntax}'
                       f'\n{green}> {white}Одноразовая:\t\t{disposable}'
                       f'\n{green}> {white}Веб-почта:\t\t{webmail}'
                       f'\n{green}> {white}Отправка писем:\t{deliverable}'
                       f'\n{green}> {white}Принятие писем:\t{catch_all}'
                       f'\n{green}> {white}Cпам:\t\t\t{spam}')
        return result
    except:
        pass


def mail_leaked(email):
    try:
        result = f'{blue}────────────────────────────────{white}'
        mail = str(email)
        l = mail.split('@')[0]
        url = f"https://api.proxynova.com/comb?query={l}"
        response = requests.get(url)
        info_mail = json.loads(response.text)
        if response.status_code == 200:
            res = info_mail['lines']
            count = info_mail['count']
            if int(count) > 0:
                res_list = []
                for i in res:
                    login = i.split(':')[0]
                    password = i.split(':')[1]
                    res_list.append(f"\n{green}> {white}{login}:{red + Style.NORMAL}{password}{white}")

                for i in res_list:
                    result += i
        return result
    except:
        pass


def mail(command, data_command):
    data = remove_first_space(data_command.replace(command, ''))

    if check_email(data):
        print(f'Это не почта!\n')
        main()

    print(f'Информация о почте'
          f'\n{blue}=================={white}'
          f'\n'
          f'\nТип данных\t\tЗначение'
          f'\n{blue}──────────\t\t────────{white}'
          f'\n{green}> {white}Почта:\t\t{data}')

    if command == 'maillookup':
        s = mail_lookup(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'mailleaked':
        s = mail_leaked(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'mailinfo':
        s = api_leak_osint(data)
        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'mailall':
        s1 = mail_lookup(data)
        if s1 == None:
            error_search()
        else:
            print(s1)
        s2 = mail_leaked(data)
        if s2 == None:
            error_search()
        else:
            print(s2)
        s3 = api_leak_osint(data)
        if s3 == None:
            error_search()
        else:
            print(s3)
