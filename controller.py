import view
import model
import text

my_pb = model.PhoneBook()

def start():
    pb = my_pb.get_contact_list()
    while True:
       value =  view.main_menu()
       match value:
           case 1:
               view.print_contact_list(pb)
               view.print_message(text.succsesful_message)
           case 2:
               my_pb.add_contact()
               my_pb.save_contact()
               view.print_message(text.succsesful_message)
           case 3:
               search_list, index_for_change = my_pb.search_contact()
               if len(search_list) !=0:
                   view.print_contact_list(search_list)
               else:
                   view.print_message(text.search_fall)
           case 4:
                search_list, index_for_change = my_pb.search_contact()
                flag = 1
                while flag:
                    if len(search_list) > 1: 
                        view.print_message(text.search_message)
                        search_list, index_for_change = my_pb.search_contact()
                    elif len(search_list) == 0: 
                        view.print_message(text.search_fall)
                        search_list, index_for_change = my_pb.search_contact()
                    else:
                        while flag:
                            input_value =  view.change_contact_menu()
                            match input_value:
                                case 1:
                                    ch_contact = my_pb.change_contact(search_list, index_for_change, input_value)
                                    my_pb.save_contact()
                                    view.print_message(text.succsesful_message)
                                    search_list[0] = ch_contact
                                case 2:
                                    ch_contact = my_pb.change_contact(search_list, index_for_change, input_value)
                                    my_pb.save_contact()
                                    view.print_message(text.succsesful_message)
                                    search_list[0] = ch_contact
                                case 3:
                                    view.print_message(text.succsesful_message)
                                    flag = 0               
           case 5:
                search_list, index_for_change = my_pb.search_contact()
                flag = 1
                while flag:
                    if len(search_list) > 1: 
                        view.print_message(text.search_message)
                        search_list, index_for_change = my_pb.search_contact()
                    elif len(search_list) == 0: 
                        view.print_message(text.search_fall)
                        search_list, index_for_change = my_pb.search_contact()
                    else:
                        my_pb.del_contact(index_for_change[0])
                        my_pb.save_contact()
                        view.print_message(text.succsesful_message)
                        
                        flag = 0
           case 6:
               view.print_message(text.bye_message)
               exit()