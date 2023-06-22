import json


def load_data(file_path):
    """Открывает .json файл"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def number_hide(card_number):
    """Маскирует номер карты"""
    card_number_space = card_number.split(' ')
    number_part = card_number_space[-1]
    if "Счет" not in card_number_space:
        return number_part[:4] + ' ' + number_part[4:6] + '** **** ' + number_part[-4:]
    else:
        return '**' + number_part[-4:]


def filter_sort(data):
    """Выводит последние 5 операций и сортирует их по дате"""
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items[:5]


def convert_date(date):
    """Конвертирует дату в формат ДД.ММ.ГГГГ"""
    new_date = date[:10]
    new_date = new_date.split('-')
    return f"{new_date[2]}.{new_date[1]}.{new_date[0]}"
