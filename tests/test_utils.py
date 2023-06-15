from utils import load_data


def test_load_data():
    from_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        }
    ]
    assert load_data('data_test.json') == from_file