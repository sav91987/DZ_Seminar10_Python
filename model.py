import text


class PhoneBook:

    def __init__(self):
        self.phone_book = []
        self.path = text.file_path

    def get_contact_list(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            contact = data.readline()
            if contact != '':
                my_list = contact.split(';')
            else:
                my_list = []
        for i in range(len(my_list)):
            my_list[i] = tuple(my_list[i].strip().split(','))
            self.phone_book.append(my_list[i])
        return self.phone_book

    def add_contact(self):
        fio = input(text.new_fio)
        phone_number = input(text.new_phone)
        self.phone_book.append((fio, phone_number))

    def search_contact(self):
        search_data = input(text.search_info).lower()
        search_list = []
        index_list = []
        for elem in self.phone_book:
            for elm in elem:
                if search_data in elm.lower():
                    search_list.append(elem)
                    index_list.append(self.phone_book.index(elem))

        return search_list, index_list

    def save_contact(self):
        data = []
        for contact in self.phone_book:
            data.append(','.join(elem for elem in contact))

        data = ';'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def change_contact(self, search_contact_list, index_for_change, input_value):
        new_data = input(text.new_data)
        if input_value == 1:
            for elem in search_contact_list:
                changed_contact = (new_data, elem[1])
        else:
            for elem in search_contact_list:
                changed_contact = (elem[0], new_data)

        self.phone_book.pop(index_for_change[0])
        self.phone_book.insert(index_for_change[0], changed_contact)
        return changed_contact

    def del_contact(self, index_for_change):
        self.phone_book.pop(index_for_change)
