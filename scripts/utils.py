from scripts.variables import *
import socket
import re
import requests


def incorrect_command():
    print(f'{red}Некорректная команда!{white}')


def error_search():
    print(f'{red}Не удалось найти данные! Попробуйте включить/выключить VPN. Проверить соединение с интернетом{white}')


def extract_command(command):
    try:
        extract_result = str(command).split(' ')[0]
        return extract_result
    except:
        return False


def remove_first_space(input_string):
    try:
        if input_string[0] == ' ':
            return input_string.lstrip(' ')
        else:
            return input_string
    except:
        pass


def replace_in_last_element(input_list, old_char, new_char):
    if input_list:
        input_list[-1] = input_list[-1].replace(old_char, new_char)
    return input_list


def format_data(data, type):
    columns = type.split(',')
    values = data.split(',')
    formatted_data = {}
    for col, val in zip(columns, values):
        if col.strip() not in ['type', 'phone_number'] and val.strip() != '' and val.strip() != ' ':
            formatted_data[col] = val
    formatted_output = f"{blue}──────────\t\t────────\n{white}"

    for col, val in formatted_data.items():
        if len(col.capitalize()) <= 12:
            formatted_output += f"{green}> {white}{col.capitalize()}:\t\t{val}\n"
        elif len(col.capitalize()) <= 4:
            formatted_output += f"{green}> {white}{col.capitalize()}:\t\t\t{val}\n"
        else:
            formatted_output += f"{green}> {white}{col.capitalize()}:\t{val}\n"
    return formatted_output


def is_invalid_ip(ip):
    try:
        socket.inet_aton(ip)
        return False
    except:
        return True


def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return False
    else:
        return True


def correct_phone(data):
    try:
        number = data.replace("+", '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if number.isdigit():
            if len(number) >= 11:
                if "+" in data:
                    return number
                else:
                    if number[0] == "8":
                        number = str("7") + number[1:]
                        return number
                    else:
                        return number
    except:
        print(f'{red}Это не номер телефона!\n{white}')
        main()


def replace_item_space(item):
    return item.replace("_", " ")


def correct_domain(domain):
    try:
        correct_domain = domain.replace('http://', '').replace('https://', '').replace('/', '')
        if "." in correct_domain:
            return correct_domain
        else:
            return None
    except:
        return None


def format_output(key, value):
    if key == None or key == '' or key == ' ':
        if len(key) <= 5:
            return f"\n  {key} \t\t\t{value}"
        elif len(key) <= 12:
            return f"\n  {key} \t\t{value}"
        else:
            return f"\n  {key} \t{value}"
    else:
        if len(key) < 5:
            return f"\n{green}> {white}{key}:\t\t\t{value}"
        elif len(key) <= 12:
            return f"\n{green}> {white}{key}:\t\t{value}"
        else:
            return f"\n{green}> {white}{key}:\t{value}"


def api_leak_osint(request):
    try:
        token = token_leak_osint
        send_req = {"token": token, "request": request, "limit": 100, "lang": 'ru', "type": "short"}
        url = 'https://server.leakosint.com/'
        response = requests.post(url, json=send_req)
        answer = response.json()

        result = f"{blue}──────────\t\t────────{white}"

        for key, value in answer.items():
            key_with_space = replace_item_space(key)
            if len(value) == 1 and value[0]:
                result += format_output(key, value[0])
            elif len(value) > 1:
                for i, v in enumerate(value):
                    if not v.strip() and i > 0:
                        result += format_output(" ", v)
                    else:
                        result += format_output(key_with_space if i == 0 else " ", v)
        return result
    except:
        pass


def clean_text(text):
    cleaned_lines = [line.strip() for line in text.split('\n') if line.strip()]
    text_split = '\n'.join(cleaned_lines).split('\n')
    res_edit = []
    for i in text_split:
        res_edit.append(f"\n  {i}")
    res_edit[0] = res_edit[0].replace('\n', '')
    result = ''
    for i in res_edit:
        result += i
    return result
