import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value) < 7:
            return int(value)
        

        
def change_contact_menu() -> int:
    print(text.change_contact_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value) < 4:
            return int(value)
        

        
def print_contact_list(contact_list):
    if contact_list:
        for elem in contact_list:
            print(f'ФИО: {elem[0].strip()}\nТелефон: {elem[1].strip()}\n\n')
    else: print_message(text.phone_book_empty)


def print_message(message):
    print('\n'+ '*'*len(message) + '\n')
    print(message)
    print('\n' + '*'*len(message) + '\n')