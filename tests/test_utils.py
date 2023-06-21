from src.utils import convert_date, number_hide, load_data, filter_sort


def test_convert_date():
    assert convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_number_hide():
    assert number_hide("Maestro 1596837868705199") == '1596 83** **** 5199'
    assert number_hide("Счет 64686473678894779589") == '**9589'


def test_load_data():
    assert load_data('tests/test_data.json') == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
