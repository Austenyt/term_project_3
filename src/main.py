from utils import load_data, number_hide, filter_sort, convert_date

file = "operations.json"


def main():
    data = load_data(file)
    sorted_data = filter_sort(data)
    for item in sorted_data:
        date = item.get('date')
        new_date = convert_date(date)
        description = item.get('description')
        sender = item.get('from')
        recipient = item.get('to')
        hide_recipient = number_hide(recipient)
        amount = item.get('operationAmount').get('amount')
        currency = item.get('operationAmount').get('currency').get('name')
        recipient_name = ' '.join(recipient.split()[:-1])

        if sender:
            sender_name_list = sender.split(' ')
            sender_name = ' '.join(sender_name_list[:-1])
            hide_sender = number_hide(sender)
            print(
                f'{new_date} {description}\n{sender_name} {hide_sender} -> {recipient_name} {hide_recipient}\n{amount} {currency}\n')
        else:
            print(f'{new_date} {description}\n{recipient_name} {hide_recipient}\n{amount} {currency}\n')


main()
