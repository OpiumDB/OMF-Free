from scripts.utils import *
from phonenumbers import geocoder, carrier
import phonenumbers


def phone(command, data_command):
    data = remove_first_space(data_command.replace(command, ''))

    def phone_lookup(number):
        try:
            phone_parse = phonenumbers.parse(str("+") + number)
            country = geocoder.country_name_for_number(phone_parse, 'ru')
            operator = carrier.name_for_number(phone_parse, lang='ru')
            if operator == '':
                operator = 'Не удалось определить'
            result = (f'{green}> {white}Страна:\t\t{country}'
                      f'\n{green}> {white}Оператор:\t\t{operator}')
            return result
        except:
            pass

    phone_correct = correct_phone(data)
    print(f'{blue}Информация о номере'
          f'\n{white}==================='
          f'\n'
          f'\nТип данных\t\tЗначение'
          f'\n{blue}──────────\t\t────────'
          f'\n{green}> {white}Телефон:\t\t+{phone_correct}')

    if phone_correct == False:
        print(f'{red}Это не номер телефона!{white}\n')
        main()

    if command == 'phonelookup':
        s = phone_lookup(phone_correct)

        if s == None:
            error_search()
        else:
            print(s)
    elif command == 'phoneinfo':
        s1 = api_leak_osint(phone_correct)

        if s1 == None:
            error_search()
        else:
            print(s1)
    elif command == 'phoneall':
        s1 = phone_lookup(phone_correct)
        if s1 == None:
            error_search()
        else:
            print(s1)
        s2 = api_leak_osint(phone_correct)
        if s2 == None:
            error_search()
        else:
            print(s2)
