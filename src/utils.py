import json


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def number_hide(card_number):
    card_number_space = card_number.split(' ')
    number_part = card_number_space[-1]
    if len(card_number_space) > 2:
        return number_part[:4] + ' ' + number_part[4:6] + '** **** ' + number_part[-4:]
    else:
        if card_number_space[0] == 'Счет':
            return '**' + number_part[-4:]
        return number_part[:4] + ' ' + number_part[4:6] + '** **** ' + number_part[-4:]


def filter_sort(data):
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items[:5]


if __name__ == '__main__':
    dict_ = {
        'a': 1
    }
    print(dict_.get('h'))
